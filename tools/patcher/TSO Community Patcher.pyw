#!/usr/bin/env python3
"""TSO Community Patcher: patch TimeSplitters: Future Perfect for the TSO Community Patch.

Xbox: turn the player's own default.xbe into the TSO Community Patch XBE, then put it
into the game's disc image (as default.xbe) or save it as a file.
PS2: build a PCSX2 .pnach into the game's ISO.
Both can be undone with "Restore original ISO/XBE" (Xbox) or "Restore original ISO" (PS2).
"""

import json
import os
import queue
import subprocess
import sys
import threading
import traceback
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pmd import core, ps2patch, update  # noqa: E402
from pmd.xbe import parse_xbe_header  # noqa: E402

APP = "TSO Community Patcher"
SETTINGS = os.path.join(os.path.expanduser("~"), ".tso_community_patcher.json")
OLD_SETTINGS = os.path.join(os.path.expanduser("~"), ".patchmedaddy.json")  # PatchmeDaddy, the patcher's old name
DEFAULT_BACKUPS = os.path.join(os.path.expanduser("~"), "Documents", "TSO Community Patcher Backups")
OLD_BACKUPS = os.path.join(os.path.expanduser("~"), "Documents", "PatchmeDaddy Backups")
XBOX_REGIONS = {0x4541000D: "Europe", 0x45410066: "USA"}


def human(n):
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return ("%d %s" % (n, unit)) if unit == "B" else ("%.1f %s" % (n, unit))
        n /= 1024.0


def open_in_explorer(path):
    if sys.platform.startswith("win"):
        os.startfile(path)  # noqa
    elif sys.platform == "darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


def see_through(widget, alpha):
    """Let the background picture show through a panel (Windows 8 and later: a layered child window).
    Anywhere else, or if Windows refuses, the panel just stays solid."""
    if not sys.platform.startswith("win"):
        return
    try:
        import ctypes
        user32 = ctypes.windll.user32
        hwnd = widget.winfo_id()
        GWL_EXSTYLE, WS_EX_LAYERED, LWA_ALPHA = -20, 0x80000, 2
        user32.SetWindowLongW(hwnd, GWL_EXSTYLE, user32.GetWindowLongW(hwnd, GWL_EXSTYLE) | WS_EX_LAYERED)
        user32.SetLayeredWindowAttributes(hwnd, 0, int(alpha * 255), LWA_ALPHA)
    except Exception:
        pass


class App(tk.Tk):
    SECTIONS = (("xbox", "XBOX/XEMU", "Make the TSO Community Patch from your own XBE/ISO"),
                ("ps2", "PS2/PCSX2", "Build a pnach into your PS2 ISO"))
    NAV_ON, NAV_OFF, NAV_HOVER = "#2b65d9", "#e4e7ec", "#d2d9e6"
    PANEL_ALPHA = 0.86  # how solid the menu tiles and page are over the background picture

    def __init__(self):
        super().__init__()
        self.title(APP + " - TimeSplitters: Future Perfect")
        self.geometry("900x680")
        self.minsize(760, 500)
        self.q = queue.Queue()
        self.busy = False
        self.settings = self._load_settings()
        self.xbox_iso = tk.StringVar(value=self.settings.get("xbox_iso", ""))
        self.src_xbe = tk.StringVar(value=self.settings.get("src_xbe", ""))
        self.xbe_source = tk.StringVar(value=self.settings.get("xbe_source", "iso"))
        self.backup_dir = tk.StringVar(value=self.settings.get(
            "backup_dir", OLD_BACKUPS if os.path.isdir(OLD_BACKUPS) else DEFAULT_BACKUPS))
        self.ps2_pnach = tk.StringVar(value=self.settings.get("ps2_pnach", ""))
        self.ps2_iso = tk.StringVar(value=self.settings.get("ps2_iso", ""))
        self.xbox_target = None
        self._build()
        self.after(100, self._poll)

    # -- settings / plumbing ---------------------------------------------------

    def _load_settings(self):
        for p in (SETTINGS, OLD_SETTINGS):
            try:
                with open(p, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {}

    def save_settings(self):
        s = {"xbox_iso": self.xbox_iso.get(), "src_xbe": self.src_xbe.get(), "xbe_source": self.xbe_source.get(),
             "save_dir": self.settings.get("save_dir", ""), "backup_dir": self.backup_dir.get(),
             "ps2_pnach": self.ps2_pnach.get(), "ps2_iso": self.ps2_iso.get()}
        try:
            with open(SETTINGS, "w", encoding="utf-8") as f:
                json.dump(s, f, indent=2)
        except Exception:
            pass

    def log(self, msg):
        self.q.put(("log", msg))

    def _poll(self):
        try:
            while True:
                kind, val = self.q.get_nowait()
                if kind == "log":
                    self.logbox.configure(state="normal")
                    self.logbox.insert("end", val + "\n")
                    self.logbox.see("end")
                    self.logbox.configure(state="disabled")
                elif kind == "call":
                    val()
        except queue.Empty:
            pass
        self.after(80, self._poll)

    def run_bg(self, fn, done=None):
        """Run fn in a worker thread; call done(result) on the UI thread."""
        if self.busy:
            messagebox.showinfo(APP, "Still working on the last task, please wait.")
            return
        self.busy = True
        self.config(cursor="watch")

        def worker():
            try:
                r = fn()
                err = None
            except Exception as e:  # report every failure in the log and a dialog
                r, err = None, e
                self.log("ERROR: %s" % e)
                self.log(traceback.format_exc().strip().splitlines()[-1])

            def finish():
                self.busy = False
                self.config(cursor="")
                if err is not None:
                    messagebox.showerror(APP, str(err))
                elif done:
                    done(r)
            self.q.put(("call", finish))
        threading.Thread(target=worker, daemon=True).start()

    # -- layout ----------------------------------------------------------------

    def _build(self):
        # background.png (next to the program or in the exe) fills the window; everything else sits on top
        # with a margin, so the picture shows around the menu tiles and the page.
        bg_path = os.path.join(getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__))), "background.png")
        m = 0
        if os.path.isfile(bg_path):
            try:
                self.bg_image = tk.PhotoImage(file=bg_path)
                tk.Label(self, image=self.bg_image, bd=0).place(relx=0.5, rely=0.5, anchor="center")
                m = 18
            except tk.TclError:
                pass
        nav_h = 78
        self.nav = {}
        for i, (key, title, sub) in enumerate(self.SECTIONS):
            box = tk.Frame(self, bd=2, relief="raised", cursor="hand2", bg=self.NAV_OFF)
            box.place(relx=i / 2.0, x=m + 4 if i == 0 else m / 2 + 4, y=m + 8, relwidth=0.5,
                      width=-(1.5 * m + 8), height=nav_h)
            t = tk.Label(box, text=title, font=("TkDefaultFont", 13, "bold"), bg=self.NAV_OFF, cursor="hand2")
            t.pack(padx=10, pady=(12, 0))
            d = tk.Label(box, text=sub, font=("TkDefaultFont", 9), bg=self.NAV_OFF, cursor="hand2")
            d.pack(padx=10, pady=(2, 12))
            for w in (box, t, d):
                w.bind("<Button-1>", lambda e, k=key: self.show_section(k))
                w.bind("<Enter>", lambda e, k=key: self._nav_paint(k, hover=True))
                w.bind("<Leave>", lambda e, k=key: self._nav_paint(k))
            self.nav[key] = (box, t, d)
        top = m + 8 + nav_h + max(m, 8)
        body = ttk.Frame(self)
        body.place(x=m, y=top, relwidth=1, width=-2 * m, relheight=1, height=-(top + m))

        self.page_area = ttk.Frame(body)
        self.page_area.pack(fill="both", expand=True, padx=6, pady=4)
        self.pages = {}
        style = ttk.Style(self)
        style.configure("Big.TButton", font=("TkDefaultFont", 12), padding=8)
        self._build_xbox_page(self._page("xbox"))
        self._build_ps2_page(self._page("ps2"))
        self.section = None

        bottom = ttk.Frame(body)
        bottom.pack(fill="x", padx=6, pady=4)
        row = ttk.Frame(bottom)
        row.pack(fill="x")
        ttk.Label(row, text="Originals are saved in:", foreground="#555").pack(side="left")
        ttk.Label(row, textvariable=self.backup_dir, foreground="#555").pack(side="left", padx=4)
        ttk.Button(row, text="Open", command=self.open_backup_dir).pack(side="right")
        ttk.Button(row, text="Change...", command=self.browse_backup_dir).pack(side="right", padx=4)
        self.logbox = tk.Text(bottom, height=6, state="disabled", wrap="word")
        self.logbox.pack(fill="x", pady=(4, 0))
        self.show_section("xbox")
        if m:
            self.update_idletasks()
            for w in [n[0] for n in self.nav.values()] + [body]:
                see_through(w, self.PANEL_ALPHA)

    def _page(self, key):
        f = ttk.Frame(self.page_area)
        self.pages[key] = f
        return f

    def _nav_paint(self, key, hover=False):
        on = key == self.section
        bg = self.NAV_ON if on else (self.NAV_HOVER if hover else self.NAV_OFF)
        box, t, d = self.nav[key]
        box.configure(bg=bg, relief="sunken" if on else "raised")
        t.configure(bg=bg, fg="white" if on else "black")
        d.configure(bg=bg, fg="white" if on else "#444")

    def show_section(self, key):
        self.section = key
        for k, f in self.pages.items():
            if k != key:
                f.pack_forget()
        self.pages[key].pack(fill="both", expand=True)
        for k in self.nav:
            self._nav_paint(k)

    def browse_backup_dir(self):
        p = filedialog.askdirectory(title="Where to save originals", initialdir=self.backup_dir.get())
        if p:
            self.backup_dir.set(os.path.normpath(p))
            self.save_settings()
            self.xbox_check()
            self.ps2_check()

    def open_backup_dir(self):
        os.makedirs(self.backup_dir.get(), exist_ok=True)
        open_in_explorer(self.backup_dir.get())

    # -- Xbox page -------------------------------------------------------------

    def _build_xbox_page(self, tab):
        pad = {"padx": 8, "pady": 6}
        ttk.Label(tab, text="Makes the TSO Community Patch from your own copy of the game. Close xemu if you are patching an Xbox ISO.",
                  wraplength=780, foreground="#555").pack(anchor="w", **pad)
        up = ttk.Frame(tab)
        up.pack(fill="x", padx=8)
        self.update_info = ttk.Label(up, text="", foreground="#555")
        self.update_info.pack(side="left")
        ttk.Button(up, text="Check for updates", command=lambda: self.check_updates(quiet=False)).pack(side="right")

        a = ttk.LabelFrame(tab, text="1. Apply patch to... (pick one)")
        a.pack(fill="x", **pad)
        ttk.Radiobutton(a, text="My disc image (.iso):", value="iso", variable=self.xbe_source
                        ).grid(row=0, column=0, sticky="w", padx=8, pady=(6, 0))
        ttk.Entry(a, textvariable=self.xbox_iso).grid(row=0, column=1, sticky="ew", padx=4, pady=(6, 0))
        ttk.Button(a, text="Choose...", command=self.xbox_browse_iso).grid(row=0, column=2, padx=8, pady=(6, 0))
        self.xbox_iso_info = ttk.Label(a, text="", foreground="#555")
        self.xbox_iso_info.grid(row=1, column=1, columnspan=2, sticky="w", padx=4)
        ttk.Radiobutton(a, text="A default.xbe file:", value="file", variable=self.xbe_source
                        ).grid(row=2, column=0, sticky="w", padx=8, pady=(6, 0))
        ttk.Entry(a, textvariable=self.src_xbe).grid(row=2, column=1, sticky="ew", padx=4, pady=(6, 0))
        ttk.Button(a, text="Choose...", command=self.browse_xbe).grid(row=2, column=2, padx=8, pady=(6, 0))
        ttk.Label(a, text=core.source_hint(),
                  foreground="#555", wraplength=640, justify="left").grid(row=3, column=1, columnspan=2, sticky="w", padx=4)
        self.src_info = ttk.Label(a, text="", wraplength=760, justify="left")
        self.src_info.grid(row=4, column=0, columnspan=3, sticky="w", padx=8, pady=(8, 6))
        a.columnconfigure(1, weight=1)

        c = ttk.LabelFrame(tab, text="2. Patch")
        c.pack(fill="x", **pad)
        row = ttk.Frame(c)
        row.pack(fill="x", **pad)
        ttk.Button(row, text="Apply patch", style="Big.TButton", command=self.xbox_apply).pack(side="left")
        ttk.Button(row, text="Restore original ISO/XBE", command=self.xbox_restore).pack(side="left", padx=12)

        self.xbox_iso.trace_add("write", lambda *a: self.xbox_check())
        self.src_xbe.trace_add("write", lambda *a: self.describe_source())
        self.xbe_source.trace_add("write", lambda *a: (self.save_settings(), self.describe_source()))
        self.xbox_check()
        self.show_patch_version()
        self.after(500, lambda: self.check_updates(quiet=True))

    def show_patch_version(self, extra=""):
        try:
            text = "Makes TSO Community Patch %s." % core.tso_patch().version
        except Exception as e:
            text = str(e)
        self.update_info.configure(text=text + ((" " + extra) if extra else ""))

    def check_updates(self, quiet):
        """Fetch the newest patch data in the background (at start, and from the button)."""
        try:
            current = core.tso_patch().version
        except Exception:
            current = ""
        self.update_info.configure(text="Checking for a newer TSO Community Patch...")

        def worker():
            try:
                newer, err = update.check(current), None
            except Exception as e:
                newer, err = None, e
            self.q.put(("call", lambda: done(newer, err)))

        def done(newer, err):
            if err is not None:
                self.show_patch_version("Couldn't check for updates.")
                if not quiet:
                    messagebox.showwarning(APP, "Couldn't check for updates (no internet connection, or GitHub "
                                                "can't be reached).\n\n%s" % err)
                return
            if newer:
                core.reload_tso_patch()
                self.show_patch_version("Updated just now.")
                self.log("Downloaded the patch data for the TSO Community Patch %s." % newer)
                self.xbox_check()
                if not quiet:
                    messagebox.showinfo(APP, "Updated: the patcher now makes the TSO Community Patch %s." % newer)
            else:
                self.show_patch_version("Up to date.")
                if not quiet:
                    messagebox.showinfo(APP, "You have the latest TSO Community Patch (%s)." % current)
        threading.Thread(target=worker, daemon=True).start()

    def xbox_browse_iso(self):
        cur = self.xbox_iso.get()
        p = filedialog.askopenfilename(title="Pick your TimeSplitters: Future Perfect Xbox disc image",
                                       initialdir=os.path.dirname(cur) if cur else None,
                                       filetypes=[("Xbox disc images", "*.iso *.xiso"), ("All files", "*.*")])
        if p:
            self.xbox_iso.set(os.path.normpath(p))
            if not self.src_xbe.get().strip():
                self.xbe_source.set("iso")
            self.save_settings()

    def xbox_check(self):
        """Describe the picked disc image. Returns its target when it's TSFP."""
        p = self.xbox_iso.get().strip()
        self.xbox_target = None
        if not p:
            self.xbox_iso_info.configure(text="", foreground="#555")
        else:
            try:
                t = core.find_iso_game(p)
                if not (t.info and t.info.is_tsfp):
                    self.xbox_iso_info.configure(text="This is \"%s\", not TimeSplitters: Future Perfect."
                                                      % ((t.info.title_name if t.info else "") or "an unknown game"),
                                                 foreground="#b00")
                else:
                    orig = core.original_backup(self.backup_dir.get(), t)
                    if orig is not None and core.iso_xbe_sha1(t) != orig.get("sha1"):
                        text = "OK: TimeSplitters: Future Perfect, already patched (the original is saved)"
                    else:
                        region = XBOX_REGIONS.get(t.info.title_id, "")
                        text = "OK: TimeSplitters: Future Perfect%s" % ((" " + region) if region else "")
                    self.xbox_iso_info.configure(text=text, foreground="#070")
                    self.xbox_target = t
            except Exception as e:
                self.xbox_iso_info.configure(text=str(e) if os.path.isfile(p) else "File not found.", foreground="#b00")
        self.describe_source()
        return self.xbox_target

    def browse_xbe(self):
        cur = self.src_xbe.get()
        p = filedialog.askopenfilename(title="Pick your TimeSplitters: Future Perfect default.xbe",
                                       initialdir=os.path.dirname(cur) if cur else None,
                                       filetypes=[("Xbox executables", "*.xbe"), ("All files", "*.*")])
        if p:
            self.src_xbe.set(os.path.normpath(p))
            self.xbe_source.set("file")
            self.save_settings()

    def source_data(self):
        """(bytes, what) of the player's default.xbe (step 1), or raise with what to fix."""
        if self.xbe_source.get() == "file":
            p = self.src_xbe.get().strip()
            if not p:
                raise ValueError("Choose your default.xbe file.")
            with open(p, "rb") as f:
                return f.read(), "This file"
        if self.xbox_target is None:
            raise ValueError("Choose your disc image.")
        if core.original_backup(self.backup_dir.get(), self.xbox_target) is not None:
            what = "The original saved when this disc image was first patched"
        else:
            what = "The disc image's default.xbe"
        return core.original_iso_xbe(self.backup_dir.get(), self.xbox_target), what

    def describe_source(self):
        """Show what the step 1 XBE is. Returns its bytes when it can become the TSO build."""
        data = None
        try:
            data, what = self.source_data()
            ok, text = core.describe_xbe(data, what)
        except OSError:
            ok, text = False, "File not found."
        except Exception as e:
            ok, text = False, str(e)
        self.src_info.configure(text=("\u2714  " if ok else "\u2718  ") + text, foreground="#070" if ok else "#b00")
        return data if ok else None

    def _tso_or_warn(self):
        data = self.describe_source()
        if data is None:
            messagebox.showerror(APP, self.src_info["text"].lstrip("\u2714\u2718 ") or "Choose your default.xbe in step 1.")
        return data

    def xbox_apply(self):
        """One button: patch the disc image, or save the patched default.xbe as a new file."""
        if self.xbe_source.get() == "file":
            self.xbox_save()
        else:
            self.xbox_patch()

    def xbox_save(self):
        data = self._tso_or_warn()
        if data is None:
            return
        cur = self.settings.get("save_dir") or (os.path.dirname(self.src_xbe.get()) if self.src_xbe.get() else None)
        p = filedialog.asksaveasfilename(title="Save the TSO Community Patch XBE", initialdir=cur,
                                         initialfile="TSO Community Patch.xbe", defaultextension=".xbe",
                                         filetypes=[("Xbox executables", "*.xbe")])
        if not p:
            return
        p = os.path.normpath(p)
        if os.path.isfile(p) and os.path.isfile(self.src_xbe.get()) and os.path.samefile(p, self.src_xbe.get()) and not messagebox.askyesno(
                APP, "That is the file you picked in step 1. Replace it with the TSO Community Patch?\n\n"
                     "(Keep a copy of your original somewhere first.)", icon="warning", default="no"):
            return
        self.settings["save_dir"] = os.path.dirname(p)
        self.save_settings()
        ver = core.tso_patch().version
        self.run_bg(lambda: core.save_xbe(core.make_tso_xbe(data), p, log=self.log),
                    lambda _: messagebox.showinfo(APP, "Saved the TSO Community Patch %s:\n\n%s" % (ver, p)))

    def xbox_patch(self):
        target = self.xbox_check()
        if target is None:
            messagebox.showwarning(APP, "Choose the disc image to patch in step 1.")
            return
        data = self._tso_or_warn()
        if data is None:
            return
        if core.xemu_running():
            messagebox.showerror(APP, "xemu is still running.\n\nClose xemu completely, then try again.")
            return
        bdir = self.backup_dir.get()
        ver = core.tso_patch().version
        self.save_settings()

        def work():
            new = core.make_tso_xbe(data)
            self.log("Made the TSO Community Patch %s from your default.xbe (checked)." % ver)
            return core.patch_iso(target.iso_path, target, new, bdir, label="the TSO Community Patch " + ver, log=self.log)

        def done(_):
            self.xbox_check()
            messagebox.showinfo(APP, "Patched!\n\n%s now starts the TSO Community Patch %s.\n\nStart xemu and boot the game "
                                     "fresh (don't load a save state made before patching)." % (os.path.basename(target.iso_path), ver))
        self.run_bg(work, done)

    def xbox_restore(self):
        target = self.xbox_check()
        if target is None:
            messagebox.showinfo(APP, "Choose the disc image in step 1 first.")
            return
        if core.original_backup(self.backup_dir.get(), target) is None:
            messagebox.showinfo(APP, "There is no saved original for this disc image.\n\n"
                                     "It is saved automatically the first time you patch.")
            return
        if core.xemu_running():
            messagebox.showerror(APP, "xemu is still running.\n\nClose xemu completely, then try again.")
            return
        if not messagebox.askyesno(APP, "Put the original default.xbe back in %s?" % os.path.basename(target.iso_path)):
            return
        bdir = self.backup_dir.get()
        self.run_bg(lambda: core.restore_original(target, bdir, log=self.log),
                    lambda _: (self.xbox_check(), messagebox.showinfo(APP, "The original is back.")))

    # -- PS2 page --------------------------------------------------------------

    def _build_ps2_page(self, tab):
        pad = {"padx": 8, "pady": 6}
        ttk.Label(tab, text="Builds a PCSX2 .pnach into a TimeSplitters: Future Perfect PS2 ISO (USA or Europe). "
                            "Close PCSX2 first.",
                  wraplength=780, foreground="#555").pack(anchor="w", **pad)

        a = ttk.LabelFrame(tab, text="1. Your pnach file")
        a.pack(fill="x", **pad)
        ttk.Entry(a, textvariable=self.ps2_pnach).grid(row=0, column=0, sticky="ew", **pad)
        ttk.Button(a, text="Choose...", command=self.ps2_browse_pnach).grid(row=0, column=1, **pad)
        self.ps2_pnach_info = ttk.Label(a, text="")
        self.ps2_pnach_info.grid(row=1, column=0, columnspan=2, sticky="w", padx=8, pady=(0, 6))
        a.columnconfigure(0, weight=1)

        b = ttk.LabelFrame(tab, text="2. The TimeSplitters: Future Perfect PS2 ISO to change")
        b.pack(fill="x", **pad)
        ttk.Entry(b, textvariable=self.ps2_iso).grid(row=0, column=0, sticky="ew", **pad)
        ttk.Button(b, text="Choose...", command=self.ps2_browse_iso).grid(row=0, column=1, **pad)
        self.ps2_iso_info = ttk.Label(b, text="")
        self.ps2_iso_info.grid(row=1, column=0, columnspan=2, sticky="w", padx=8, pady=(0, 6))
        b.columnconfigure(0, weight=1)

        c = ttk.LabelFrame(tab, text="3. Patch")
        c.pack(fill="x", **pad)
        self.ps2_match = tk.Label(c, text="", font=("TkDefaultFont", 11, "bold"), anchor="w", justify="left", wraplength=780)
        self.ps2_match.pack(fill="x", **pad)
        ttk.Label(c, text="The original game file is kept inside the ISO and a copy is saved to your backup folder, "
                          "so \"Restore original ISO\" restores the ISO without the patch.",
                  wraplength=780, foreground="#555").pack(anchor="w", padx=8)
        row = ttk.Frame(c)
        row.pack(fill="x", **pad)
        ttk.Button(row, text="Apply patch", style="Big.TButton", command=self.ps2_patch).pack(side="left")
        ttk.Button(row, text="Restore original ISO", command=lambda: self.ps2_restore(None)).pack(side="left", padx=12)

        self.ps2_pnach.trace_add("write", lambda *a: self.ps2_check())
        self.ps2_iso.trace_add("write", lambda *a: self.ps2_check())
        self.ps2_check()

    def ps2_browse_pnach(self):
        cur = self.ps2_pnach.get()
        p = filedialog.askopenfilename(title="Pick the pnach file", initialdir=os.path.dirname(cur) if cur else None,
                                       filetypes=[("PCSX2 patch files", "*.pnach"), ("All files", "*.*")])
        if p:
            self.ps2_pnach.set(os.path.normpath(p))
            self.save_settings()

    def ps2_browse_iso(self):
        cur = self.ps2_iso.get()
        p = filedialog.askopenfilename(title="Pick the TimeSplitters: Future Perfect PS2 ISO",
                                       initialdir=os.path.dirname(cur) if cur else None,
                                       filetypes=[("PS2 disc images", "*.iso"), ("All files", "*.*")])
        if p:
            self.ps2_iso.set(os.path.normpath(p))
            self.save_settings()

    def ps2_check(self):
        """Describe both files and whether they match. Returns True when patching can go ahead."""
        pn_path, iso_path = self.ps2_pnach.get().strip(), self.ps2_iso.get().strip()
        ok_pn = ok_iso = False
        if not pn_path:
            self.ps2_pnach_info.configure(text="")
        else:
            try:
                pn = ps2patch.Pnach(pn_path)
                v = ps2patch.pnach_version(pn)
                if v in ps2patch.TSFP_VERSIONS:
                    self.ps2_pnach_info.configure(text="OK: for %s, %d patch lines" % (ps2patch.describe_crc(v), len(pn.writes)),
                                                  foreground="#070")
                    ok_pn = True
                elif v is None:
                    self.ps2_pnach_info.configure(text="Can't tell which version this pnach is for "
                                                       "(the file name should end with the CRC, like _FB2F4502.pnach)",
                                                  foreground="#b00")
                else:
                    self.ps2_pnach_info.configure(text="This pnach is for a different game (CRC %08X)" % v, foreground="#b00")
            except Exception as e:
                self.ps2_pnach_info.configure(text=str(e) if os.path.isfile(pn_path) else "File not found.", foreground="#b00")
        if not iso_path:
            self.ps2_iso_info.configure(text="")
        else:
            try:
                undo = core.ps2_patched_record(self.backup_dir.get(), iso_path)
                if undo:
                    self.ps2_iso_info.configure(text="OK: TimeSplitters: Future Perfect %s, already has %s built in"
                                                     % (ps2patch.describe_crc(undo["crc"]), undo.get("pnach", "a pnach")),
                                                foreground="#070")
                    ok_iso = True
                else:
                    info = ps2patch.inspect_iso(iso_path)
                    if info["version"]:
                        self.ps2_iso_info.configure(text="OK: TimeSplitters: Future Perfect %s" % ps2patch.describe_crc(info["crc"]),
                                                    foreground="#070")
                        ok_iso = True
                    else:
                        self.ps2_iso_info.configure(text="Not TimeSplitters: Future Perfect (USA or Europe). Its game file is %s."
                                                         % info["boot"], foreground="#b00")
            except Exception as e:
                self.ps2_iso_info.configure(text=str(e) if os.path.isfile(iso_path) else "File not found.", foreground="#b00")
        if ok_pn and ok_iso:
            try:
                core.check_ps2(pn_path, iso_path, self.backup_dir.get())
                self.ps2_match.configure(text="\u2714  The pnach and the ISO are the same version. Ready to patch.", fg="#070")
                return True
            except Exception as e:
                want = ps2patch.pnach_version(ps2patch.Pnach(pn_path))
                undo = core.ps2_patched_record(self.backup_dir.get(), iso_path)
                have = undo["crc"] if undo else ps2patch.inspect_iso(iso_path)["crc"]
                if want != have:
                    msg = "Wrong version: this pnach is for %s, but the ISO is %s." % (
                        ps2patch.describe_crc(want), ps2patch.describe_crc(have))
                else:
                    msg = str(e)
                self.ps2_match.configure(text="\u2718  " + msg, fg="#b00")
                return False
        self.ps2_match.configure(text="Pick a pnach and an ISO above." if not (pn_path and iso_path) else
                                 "\u2718  Fix the problem shown above first.", fg="#b00" if pn_path and iso_path else "#555")
        return False

    def ps2_patch(self):
        pn_path, iso_path = self.ps2_pnach.get().strip(), self.ps2_iso.get().strip()
        if not pn_path or not iso_path:
            messagebox.showwarning(APP, "Pick the pnach (step 1) and the ISO (step 2) first.")
            return
        try:
            core.check_ps2(pn_path, iso_path, self.backup_dir.get())
        except Exception as e:
            messagebox.showerror(APP, str(e))
            return
        if core.pcsx2_running() and not messagebox.askyesno(
                APP, "PCSX2 looks like it's running. Close the game in PCSX2 first.\n\nPatch anyway?", icon="warning", default="no"):
            return
        bdir = self.backup_dir.get()
        self.save_settings()
        self.run_bg(lambda: core.patch_ps2_iso(pn_path, iso_path, bdir, log=self.log),
                    lambda _: (self.ps2_check(),
                               messagebox.showinfo(APP, "Patched!\n\n%s now has the pnach built in.\n\nBoot it in PCSX2 "
                                                        "(turn the pnach itself off so it isn't applied twice)."
                                                   % os.path.basename(iso_path))))

    def ps2_restore(self, rec):
        if rec is None:
            iso_path = self.ps2_iso.get().strip()
            rec = core.ps2_patched_record(self.backup_dir.get(), iso_path) if iso_path else None
            if rec is None:
                messagebox.showinfo(APP, "This ISO doesn't have a pnach built in by this patcher, so there's nothing to undo.")
                return
        if not messagebox.askyesno(APP, "Put the original game file back in %s?" % os.path.basename(rec["iso_path"])):
            return
        self.run_bg(lambda: core.restore_ps2_iso(rec, log=self.log),
                    lambda _: (self.ps2_check(), messagebox.showinfo(APP, "The original is back.")))



if __name__ == "__main__":
    App().mainloop()

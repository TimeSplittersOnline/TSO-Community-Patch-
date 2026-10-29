"""Update check test: a newer tso_patch.dat is downloaded and used once installed; an older or damaged one is not.
Serves the files from a local web server, so it needs no internet. Usage: python tests/test_update.py
"""
import http.server
import os
import shutil
import sys
import tempfile
import threading

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from pmd import core, tsopatch, update  # noqa: E402


def main():
    root = tempfile.mkdtemp()
    os.environ["APPDATA"] = os.path.join(root, "appdata")
    served = os.path.join(root, "web")
    os.makedirs(served)
    handler = lambda *a: http.server.SimpleHTTPRequestHandler(*a, directory=served)  # noqa: E731
    httpd = http.server.HTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    update.URL = "http://127.0.0.1:%d/tso_patch.dat" % httpd.server_port
    web = os.path.join(served, "tso_patch.dat")

    built_in = core.reload_tso_patch().version
    old, new = b"o" * 4096, b"n" * 4096
    tsopatch.make_patch("v99.1", new, [("test", old)], web)
    assert update.check(built_in) == "v99.1"
    assert core.reload_tso_patch().version == built_in        # found, but not used until the player says yes
    update.install_pending()
    assert core.reload_tso_patch().version == "v99.1" and core.make_tso_xbe(old) == new
    assert update.check("v99.1") is None                      # nothing newer
    tsopatch.make_patch("v1.0", new, [("test", old)], web)
    assert update.check(built_in) is None and core.reload_tso_patch().version == "v99.1"  # an older one is ignored
    with open(web, "wb") as f:
        f.write(b"not patch data")
    try:
        update.check(built_in)
        raise AssertionError("damaged patch data was accepted")
    except tsopatch.PatchError:
        pass
    assert core.reload_tso_patch().version == "v99.1"
    assert [f for f in os.listdir(update.data_dir()) if f.endswith(".tmp")] == []
    os.remove(web)
    try:
        update.check(built_in)
        raise AssertionError("a missing file was accepted")
    except OSError:
        pass
    httpd.shutdown()
    shutil.rmtree(root)
    print("update check: newer found, used only after install, older / damaged / missing ignored OK (built in: %s)" % built_in)


if __name__ == "__main__":
    main()

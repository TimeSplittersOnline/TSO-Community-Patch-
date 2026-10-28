"""Minimal XBE header reader: enough to name the game an .xbe belongs to."""

import re
import struct


class XbeInfo:
    def __init__(self, title_id, title_name, timestamp):
        self.title_id = title_id
        self.title_name = title_name
        self.timestamp = timestamp

    @property
    def title_id_str(self):
        tid = self.title_id
        pub = bytes([(tid >> 24) & 0xFF, (tid >> 16) & 0xFF])
        try:
            p = pub.decode("ascii")
        except UnicodeDecodeError:
            p = "??"
        return "%s-%03d (%08X)" % (p, tid & 0xFFFF, tid)

    @property
    def is_tsfp(self):
        """TimeSplitters: Future Perfect only (not TimeSplitters 2 or the first game).

        Title IDs: 4541000D is the Europe disc, 45410066 the USA disc and the TSO community patch."""
        name = re.sub(r"[^a-z0-9]+", " ", self.title_name.lower()).strip()
        return (self.title_id in TSFP_TITLE_IDS or "future perfect" in name
                or name in ("timesplitters fp", "ts fp", "tsfp"))


TSFP_TITLE_IDS = (0x4541000D, 0x45410066)


def parse_xbe_header(data):
    """Parse the first few KB of an XBE. Returns XbeInfo or None if not an XBE."""
    if len(data) < 0x178 or data[:4] != b"XBEH":
        return None
    base, = struct.unpack_from("<I", data, 0x104)
    cert_va, = struct.unpack_from("<I", data, 0x118)
    off = cert_va - base
    if off < 0 or off + 0x5C > len(data):
        return XbeInfo(0, "", 0)
    _size, ts, tid = struct.unpack_from("<III", data, off)
    raw = data[off + 0x0C:off + 0x0C + 80]
    name = raw.decode("utf-16-le", "replace").split("\0", 1)[0].strip()
    return XbeInfo(tid, name, ts)


def is_xbe(data):
    return data[:4] == b"XBEH"

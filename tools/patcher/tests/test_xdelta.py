"""make_xdelta round trip through the real xdelta3. Usage: python3 tests/test_xdelta.py (needs xdelta3)."""
import os, random, subprocess, sys, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
import make_xdelta

rnd = random.Random(1)
work = tempfile.mkdtemp()
src = bytearray(rnd.randbytes(5 << 20))
dst = bytearray(src)
for _ in range(200):                                  # scattered small changes
    a, n = rnd.randrange(len(dst) - 64), rnd.randrange(1, 64)
    dst[a:a + n] = rnd.randbytes(n)
dst[123456:123456 + 100000] = rnd.randbytes(100000)   # a changed block
tail = bytearray(src[1 << 20:(1 << 20) + 3000000])    # appended copy of part of the source, a bit changed
tail[5000:5100] = bytes(100)
dst += tail + bytes(4096)
paths = [os.path.join(work, n) for n in ("a", "b", "p", "out")]
open(paths[0], "wb").write(src)
open(paths[1], "wb").write(dst)
for hint in (None, 1 << 20):
    make_xdelta.make(paths[0], paths[1], paths[2], hint, log=lambda m: None)
    subprocess.run(["xdelta3", "-d", "-f", "-s", paths[0], paths[2], paths[3]], check=True)
    assert open(paths[3], "rb").read() == bytes(dst), hint
    assert os.path.getsize(paths[2]) < (400000 if hint else 3500000), os.path.getsize(paths[2])
    print("hint %s: %d-byte patch, xdelta3 rebuilds the target" % (hint, os.path.getsize(paths[2])))
print("ok")

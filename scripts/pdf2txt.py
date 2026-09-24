"""Copy a downloaded PDF into the lab's downloads/ and dump its text (pymupdf). Usage: pdf2txt.py <src.pdf> <name>"""
import sys, shutil, os
import pymupdf
src, name = sys.argv[1], sys.argv[2]
dst_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "downloads")
pdf = os.path.join(dst_dir, name + ".pdf")
shutil.copyfile(src, pdf)
d = pymupdf.open(pdf)
txt = "\n".join("=== PAGE %d ===\n" % (i + 1) + p.get_text() for i, p in enumerate(d))
open(os.path.join(dst_dir, name + ".txt"), "w", encoding="utf-8").write(txt)
print(pdf, d.page_count, "pages,", len(txt), "chars")

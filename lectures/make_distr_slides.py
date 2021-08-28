#!/usr/bin/env python3

import sys
import re

if len(sys.argv) != 2:
    print("Usage: {} [PDF INPUT]".format(sys.argv[0]))

def exec(*args):
    import subprocess
    with subprocess.Popen(
            list(map(str, args)),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE) as p:
        out, _ = p.communicate()
    return str(out, 'utf-8')

def get_pdf_page_count(pdf):
    for line in exec('pdfinfo', pdf).split("\n"):
        vals = line.split(':', 1)
        if len(vals) == 2 and vals[0] == "Pages":
            return int(vals[1])

def get_pdf_page_text(pdf, page):
    return exec('pdftotext', '-f', page + 1, '-l', page + 1, '-raw', pdf, '-')

# Fetch the frame number of each page
pdf = sys.argv[1]
n_pages = get_pdf_page_count(pdf)
pattern = re.compile('^\s*([0-9]+)\s*/\s*([0-9]+)\s*$', re.MULTILINE)
page_frame_map = {}
for page in range(n_pages):
    txt = get_pdf_page_text(pdf, page)
    frame_no = None, None
    for match in pattern.findall(txt):
        frame_no, _ = map(int, match)
    page_frame_map[page] = frame_no

# Decide which pages to include in the final pdf
last_frame = None
pages = []
for page, frame_no in sorted(page_frame_map.items()):
    if (last_frame is None) or (last_frame != frame_no):
        pages.append(page + 1)
    else:
        pages[-1] = page + 1
    last_frame = frame_no
print("Extracting pages [" + ", ".join(map(str, pages)) + "]")

# Create a new pdf with the selected pages using GhostScript
pdf_parts = pdf.split('.')
tar_pdf = ".".join(pdf_parts[:-1]) + "_distr." + pdf_parts[-1]
print("Writing to " + tar_pdf)
exec(
    'gs',
    '-sDEVICE=pdfwrite',
    '-dNOPAUSE',
    '-dBATCH',
    '-dSAFER',
    '-dPDFSETTINGS=/prepress',
    '-dPrinted=false',
    '-sPageList=' + ','.join(map(str, pages)),
    '-sOutputFile='+tar_pdf, pdf)


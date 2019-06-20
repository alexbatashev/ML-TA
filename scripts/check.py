# -*- coding: utf-8 -*-
import glob, os
import re
import sys

md_pattern = re.compile("[0-9]{2}(_[a-zA-Zа-яА-я0-9_\s]+)?(\.tex\.md)")
docx_pattern = re.compile("[0-9]{2}(_[a-zA-Zа-яА-я0-9_\s]+)?(\.docx)")

is_ok = True

for file in glob.glob("*.tex.md"):
    if not md_pattern.match(file):
        is_ok = False
        sys.stderr.write("Имя файла " + file + " не соответствует соглашению\n")


for file in glob.glob("*.docx"):
    if not docx_pattern.match(file):
        is_ok = False
        sys.stderr.write("Имя файла " + file + " не соответствует соглашению\n")

if not is_ok:
    sys.exit(-1)

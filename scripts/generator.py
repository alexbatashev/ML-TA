# -*- coding: utf-8 -*-
import glob, os
import subprocess

symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
           u"abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA")

tr = {ord(a):ord(b) for a, b in zip(*symbols)}

includes = []

for file in glob.glob("*.tex.md"):
    new_file_name = str(file.replace(".tex.md", ".tex")).translate(tr)
    subprocess.call(['pandoc', '-f', 'markdown-auto_identifiers', '-t', 'latex', file, '-o', new_file_name])
    includes.append(new_file_name)

for file in glob.glob("*.docx"):
    new_file_name = str(file.replace(".docx", ".tex")).translate(tr)
    subprocess.call(['pandoc', '-f', 'docx+latex_macros-hard_line_breaks-empty_paragraphs+superscript+subscript-styles', '-t', 'latex', file, '-o', new_file_name])
    includes.append(new_file_name)

includes.sort()

with open("readable.tex", "w") as file:
    header_file = open("templates/readable_header.tex")
    header = str(header_file.read())
    file.write(header)
    for inp in includes:
        file.write("\\input{"+inp+"}\n")
    file.write("\\end{document}")

with open("printable.tex", "w") as file:
    header_file = open("templates/printable_header.tex")
    header = str(header_file.read())
    file.write(header)
    for inp in includes:
        file.write("\\input{"+inp+"}\n")
        file.write("\\clearpage\n")
    file.write("\end{document}")

subprocess.call(["pdflatex", "readable.tex"])
subprocess.call(["pdflatex", "readable.tex"])
subprocess.call(["pdflatex", "printable.tex"])
subprocess.call(["pdflatex", "printable.tex"])

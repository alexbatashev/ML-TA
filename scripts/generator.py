import glob, os
import subprocess

includes = []

for file in glob.glob("*.tex.md"):
    subprocess.call(['pandoc', '-f', 'markdown-auto_identifiers', '-t', 'latex', file, '-o', file.replace(".tex.md", ".tex")])
    includes.append(file.replace(".tex.md", ".tex"))

for file in glob.glob("*.docx"):
    subprocess.call(['pandoc', '-t', 'latex', file, '-o', file.replace(".docx", ".tex")])
    includes.append(file.replace(".docx", ".tex"))

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

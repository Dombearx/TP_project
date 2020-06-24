import fitz

from fpdf import FPDF

import docx
from docx.shared import RGBColor
from docx2pdf import convert


def readFile(fileName):
    f = open(fileName, "r", encoding="utf-8")
    return f.readlines()


if __name__ == "__main__":
    lines = readFile("test.txt")

    doc = docx.Document()
    for line in lines:
        parag = doc.add_paragraph(line)

    for n, parag in enumerate(doc.paragraphs):
        if (n % 10 == 0):
            run = parag.add_run()
            run.text = parag.text
            run.font.underline = True
            run.font.bold = True
            run.font.color.rgb = RGBColor(0xff, 0x00, 0x00)

    doc.save('result.docx')

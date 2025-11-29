import pandas
from fpdf import FPDF, XPos, YPos
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pandas.read_csv("topics.csv")
pdf.add_page()

pdf.set_font(
    family="Times",
    style="B",
    size=12)
pdf.cell(
    w=0,
    h=12,
    text="Hello There!",
    new_x=XPos.LMARGIN,
    new_y=YPos.NEXT,
    align='L',
    border=1
)


pdf.set_font(family="Times", style="B", size=12)
pdf.cell(
    w=0,
    h=12,
    text="Hi There!",
    new_x=XPos.LMARGIN,
    new_y=YPos.NEXT,
    align='L',
    border=1
)

pdf.add_page()
pdf.set_font(
    family="Times",
    style="B",
    size=12)


pdf.cell(
    w=0,
    h=12,
    text="Hello There!",
    new_x=XPos.LMARGIN,
    new_y=YPos.NEXT,
    align='L',
    border=1
)


pdf.set_font(family="Times", style="B", size=12)
pdf.cell(
    w=0,
    h=12,
    text="Hi There!",
    new_x=XPos.LMARGIN,
    new_y=YPos.NEXT,
    align='L',
    border=1
)

pdf.output("output.pdf")

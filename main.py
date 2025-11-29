from fpdf import FPDF, XPos, YPos
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")


for index, row in df.iterrows():
    pdf.add_page()

    #Set Header
    pdf.set_font(
    family="Times",
    style="B",
    size=12)
    pdf.set_text_color(
        100,
        100,
        100
    )
    pdf.cell(
    w=0,
    h=12,
    text=row["Topic"],
    new_x=XPos.LMARGIN,
    new_y=YPos.NEXT,
    align='L',
    )
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)
    pdf.line(
        10,
        21,
        200,
        21
    )

    # Set the footer
    pdf.ln(265)
    pdf.set_font(
    family="Times",
    style="B",
    size=12)
    pdf.set_text_color(
        180,
        180,
        180
    )
    pdf.cell(
    w=0,
    h=10,
    text=row["Topic"],
    align='R',
    )

    for i in range(row["Pages"]-1):
        pdf.add_page()
        # Set the footer
        pdf.ln(277)
        pdf.set_font(
            family="Times",
            style="B",
            size=12)
        pdf.set_text_color(
            180,
            180,
            180
        )
        pdf.cell(
            w=0,
            h=10,
            text=row["Topic"],
            align='R',
        )
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)


pdf.output("output_lined.pdf")

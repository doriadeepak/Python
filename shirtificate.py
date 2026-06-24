from fpdf import FPDF

name=input("Name: ")

pdf=FPDF(orientation="portrait", format="A4")
pdf.add_page()
pdf.set_font("Helvetica", size=30)
pdf.cell(w=0, h=20, text="CS50 Shirtificate", align="C")
pdf.set_font("Helvetica", size=30)
pdf.image("Shirtificate.png", x=10, y=70, w=190)
pdf.set_xy(0, 120)
pdf.cell(w=210, h=10, text=f"{name} took CS50", align="C")
pdf.output("Shirtificate.pdf")
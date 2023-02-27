import fpdf
import pandas as pd

pdf = fpdf.FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    for page in range(row['Pages']):
        pdf.add_page()
        pdf.set_font(family='Arial', style="B", size=24)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
        pdf.line(10, 25, 200, 25)

        pdf.ln(245)
        pdf.line(10, 270, 200, 270)
        pdf.set_font(family='Arial', style="I", size=10)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)


pdf.output("output.pdf")
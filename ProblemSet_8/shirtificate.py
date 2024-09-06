from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 40)
        self.cell(0, 10, "CS50 Shirtificate", ln=True, align="C")
        self.ln(40)

    def add_shirtificate_content(self, name):
        self.image("shirtificate.png", x=0, y=60, w=self.w)
        self.set_xy(0, 140)
        self.set_font("Arial", "B", 30)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, f'{name} took CS50', align="C")

name = input('Name: ')

pdf = PDF(orientation='portrait', format='A4')
pdf.add_page()
pdf.add_shirtificate_content(name)
pdf.output('shirtificate.pdf')

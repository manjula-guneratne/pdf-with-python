from fpdf import FPDF

class PDF(FPDF):
    def header(self) -> None:
        #logo
        self.image('logo.png', 20,16,50)
        #font
        self.set_font('helvetica', 'B', 30)
        #line break
        self.ln(20)
        #Padding
        self.cell(80)
        #title
        self.cell(30,10,'Title', border=True, align='C')
        #line break
        self.ln(50)

    def footer(self):
        #Set position of the footer
        self.set_y(-15)
        #Set font
        self.set_font('helvetica', 'I', 10)
        #Page number
        self.cell(0,10,f'Page {self.page_no()}/{{nb}}', align='C')

    

pdf = PDF('P','mm', 'Letter')

#Get total page numbers
pdf.alias_nb_pages()

pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

pdf.set_font('helvetica','BIU', size=16)

for i in range(1,41):
    pdf.cell(0, 10, f'This is line {i} :D', ln=1)

pdf.cell(80,10, "Good bye World!")

pdf.output("hello_world.pdf")
from fpdf import FPDF

title = "20,000 Leagues Under the Sea"

class PDF(FPDF):
    def header(self) -> None:
        #font
        self.set_font('helvetica', 'B', 15)

        #Calculate width of title and position
        title_w = self.get_string_width(title) + 6
        doc_w = self.w
        self.set_x((doc_w - title_w)/2)

        # colours of frame, background, and text
        self.set_draw_color(0,80,180) # border = blue
        self.set_fill_color(230, 230, 0) # background = yellow
        self.set_text_color(220, 50, 50) # text = red
        # Thickness of frame (border)
        self.set_line_width(1)
        #Title
        self.cell(title_w, 10, title, border=1, ln=1, align='C', fill=1)

        #line break
        self.ln(50)

    def footer(self):
        #Set position of the footer
        self.set_y(-15)
        #Set font
        self.set_font('helvetica', 'I', 8)
        #Set font colour grey
        self.set_text_color(169, 169, 169)
        #Page number
        self.cell(0,10,f'Page {self.page_no()}/{{nb}}', align='C')

    # Chapter content
    def chapter_body(self, name):
        # read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        #set font
        self.set_font('times', '', 12)
        #insert text
        self.multi_cell(0,5,txt)
        #line break
        self.ln()

    

pdf = PDF('P','mm', 'Letter')

#Get total page numbers
pdf.alias_nb_pages()

pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

pdf.set_font('helvetica','BIU', size=16)

for i in range(1,41):
    pdf.cell(0, 10, f'This is line {i} :D', ln=1)

pdf.cell(80,10, "Good bye World!")

pdf.output("Leagues.pdf")
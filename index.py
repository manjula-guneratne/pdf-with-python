from fpdf import FPDF

pdf = FPDF('P','mm', 'Letter')
pdf.add_page()
pdf.set_font('helvetica', size=16)

pdf.cell(40,10,"hello world", border=True)
pdf.cell(80,10, "Good bye World!")

pdf.output("hello_world.pdf")
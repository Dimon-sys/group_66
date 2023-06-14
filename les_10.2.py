from fpdf import FPDF

pdf = FPDF('P', 'cm', (10, 15))
pdf.add_page()

pdf.set_font('Arial', size=16)
pdf.set_text_color(0,255,0)
pdf.set_fill_color(155,50,168)
pdf.set_draw_color(0,0,255)

pdf.cell(10,5, txt = 'Hello!', align='C', border=1, fill=True)

pdf.image('pic.jpg', h=0, w=10, x=0, y=5)

pdf.output('test_fpdf4.pdf')
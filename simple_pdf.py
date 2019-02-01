from reportlab.pdfgen import canvas

c = canvas.Canvas('simple.pdf')
c.drawString(150,200,"simple pdf here ")
c.save()

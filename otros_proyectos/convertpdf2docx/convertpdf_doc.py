from pdf2docx import Converter
pdf_file = '/otros_proyectos/convertpdf2docx/Griffith College.pdf'
docx_file='sample.docx'
cv=Converter(pdf_file)
cv.convert(docx_file)
cv.close()
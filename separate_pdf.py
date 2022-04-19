pip install pypdf2==1.25.0

from PyPDF2 import PdfFileWriter, PdfFileReader
#change document.pdf name to your input file path if not same directory/"document_name".pdf
input_pdf=PdfFileReader(open("document.pdf","rb"))

for i in range(input_pdf.numPages):
    output = PdfFileWriter()
    output.addPage(input_pdf.getPage(i))
    #change document in document-page%s.pdf name to your "document_name".pdf
    with open("document-page%s.pdf"%i, "wb") as outputStream:
        output.write(outputStream)

# main program
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def marge_file(file1, file2, output):
    pdf_writer = PdfFileWriter()
    pdf_reader_1 = PdfFileReader(file1)
    pdf_reader_2 = PdfFileReader(file2)

    numpage1 = pdf_reader_1.getNumPages()
    numpage2 =pdf_reader_2.getNumPages()

    maxpage = numpage1
    if(numpage1 < numpage2):
        maxpage = numpage2
    
    for page in range(maxpage):
        if(page < numpage1):
            pdf_writer.addPage(pdf_reader_1.getPage(page))
        if(page < numpage2):
            pdf_writer.addPage(pdf_reader_2.getPage(page))
    with open(output, 'wb') as out:
        pdf_writer.write(out)
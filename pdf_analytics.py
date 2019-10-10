import io
 
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

import buzzwords
 
def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
 
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
 
        text = fake_file_handle.getvalue()
 
    converter.close()
    fake_file_handle.close()
 
    if text:
        return text
 
if __name__ == '__main__':
    splitted = extract_text_from_pdf('main.pdf').split()
    splitted = [x.lower() for x in splitted]
    for w in buzzwords.general:
        count = [w.lower() in x for x in splitted].count(True)
        if count > 0:
            print(w + ": ")
            print(str(count) + "\n")
    for w in buzzwords.bigData:
        count = [w.lower() in x for x in splitted].count(True)
        if count > 0:
            print(w + ": ")
            print(str(count) + "\n")
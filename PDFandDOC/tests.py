from django.test import TestCase
import win32com.client
import os
import comtypes.client
import time


def pdftodoc(doc_pdf):
    word = win32com.client.Dispatch("Word.Application")
    word.visible = 0
    input_file = os.path.abspath(doc_pdf)
    wb = word.Documents.Open(input_file)
    try:
        output_file = os.path.abspath(doc_pdf[0:-4]+".docx" )
        wb.SaveAs2(output_file, FileFormat=16)
        wb.Close()
        word.Quit()
    except:
        wb.Close()
        word.Quit()
        print("Failed TO Convert")
        return False
    return True
pdftodoc('../static/media/hello.pdf')

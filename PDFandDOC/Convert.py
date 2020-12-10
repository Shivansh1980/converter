import win32com.client
import os
import comtypes.client
import time


def pdftoword(doc_pdf):
    word = win32com.client.Dispatch("Word.Application")
    word.visible = 0
    input_file = os.path.abspath(doc_pdf)
    wb = word.Documents.Open(input_file)
    try:
        output_file = os.path.abspath(doc_pdf[0:-4]+".docx")
        wb.SaveAs2(output_file, FileFormat=16)
        wb.Close()
        word.Quit()
        return True
    except:
        wb.Close()
        word.Quit()
        print("Failed TO Convert")
        return False


def wordtopdf(doc_docx):
    formate_code = 17

    file_input = os.path.abspath('./'+doc_docx)
    file_output = os.path.abspath('../static/'+doc_docx+'_output.pdf')

    word_app = comtypes.client.CreateObject("Word.Application")
    word_file = word_app.Documents.Open(file_input)
    word_file.SaveAs(file_output, FileFormat=formate_code)
    word_file.Close()
    word_app.Quit()


def __init__():
    if __name__ == "__main__":
        pass

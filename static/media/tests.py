import os
import io
# def saveDocx(files, user):
#     destination = Path.joinpath(MEDIA_ROOT, user, "trash")
#     current_doc_files = list()
#     for file in files:
#         fs = FileSystemStorage(location=destination)
#         filename = fs.save(file.name, file)
#         filename = os.path.join(destination, filename)
#         current_doc_files.append(filename)
#     print("doc files---->", current_doc_files)
# return current_doc_files, destination


def convToPdf(current_doc_files):
    current_pdf_files = list()
    for root, dirs, files in os.walk(current_doc_files, topdown=False):
        for name in files:
            print(os.path.join(root,name))
            if name.endswith(".docx"):
                path = os.path.join(root,name)
                cmd = "abiword --to=pdf '{}'".format(path)
                print("CMD> ", cmd)
                try:
                    os.system(cmd)
                    pdf_file_name = os.path.splitext(name)[0] + '.pdf'
                    print("converted ", pdf_file_name)
                    current_pdf_files.append(pdf_file_name)
                except Exception as ex:
                    print("--------Exception--------")
                    print(ex)
    return current_pdf_files


print(os.getcwd())
path = os.getcwd()+"/static/media"
convToPdf(path)

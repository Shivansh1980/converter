import os
import time

def DocxToPdf(current_doc_files):
    res = {'status':None, 'url':None}

    current_doc_files = os.getcwd()+current_doc_files
    print("Converting Files In Dir : ", current_doc_files)
    path = None
    for root, dirs, files in os.walk(current_doc_files, topdown=False):
        for name in files:
            if name.endswith(".docx"):
                path = os.path.join(root,name)
                cmd = "abiword --to=pdf '{}'".format(path)
                print("Terminal> ", cmd)
                try:
                    os.system(cmd)
                    res['status'] = True
                    res['url'] = "/static/media/"+name[0:len(name)-5]+".pdf"
                    print("returning the url : " ,res['url'])
                except Exception as ex:
                    print("--------Exception--------")
                    res['status'] = False
                    res['url'] = None
    print("The dictonary is : ", res)
    return res
DocxToPdf("/static/media")
def __init__():
    if __name__ == "__main__":
        pass
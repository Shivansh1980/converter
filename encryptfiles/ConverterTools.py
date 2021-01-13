import requests
from cryptography.fernet import Fernet
import os
from converter import settings

#The Below Api is from url : https://portal.api2pdf.com/

def downloadFile(url,name="output.pdf"):
    file_url = url
    if not name.endswith(".pdf"):
        name += ".pdf"
    # URL of the image to be downloaded is defined as image_url
    r = requests.get(file_url)  # create HTTP response object

    # send a HTTP request to the server and save
    # the HTTP response in a response object called r
    with open(name, 'wb') as f:

        # Saving received content as a pdf file in
        # binary format

        # write the contents of the response (r.content)
        # to a new file in binary mode.
        f.write(r.content)

def DocxToPdf(request,current_doc_files):
    res = {'status':None,'url':None}
    url = "http://"+request.get_host()

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
                    outputpath = os.getcwd()+"/static/media/" + name[0:len(name) - 5] + ".pdf"
                    print("Output Path : ", outputpath)
                    if (not os.path.exists(outputpath)):
                        res['status'] = False
                        print("path not exists")
                        return res

                    res['url'] = url+"/static/media/"+name[0:len(name)-5]+".pdf"
                    print("returning the url : " ,res['url'])

                except Exception as ex:
                    print("--------Exception--------")
                    res['status'] = False
                    res['url'] = None
                    
    removeFiles(".docx")
    return res


def removeFiles(extension):
    for dirpath, dirnames, filenames in os.walk(settings.MEDIA_ROOT):
        for file in filenames:
            if (file.endswith(extension)):
                os.remove(os.path.join(dirpath, file))


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open("key.key", "rb").read()


def encryptFile(filepath, key):
    f = Fernet(key)
    with open(filepath, "rb") as file:
        # read all file data
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filepath, "wb") as file:
        file.write(encrypted_data)

def decryptFile(filepath, key):
    f = Fernet(key)
    with open(filepath, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filepath, "wb") as file:
        file.write(decrypted_data)

def __init__():
    if __name__ == "__main__":
        pass

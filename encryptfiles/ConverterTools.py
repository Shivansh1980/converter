from api2pdf import Api2Pdf
import requests
from cryptography.fernet import Fernet

#The Below Api is from url : https://portal.api2pdf.com/
a2p_client = Api2Pdf('d2cf4a4a-ac62-4e71-b0da-260a68c4418e	')

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

def convertToPdf(wordFileurl):
    a2p_client = Api2Pdf('d2cf4a4a-ac62-4e71-b0da-260a68c4418e	')
    api_response = a2p_client.LibreOffice.convert_from_url(
        'https://www.api2pdf.com/wp-content/themes/api2pdf/assets/samples/sample-word-doc.docx')
    print(api_response)


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open("key.key", "rb").read()


def encryptPdf(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    

def decryptFile(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)

# downloadFile("https://storage.googleapis.com/a2p-v2-storage/97005083-c8fa-44ef-8abc-a34f813ff401","file")
# write_key()
k = load_key()
#encryptPdf("file.pdf", k)
decryptFile("file.pdf",k)

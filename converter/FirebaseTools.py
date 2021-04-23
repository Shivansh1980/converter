import pyrebase

config = {
    'apiKey': "AIzaSyBwRxD6o8eC5FNDBIpW0wmawafM13pCXho",
    'authDomain': "converter-b30ab.firebaseapp.com",
    'projectId': "converter-b30ab",
    'databaseURL': "https://converter-b30ab.firebaseio.com",
    'storageBucket': "converter-b30ab.appspot.com",
    'messagingSenderId': "850133980369",
    'appId': "1:850133980369:web:531c1148c41b0db30ae1f0",
    'measurementId': "G-YQ3YVHVQYR"
}

firebase = pyrebase.initialize_app(config)
path_on_cloud = "images"
path_on_local = settings.MEDIA_ROOT

class FireBase:
    def __init__(self):
        self.__auth = firebase.auth()
        self.__storage = firebase.storage()
    
    def upload_file_to_firebase(self, local_file_path, filename):
        self.storage.child(path_on_cloud+f"/{filename}").put(local_file_path)

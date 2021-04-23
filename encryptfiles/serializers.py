from rest_framework import serializers
from encryptfiles.models import EncryptedFile

class EncryptedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncryptedFile
        fields = '__all__'
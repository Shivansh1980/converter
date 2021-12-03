from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MoodleUser
# Create your views here.

class MoodleUserApi(APIView):
    def post(self, request, slug=None, **args):

        username = request.POST.get('username')

        if not username:
            return Response(
                {
                    'status': False,
                    'error': 'username is required'
                }
            )

        if slug == "upload":
            password = request.POST.get('password')
            email = request.POST.get('email')

            if not email or not password:
                return Response({"status":False, "error":"email and password is required"})

            if not MoodleUser.objects.filter(username=username, password=password).exists():
                user = MoodleUser(username=username, password=password, email=email)
                user.save()
                return Response({"status": True, "message":"Successfuly Uploaded"})
            else:
                return Response({"status": True, "message":"User Already Exists"})

        elif slug == "get":
            try:
                user = MoodleUser.objects.get(username=username)
                return Response({"status": True, "data":{"username":user.username, "password":user.password}})
            except:
                return Response({"status":False, "error":"user doest not exists"})

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MoodleUser
# Create your views here.

class MoodleUserApi(APIView):
    def post(self, request, slug=None, **args):

        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if not username or not password or not email:
            return Response(
                {
                    'status': False,
                    'error': 'username, password or email not provided'
                }
            )

        if slug == "upload":
            if not MoodleUser.objects.filter(username=username, password=password).exists():
                user = MoodleUser(username=username, password=password, email=email)
                user.save()
                return Response({"status": True, "message":"Successfuly Uploaded"})
            else:
                return Response({"status": True, "message":"User Already Exists"})

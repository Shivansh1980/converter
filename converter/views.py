from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import smtplib
from email.message import EmailMessage


def home(request):
    print('working')
    return render(request,'homepage.html')

@csrf_exempt
def send_email(request):
    if(request.method == 'POST'):
        try:
            gmailaddress = 'shivanshshrivastava1980@gmail.com'
            gmailpassword = 'Prakash12@#'

            From = request.POST.get('from')
            user_message = request.POST.get('message')
            name = request.POST.get('name')
            user_message = f'Name: {name}\n\n'+user_message
            msg = EmailMessage()
            msg.set_content(user_message)

            msg['subject'] = 'Email From Your PortFolio'
            msg['From'] = From
            msg['To'] = 'shivanshshrivastava1980@gmail.com'

            smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
            smtp_server.starttls()
            smtp_server.login(gmailaddress, gmailpassword)
            smtp_server.send_message(msg)
            smtp_server.quit()
            return JsonResponse({'status':'success','message':'Message Sent SuccessFull', 'error':False})
        except Exception as e:
            print(e)
            return JsonResponse({'status':'error', 'error':True, 'error_msg':'unable to send'})





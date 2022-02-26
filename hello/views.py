import json
import requests
from django.shortcuts import render

from .models import Contact


# Create your views here.
# request - this is the message sent by the user to the server which holds the website.
# render - shows the html file as a response.


def index(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        r = requests.get('https://api.icndb.com/jokes/random?firstName=' + first_name + '&lastName=' + last_name)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')

        context = {'joke': joke}
        return render(request, 'hello/index.html', context)
    else:
        first_name = "Tony"
        last_name = "Stark"
        r = requests.get('https://api.icndb.com/jokes/random?firstName=' + first_name + '&lastName=' + last_name)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')

        context = {'joke': joke}
        return render(request, 'hello/index.html', context)


def portfolio(request):
    return render(request, 'hello/portfolio.html')


def contact(request):
    print(request.method)  # prints the method whether it is GET or POST

    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        mobile_no_r = request.POST.get('mobile_no')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(name=name_r, email=email_r, mobile_no=mobile_no_r, subject=subject_r, message=message_r)
        c.save()
        return render(request, 'hello/thankyou.html')

    else:
        return render(request, 'hello/contact.html')

from django.core.mail import BadHeaderError, send_mail,EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
import urllib.request
import urllib.parse
from twilio.rest import TwilioRestClient
import time
from django.shortcuts import render
from twilio.rest import Client
#from twilio_api import settings

def send_email(request):
 #   subject = request.POST.get('subject', '')
 #  message = request.POST.get('message', '')
 #   from_email = request.POST.get('harshil0410@gmail.com', '')
	if 'Railway Pass' and 'Find your Pass Attatched below' and 'cshsrailway@gmail.com':
		try:
#			send_mail('Railway Pass', 'Find your Pass Attatched below', 'cshsrailway@gmail.com', ['harshil4000@gmail.com'])
			mail = EmailMessage('Concession Pass', 'Do find the pass in the digital format below.For any further queries contact +914045967100', 'cshsrailway@gmail.com', ['harshil4000@gmail.com'])
			mail.attach_file('mailing/docs/trainpass.doc')
			mail.send()
		except BadHeaderError:
			return HttpResponse('Invalid header found.')
			return HttpResponseRedirect('http://127.0.0.1:8000/admin/')
	else:
		return HttpResponse('Make sure all fields are entered and valid.')
def expiry(request):
		send_mail('Pass Verified', 'Dear User,Your pass has been verified. You may pay at the this link : https://www.payumoney.com/paybypayumoney/#/562BE65F1F907C7319F95A3213D694BE. Best Wishes','cshsrailway@gmail.com',['harshil4000@gmail.com'])

def sms(request):
	try:
		client = Client('AC5ed807250e50cdc8e91aa1edcfa7f364', '621e87dfa7bec7fd9e5a0874e32a4ba5')
		message = client.messages.create(to='+917506402445', from_='+12052240034', body='This is to inform you that your concession form has been rejected due to non-verfification of your details.Contact +914045967100 or your college desk for further details ')
		print(message.sid)
	except BadHeaderError:
		return HttpResponseRedirect('http://127.0.0.1:8000/admin/')

'''
def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)

resp =  sendSMS('1234', '919167122577',
    'TXTLCL', 'Test Message')
print (resp)

def sendSMS():
	account_sid = "{{ AC5ed807250e50cdc8e91aa1edcfa7f364 }}"
	auth_token  = "{{ 621e87dfa7bec7fd9e5a0874e32a4ba5 }}"
	client = TwilioRestClient(account_sid, auth_token)

	message = client.messages.create(
    body="Jenny please?! I love you <3",
    to="+919167122577",
    from_="+12052240034",
    #media_url="http://www.example.com/hearts.png"
    )
	print (message.sid)'''

from django.shortcuts import render
from django.core.mail import EmailMessage , EmailMultiAlternatives
from dj_mail import settings

def Sending_Mail(request):
    if request.method == 'POST':
        data = request.POST
        
        toEmail = data.get('toEmail')
        subject = data.get('subject')
        message = data.get('message')
        ccEmail = data.get('ccEmail')
        cc_list = [email.strip() for email in ccEmail.split(',')] # converting string to list
        
        attachment = request.FILES.get('attachment')
        
        fromEmail = settings.EMAIL_HOST_USER
        to = [toEmail]  
        
        if cc_list:
            to += cc_list  
        
        email = EmailMultiAlternatives(
            from_email=fromEmail,
            to=to,
            subject=subject,
            body=message
        )
        
        if attachment:
            email.attach(attachment.name, attachment.read(), attachment.content_type)
        
        email.content_subtype = 'html'
        email.send()
  
    return render(request, 'index.html')

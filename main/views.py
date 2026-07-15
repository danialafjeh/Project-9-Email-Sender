from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def home_page(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            email_subject = "Django Project Email Sender"
            email_body = f"""New Feedback Received

            Sender Email:
            {email} 

            Message:
            {message}
            """
            send_mail(
                subject=email_subject,
                message=email_body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['dev.danialafjeh@gmail.com'],
                fail_silently=False,
            )

            return redirect("success_page")
        
    return render(request, 'mailform.html', {'form':form})

def success_page(request):
    return render(request, 'success.html')

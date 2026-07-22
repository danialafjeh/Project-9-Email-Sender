#💻 About Project

[Complete guide | Run This Project on your computer](https://github.com/danialafjeh/Run-My-Projects-Locally)

# Email Sender System

A simple Django MVT project demonstrating how to send **real emails** using Gmail SMTP and Django's built-in email framework.

The main purpose of this project is to learn and demonstrate the integration of Django with Gmail SMTP for sending emails from a web application.

---

# Project Overview

This project contains a simple **Contact Us** page where users can submit:

* Email Address
* Message

After submitting the form:

* Django validates the input.
* The backend generates a formatted email.
* Gmail SMTP is used to send the email.
* The website owner receives the email inside their Gmail inbox.

---

# Technologies

* Python
* Django
* Django Forms
* Gmail SMTP
* HTML
* CSS

---

# Project Structure

The project follows Django's **MVT (Model-View-Template)** architecture.

Since no database models are required for sending emails, this project focuses mainly on:

* Views
* Forms
* Templates
* Django Email module

---

# Features

* Contact Us page
* Django Form validation
* Real email sending using Gmail SMTP
* Success and error messages
* Clean backend implementation
* Uses Django built-in email framework
* Uses Gmail App Password authentication
* Ready to be extended for larger projects

---

# Form Fields

The Contact Us form contains:

* User Email
* User Message

---

# Backend Workflow

1. User opens the Contact page.
2. User enters email and message.
3. Django validates the submitted form.
4. Backend creates a formatted email.
5. Django connects to Gmail SMTP.
6. Email is sent to the website owner's Gmail account.
7. Success message is displayed via redirecting to a sent successfully page.
8. User is redirected back to the Contact page.

---

# Django Email Configuration

The following settings must be added to `settings.py`.

```python
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = "YOUR_GMAIL@gmail.com"

EMAIL_HOST_PASSWORD = "YOUR_GOOGLE_APP_PASSWORD"
```

---

# Gmail Configuration

Before using Gmail SMTP you must configure your Google account.

### Step 1

Enable **2-Step Verification**.

Google Account

→ Security

→ 2-Step Verification

---

### Step 2

Create an **App Password**.

Google Account

→ Security

→ App Passwords

Generate a new App Password for this project.

---

### Step 3

Copy the generated password and use it as:

```python
EMAIL_HOST_PASSWORD
```

Do **not** use your normal Gmail password.

---

# Django Form

The project uses Django Forms for validation.

Example:

```python
class ContactForm(forms.Form):

    email = forms.EmailField()

    message = forms.CharField(
        widget=forms.Textarea
    )
```

---

# Django's email sender Logic

The email sending process is implemented using Django's built-in `send_mail()` function.
Go to views.py file for viewing the full code.

Example:

```python
from django.core.mail import send_mail
from django.conf import settings

send_mail(
    subject=email_subject,
    message=email_body,
    from_email=settings.EMAIL_HOST_USER,
    recipient_list=[settings.EMAIL_HOST_USER],
    fail_silently=False,
)
```

---

# Email Format

The website owner receives emails similar to the following:

```
Subject:
Django Email Sender Project

--------------------------------

New Feedback Received

Sender Email:
user@example.com

Message:

Hello,
This is my feedback.
```

---

# Django Packages Used

No third-party email packages are required.

The project only uses Django's built-in modules:

```python
from django.core.mail import send_mail

from django.conf import settings

```

---

# Notes

The sender shown by Gmail is the configured Gmail account (`EMAIL_HOST_USER`).

The user's email is included inside the email body.

This is the standard approach used by many Contact Us forms.

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from portfolio.models import (
    Home,
    About,
    Academics,
    Experience,
    Project,
    Skill,
    Contact,
    ContactMessage
)


def home(request):
    # -----------------------------
    # Handle Contact Form Submission
    # -----------------------------
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject", "")
        message = request.POST.get("message")

        # Save message to DB
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Send email notification
        send_mail(
            subject=f"Portfolio Contact: {subject}",
            message=f"""
Name: {name}
Email: {email}

Message:
{message}
            """,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        messages.success(
            request,
            "Thank you for contacting me! I’ll get back to you soon."
        )

        return redirect("/#contact")  # redirect back to contact section

    # -----------------------------
    # Prepare context for template
    # -----------------------------
    featured_projects = Project.objects.filter(is_featured=True)

    context = {
        "home": Home.objects.first(),
        "about": About.objects.first(),
        "academics": Academics.objects.all().order_by("-year"),
        "experiences": Experience.objects.all().order_by("-id"),
        "projects": Project.objects.all(),
        "featured_projects": featured_projects,
        "skills": Skill.objects.all(),
        "contact": Contact.objects.first(),
    }

    return render(request, "portfolio/home.html", context)

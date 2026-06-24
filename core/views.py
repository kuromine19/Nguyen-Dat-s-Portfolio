from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    """Home page with hero section"""
    context = {
        'navbar': 'home',
    }
    return render(request, 'core/home.html', context)


def about(request):
    """About page"""
    context = {
        'navbar': 'about',
    }
    return render(request, 'core/about.html', context)


def dashboard(request):
    """Dashboard with skills, projects, certifications"""
    context = {
        'navbar': 'dashboard',
    }
    return render(request, 'core/dashboard.html', context)


def blog(request):
    """Blog listing page"""
    # If you have a Post model, replace with:
    # posts = Post.objects.filter(published=True).order_by('-created_at')
    context = {
        'navbar': 'blog',
        'posts': [],  # Replace with actual queryset
    }
    return render(request, 'core/blog.html', context)


def contact(request):
    """Contact page with form"""
    if request.method == 'POST':
        name    = request.POST.get('name', '').strip()
        email   = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        # TODO: save to DB or send email
        # Example: Contact.objects.create(name=name, email=email, subject=subject, message=message)
        # Or: send_mail(subject, message, email, ['your@email.com'])

        messages.success(request, 'Message sent successfully! I will get back to you soon.')
        return redirect('/contact')

    context = {
        'navbar': 'contact',
    }
    return render(request, 'core/contact.html', context)

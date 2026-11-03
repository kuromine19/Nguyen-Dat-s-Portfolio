from django.conf import settings
from django.shortcuts import render


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
    """Contact page; the form posts to Web3Forms (see WEB3FORMS_ACCESS_KEY)."""
    context = {
        'navbar': 'contact',
        'web3forms_access_key': settings.WEB3FORMS_ACCESS_KEY,
    }
    return render(request, 'core/contact.html', context)

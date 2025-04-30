from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def resume_view(request):
    return render(request, 'resume.html')

def services_view(request):
    return render(request, 'services.html')

def portfolio_view(request):
    return render(request, 'portfolio.html')

def contact_view(request):
    return render(request, 'contact.html')

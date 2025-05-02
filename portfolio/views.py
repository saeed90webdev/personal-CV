from django.shortcuts import render

def index_view(request):
    context = {
        'full_name' : 'Saeid Salehabadi',
        }
    return render(request, 'index.html', context)

def about_view(request):
    context = {
        'full_name' : 'Saeid Salehabadi',
        'Date_of_Birth' : 'February 1, 1990',
        'website' : 'www.example.com',
        'phone' : '+98 910 061 8961',
        'email' : 'saeidsalehabadi.dev@gmail.com',
        'location' : 'Mashhad, Razavi Khorasan, Iran',
        'age' : '35',
        'degree' : 'Bachelor of Nursing',
        'freelance_status' : 'Available',
        'languages' : 'Persian, English',
        }
    return render(request, 'about.html', context)

def resume_view(request):
    context = {
        'full_name' : 'Saeid Salehabadi',
        'location' : 'Mashhad, Razavi Khorasan, Iran',
        'phone' : '+98 910 061 8961',
        'email' : 'saeidsalehabadi.dev@gmail.com',
        }
    return render(request, 'resume.html', context)

def services_view(request):
    return render(request, 'services.html')

def portfolio_view(request):
    return render(request, 'portfolio.html')

def contact_view(request):
    context = {
        'location' : 'Mashhad, Razavi Khorasan, Iran',
        'phone' : '+98 910 061 8961',
        'email' : 'saeidsalehabadi.dev@gmail.com',
        }
    return render(request, 'contact.html', context)

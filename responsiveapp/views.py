from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'responsiveapp/responsive.html', context)

def people(request):
    context = {}
    return render(request, 'responsiveapp/people.html', context)

def contact(request):
    context = {}
    return render(request, 'responsiveapp/contact.html', context)
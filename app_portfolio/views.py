from django.shortcuts import render
from .models import Home, About, Experience, Projects, Skills, Education, Contacts

# Create your views here.

def page(request):
    home = Home.objects.all()
    about = About.objects.all()
    experiences = Experience.objects.all()
    project = Projects.objects.all()
    education = Education.objects.all()
    contacts = Contacts.objects.all()
    skills = Skills.objects.all()
    

    context = {
        'home': home,
        'about': about,
        'experiences': experiences,
        'project': project,
        'skills': skills,
        'education': education,
        'contacts': contacts
    }


    return render(request, 'page.html', context=context)
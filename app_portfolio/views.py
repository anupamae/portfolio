from django.shortcuts import render
from .models import Home, About, Experience, Projects, Skills, Education, Contacts

# Create your views here.
def home(request):
    homes = Home.objects.all()
    context = {
        "homes": homes
    }
    return render(request, 'app_portfolio/home.html', context) 

def about(request):
    about_data = About.objects.all()  
    context = {
        "about_data": about_data
    }
    return render(request, 'app_portfolio/about.html', context=context)

def experience(request):
    experience_data = Experience.objects.all()
    context = {
        "experience_data":experience_data
    }
    return render(request, 'app_portfolio/experience.html', context)

def skills(request):
    skills_data = Skills.objects.all()
    context = {
        "skills_data": skills_data
    }
    return render(request, 'app_portfolio/skills.html', context)

def education(request):
    education_data = Education.objects.all()
    context = {
        "education_data": education_data
    }
    return render(request, 'app_portfolio/education.html', context)

def projects(request):
    projects_data = Projects.objects.all()
    context = {
        "projects_data": projects_data
    }
    return render(request, 'app_portfolio/projects.html', context)


def contacts(request):
    contacts_data = Contacts.objects.all()
    context = {
        "contacts_data": contacts_data
    }
    return render(request, 'app_portfolio/contacts.html', context)
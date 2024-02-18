from django.shortcuts import render, HttpResponse
from .models import Home, About, Experience, Projects, Skills, Education

# Create your views here.
def home(request):
    homes = Home.objects.all()
    about_data = About.objects.all()
    experience_data = Experience.objects.all()
    skills_data = Skills.objects.all()
    projects_data = Projects.objects.all()
    education_data = Education.objects.all()
    context = {
        "homes": homes,
        "about_data": about_data,
        "experience_data": experience_data,
        "skills_data": skills_data,
        "projects_data": projects_data,
        "education_data": education_data
    }
    return render(request, 'app_portfolio/home.html', context)


def download_pdf(request):
    home_instance = Home.objects.first()
    pdf_path = home_instance.resume.path

    with open(pdf_path, 'rb') as resume:
        response = HttpResponse(resume.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="example.pdf"'
        return response

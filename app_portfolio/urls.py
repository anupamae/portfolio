from django.urls import path
from .views import home, download_pdf, about, experience, skills, education, contacts, projects
from django.conf import settings
from django.conf.urls.static import static

app_name = 'app_portfolio'

urlpatterns = [
    path('', home, name='home'),
    path('download-pdf/', download_pdf, name='download_pdf'),
    path('about/', about, name='about'),
    path('skills/', skills, name='skills'),
    path('experience/', experience, name='experience'),
    path('education/', education, name='education'),
    path('projects/', projects, name='projects'),
    path('contacts/', contacts, name='contacts')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.urls import path
from .views import home, download_pdf
from django.conf.urls.static import static

app_name = 'app_portfolio'

urlpatterns = [
    path('', home, name='home'),
    path('download-pdf/', download_pdf, name='download_pdf'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
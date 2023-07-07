from django.contrib import admin
from django.urls import path, include
from PDFPro.views import process_pdf
from django.urls import path
from PDFPro.views import hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/process_pdf/', process_pdf, name='process_pdf'),
    path('hello/', hello, name='welcome'),
]


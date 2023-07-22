from django.urls import path
from .views import home, about, resume, services, portfolio, contact

urlpatterns = [
    path("", home, name = ''),
    path("about/", about, name = 'about'),
    path("resume/", resume, name = 'resume'),
    path("services/", services, name = 'services'),
    path("portfolio/", portfolio, name = 'portfolio'),
    path("contact/", contact, name = 'contact'),
]

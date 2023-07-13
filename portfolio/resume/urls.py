from django.urls import path
from .views import home, about, resume, services, portfolio, contact

urlpatterns = [
    path("", home),
    path("about/", about),
    path("resume/", resume),
    path("services/", services),
    path("portfolio/", portfolio),
    path("contact/", contact),
]

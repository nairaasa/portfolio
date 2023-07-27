from django.urls import path
from .views import home, about, resume, services, portfolio, contact, portfolio_project

urlpatterns = [
    path("", home, name = ""),
    path("about/", about, name = "about"),
    path("resume/", resume, name = "resume"),
    path("services/", services, name = "services"),
    path("portfolio/", portfolio, name = "portfolio"),
    path("contact/", contact, name = "contact"),
    path("portfolio_project/<int:id>", portfolio_project, name = "portfolio_project"),
]

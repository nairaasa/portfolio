from django.shortcuts import render
from .models import Skill, PersonalData, Experience, Fact, Education, Service, Contact

# Create your views here.
def home(request):
    personal_data = PersonalData.objects.first()
    data1 = {
        "personal_data": personal_data
        }
    return render(request, "index.html", context=data1)



def about(request):
    skills = Skill.objects.all()
    facts = Fact.objects.all()
    data2 = {
        "skills": [skills[:3],skills[3:]],
        "facts": facts,
    }
    return render(request, "about.html", context=data2)



def resume(request):
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    data3 = {
        "experiences": experiences,
        "educations": educations
    }
    return render(request, "resume.html", context=data3)



def services(request):
    services = Service.objects.all()
    data4 = {
        "services": services
    }
    return render(request, "services.html", context=data4)



def portfolio(request):
    return render(request, "portfolio.html")



def contact(request):
    contacts = Contact.objects.first()
    data6 = {
        "contacts": contacts
    }
    return render(request, "contact.html", context=data6)
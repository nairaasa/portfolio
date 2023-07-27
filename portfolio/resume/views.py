from django.shortcuts import render, redirect
from .models import Skill, PersonalData, Experience, Fact, Education, Service, Contact, PortfolioProject
from .forms import MessageForm
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    personal_data = PersonalData.objects.get(user__username="naira_asatryan")
    data1 = {
        "personal_data": personal_data
        }
    return render(request, "index.html", context=data1)



def about(request):
    skills = Skill.objects.all()
    facts = Fact.objects.all()
    personal_data = PersonalData.objects.first()
    data2 = {
        "skills": [skills[:3],skills[3:]],
        "facts": facts,
        "personal_data": personal_data
    }
    return render(request, "about.html", context=data2)



def resume(request):
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    personal_data = PersonalData.objects.first()
    data3 = {
        "experiences": experiences,
        "educations": educations,
        "personal_data": personal_data
    }
    return render(request, "resume.html", context=data3)



def services(request):
    services = Service.objects.all()
    data4 = {
        "services": services
    }
    return render(request, "services.html", context=data4)



def portfolio(request):
    portfolio_projects = PortfolioProject.objects.all()
    data5 = {
        "portfolio_projects": portfolio_projects
    }
    return render(request, "portfolio.html", context=data5)



def contact(request):
    
    if request.method == "POST":
        print("POSTED DATA")
        print(request.POST)
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact")
        else:
            print("TELL THEM THAT SENT DATA IS NOT VALID")

    contacts = Contact.objects.first()
    personal_data = PersonalData.objects.first()
    messageForm = MessageForm()
    data6 = {
        "contacts": contacts,
        "messageForm": messageForm,
        "personal_data": personal_data
    }
    return render(request, "contact.html", context=data6)


def portfolio_project(request, id):
    project = get_object_or_404(PortfolioProject, id=id)
    return render(request, "portfolio-details.html", context={"project": project})
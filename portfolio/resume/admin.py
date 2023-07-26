from django.contrib import admin
from .models import Skill, Education, Experience, SocialMedia, Fact, Service, PersonalData, Contact, Message, PortfolioProject

class SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "value"]
    list_filter = ["value"]
    search_fields = ["name"]

class EducationAdmin(admin.ModelAdmin):
    list_display = ["university_name", "start_date", "end_date", "grade", "created_on"]

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["job_position", "start_date", "end_date", "address", "company_name"]

class PersonalDataAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "user"]
    search_fields = ["first_name", "last_name"]

class ContactAdmin(admin.ModelAdmin):
    list_display = ["email", "phone", "location"]
    search_fields = ["email", "phone", "location"]

class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "short_description"]
    search_fields = ["name", "short_description"]


# Register your models here.
admin.site.register(Skill, SkillAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(SocialMedia)
admin.site.register(Fact)
admin.site.register(Service)
admin.site.register(PersonalData, PersonalDataAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Message)
admin.site.register(PortfolioProject, PortfolioProjectAdmin)
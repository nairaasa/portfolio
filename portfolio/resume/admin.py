from django.contrib import admin
from .models import Skill, Education, Experience, SocialMedia, Fact, Testimonial, Service, PersonalData, Contact

class SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "value"]
    list_filter = ["value"]
    search_fields = ["name"]

class EducationAdmin(admin.ModelAdmin):
    list_display = ["university_name", "start_date", "end_date", "grade", "created_on"]

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["job_position", "start_date", "end_date", "address", "company_name"]



# Register your models here.
admin.site.register(Skill, SkillAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(SocialMedia)
admin.site.register(Fact)
admin.site.register(Testimonial)
admin.site.register(Service)
admin.site.register(PersonalData)
admin.site.register(Contact)
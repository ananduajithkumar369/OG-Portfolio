from django.contrib import admin
from .models import Home, Academics, Experience, Skill, About, Contact, Project, ContactMessage


class CustomAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }
# ---------------- Home ----------------
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tagline')
    search_fields = ('name',)

# ---------------- Academics ----------------
@admin.register(Academics)
class AcademicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'degree', 'institution', 'year')
    search_fields = ('degree', 'institution', 'year')

# ---------------- Experience ----------------
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'role', 'company', 'duration')
    search_fields = ('role', 'company')
    list_filter = ('company',)

# ---------------- Project ----------------
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'academic', 'experience',)
    search_fields = ('title', 'description')
    list_filter = ('academic', 'experience')

# ---------------- Skill ----------------
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)

# ---------------- About ----------------
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'content',)

# ---------------- Contact ----------------
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone', 'location')
    search_fields = ('email', 'phone', 'location')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)
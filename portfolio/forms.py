from django import forms
from .models import Academics, Experience, Project, Skill, Home, About, Contact

class AcademicsForm(forms.ModelForm):
    class Meta:
        model = Academics
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()

        degree = cleaned_data.get("degree")
        institution = cleaned_data.get("institution")
        year = cleaned_data.get("year")

        if not degree:
            self.add_error("degree", "Degree is required.")

        if not institution:
            self.add_error("institution", "Institution is required.")

        if not year:
            self.add_error("year", "Year is required.")

        return cleaned_data 


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get("role"):
            self.add_error("role", "Role is required.")

        if not cleaned_data.get("company"):
            self.add_error("company", "Company is required.")

        if not cleaned_data.get("duration"):
            self.add_error("duration", "Duration is required.")
        
        return cleaned_data

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "academic", "experience"]

    def clean(self):
        cleaned_data = super().clean()

        if not cleaned_data.get("title"):
            self.add_error("title", "Title is required.")

        if not cleaned_data.get("description"):
            self.add_error("description", "Description is required.")

        if cleaned_data.get("academic") is None:
            self.add_error("academic", "Please select an Academic record.")

        if cleaned_data.get("experience") is None:
            if not Experience.objects.filter(id=cleaned_data.get("experience")):
                self.add_error("experience", "sorry experience does not found.")
            self.add_error("experience", "Please select an Experience record.")

        return cleaned_data


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']

    def clean(self):
        cleaned_data = super().clean()

        if not cleaned_data.get("name"):
            self.add_error("name", "Skill name is required.")

        return cleaned_data    


class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()

        if not cleaned_data.get("title"):
            self.add_error("title", "Title is required.")

        if not cleaned_data.get("subtitle"):
            self.add_error("subtitle", "Subtitle is required.")

        return cleaned_data    


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'



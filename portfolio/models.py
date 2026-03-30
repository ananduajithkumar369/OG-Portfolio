from django.db import models


class Home(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='home/', blank=True, null=True)

    def __str__(self):
        return self.name


class Academics(models.Model):
    degree = models.CharField(max_length=150)
    institution = models.CharField(max_length=200)
    year = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.degree


class Experience(models.Model):
    role = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    duration = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.role} - {self.company}"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    academic = models.ForeignKey(
        Academics, on_delete=models.CASCADE, blank=True, null=True, related_name='projects'
    )
    experience = models.ForeignKey(
        Experience, on_delete=models.CASCADE, blank=True, null=True, related_name='projects'
    )

    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(
        max_length=20,
        choices=[('technical', 'Technical'), ('soft', 'Soft')],
        blank=True,    # <- allow it to be empty for now
        null=True      # <- allow NULL in the database
    )

    def __str__(self):
        return self.name



class About(models.Model):
    content = models.TextField()

    def __str__(self):
        return "About Section"


class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=150)

    def __str__(self):
        return self.email

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

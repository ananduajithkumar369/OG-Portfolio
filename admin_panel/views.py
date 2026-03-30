from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from portfolio.models import (
    Home, Academics, Experience, Project, Skill,
    About, Contact, ContactMessage
)

from portfolio.forms import (
    HomeForm, AcademicsForm, ExperienceForm,
    ProjectForm, SkillForm, AboutForm, ContactForm
)

# ---------------- DASHBOARD HOME ----------------

@login_required(login_url='/login/')
def dashboard_home(request):
    context = {
        'home': Home.objects.first(),
        'academics_count': Academics.objects.count(),
        'experience_count': Experience.objects.count(),
        'projects_count': Project.objects.count(),
        'skills_count': Skill.objects.count(),
        'about': About.objects.first(),
        'contact': Contact.objects.first(),
    }
    return render(request, 'dashboard/index.html', context)


# ---------------- HOME SECTION ----------------

@login_required(login_url='/login/')
def home_edit(request):
    home, _ = Home.objects.get_or_create(id=1)

    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES, instance=home)
        if form.is_valid():
            form.save()
            return redirect('dashboard:dashboard_home')
    else:
        form = HomeForm(instance=home)

    return render(request, 'dashboard/form.html', {
        'form': form,
        'title': 'Edit Home Section'
    })


# ---------------- ACADEMICS ----------------

@login_required(login_url='/login/')
def academics_list(request):
    academics = Academics.objects.all().order_by('-year')
    page = request.GET.get('page', 1)
    paginator = Paginator(academics, 1)  # 1 items per page

    try:
        academics_page = paginator.page(page)
    except PageNotAnInteger:
        academics_page = paginator.page(1)
    except EmptyPage:
        academics_page = paginator.page(paginator.num_pages)

    return render(request, 'dashboard/academics_list.html', {
        'academics': academics_page
    })


@login_required(login_url='/login/')
def academics_add(request):
    if request.method == "POST":
        form = AcademicsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard:academics_list")
    else:
        form = AcademicsForm()

    return render(request, "dashboard/form.html", {
        "form": form,
        "title": "Add Academic"
    })


@login_required(login_url='/login/')
def academics_edit(request, pk):
    academic = get_object_or_404(Academics, pk=pk)
    form = AcademicsForm(request.POST or None, instance=academic)

    if form.is_valid():
        form.save()
        return redirect('dashboard:academics_list')

    return render(request, 'dashboard/form.html', {
        'form': form,
        'title': 'Edit Academics'
    })


@login_required(login_url='/login/')
def academics_delete(request, pk):
    academic = get_object_or_404(Academics, pk=pk)

    if request.method == 'POST':
        academic.delete()
        return redirect('dashboard:academics_list')

    return render(request, 'dashboard/confirm_delete.html', {'object': academic})


# ---------------- EXPERIENCE ----------------

@login_required(login_url='/login/')
def experience_list(request):
    experiences = Experience.objects.all().order_by('-id')  # newest first
    page = request.GET.get('page', 1)  # get ?page= in URL

    paginator = Paginator(experiences, 1)  # show 5 items per page
    try:
        experiences_page = paginator.page(page)
    except PageNotAnInteger:
        experiences_page = paginator.page(1)
    except EmptyPage:
        experiences_page = paginator.page(paginator.num_pages)

    return render(request, 'dashboard/experience_list.html', {
        'experiences': experiences_page
    })


@login_required(login_url='/login/')
def experience_add(request):
    form = ExperienceForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dashboard:experience_list')

    return render(request, 'dashboard/form.html', {
        'form': form,
        'title': 'Add Experience'
    })


@login_required(login_url='/login/')
def experience_edit(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    form = ExperienceForm(request.POST or None, instance=experience)

    if form.is_valid():
        form.save()
        return redirect('dashboard:experience_list')

    return render(request, 'dashboard/form.html', {
        'form': form,
        'title': 'Edit Experience'
    })


@login_required(login_url='/login/')
def experience_delete(request, pk):
    experience = get_object_or_404(Experience, pk=pk)

    if request.method == 'POST':
        experience.delete()
        return redirect('dashboard:experience_list')

    return render(request, 'dashboard/confirm_delete.html', {'object': experience})


# ---------------- PROJECTS ----------------

@login_required(login_url='/login/')
def project_list(request):
    projects = Project.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(projects, 2)

    try:
        projects_page = paginator.page(page)
    except PageNotAnInteger:
        projects_page = paginator.page(1)
    except EmptyPage:
        projects_page = paginator.page(paginator.num_pages)

    return render(request, 'dashboard/project_list.html', {
        'projects': projects_page
    })


@login_required(login_url='/login/')
def project_add(request):
    form = ProjectForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dashboard:project_list')

    return render(request, 'dashboard/form.html', {
        'form': form,
        'title': 'Add Project'
    })


@login_required(login_url='/login/')
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = ProjectForm(request.POST or None, instance=project)

    if form.is_valid():
        form.save()
        return redirect('dashboard:project_list')

    return render(request, 'dashboard/form.html', {
        'form': form,
        'title': 'Edit Project'
    })


@login_required(login_url='/login/')
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('dashboard:project_list')

    return render(request, 'dashboard/confirm_delete.html', {'object': project})


# ---------------- SKILLS ----------------

@login_required(login_url='/login/')
def skill_list(request):
    skills = Skill.objects.all().order_by('name')
    page = request.GET.get('page', 1)
    paginator = Paginator(skills, 2)  # 10 skills per page

    try:
        skills_page = paginator.page(page)
    except PageNotAnInteger:
        skills_page = paginator.page(1)
    except EmptyPage:
        skills_page = paginator.page(paginator.num_pages)

    return render(request, 'dashboard/skill_list.html', {
        'skills': skills_page
    })

@login_required(login_url='/login/')
def skill_add(request):
    form = SkillForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dashboard:skill_list')

    return render(request, 'dashboard/form.html', {
        'form': form,
        'title': 'Add Skill'
    })


@login_required(login_url='/login/')
def skill_edit(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    form = SkillForm(request.POST or None, instance=skill)

    if form.is_valid():
        form.save()
        return redirect('dashboard:skill_list')

    return render(request, 'dashboard/form.html', {
        'form': form,
        'title': 'Edit Skill'
    })


@login_required(login_url='/login/')
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)

    if request.method == 'POST':
        skill.delete()
        return redirect('dashboard:skill_list')

    return render(request, 'dashboard/confirm_delete.html', {'object': skill})


# ---------------- ABOUT ----------------

@login_required(login_url='/login/')
def about_edit(request):
    about, _ = About.objects.get_or_create(id=1)

    form = AboutForm(request.POST or None, instance=about)

    if form.is_valid():
        form.save()
        return redirect('dashboard:dashboard_home')

    return render(request, 'dashboard/form.html', {
        'form': form,
        'title': 'Edit About Section'
    })


# ---------------- CONTACT ----------------

@login_required(login_url='/login/')
def contact_edit(request):
    contact, _ = Contact.objects.get_or_create(id=1)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('dashboard:dashboard_home')
    else:
        form = ContactForm(instance=contact)

    return render(request, 'dashboard/form.html', {
        'form': form,
        'title': 'Edit Contact Section'
    })


@login_required(login_url='/login/')
def contact_messages(request):
    messages = ContactMessage.objects.order_by('-created_at')
    return render(request, 'dashboard/contact_messages.html', {
        'messages': messages
    })


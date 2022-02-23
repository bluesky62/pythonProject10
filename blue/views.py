from contact.models import Contact_model
from django.shortcuts import render
from project.models import projectModel


def index(request):
    projectData = projectModel.objects.all()
    data = {
        'project_data': projectData
    }
    return render(request, "index.html", data)


def Privacy(request):
    return render(request, "privacy.html")


def Project(request):
    return render(request, "project.html")


def Terms(request):
    return render(request, "terms.html")


def About(request):
    return render(request, "about.html")


def Service(request):
    return render(request, "service.html")


def Contact(request):
    try:

        if request.method == "POST":
            name_view = request.POST.get('name')
            email_view = request.POST.get('email')
            project_view = request.POST.get('project_details')
            n = Contact_model(name=name_view, email=email_view, project_details=project_view)
            n.save()

            return render(request, "contact.html")
    except:
        pass

    return render(request, "contact.html")


def projectFuc(request):
    projectData = projectModel.objects.all()
    data = {
        'project_data': projectData
    }
    return render(request, "project delivered.html", data)



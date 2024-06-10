from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def projects(request):
    projects_show=[
        {
            'title': 'Rasoi connect',
            'path': 'images/download (3).jpeg',
        },
        {
            'title': 'Ecommerce',
            'path': 'images/download (4).jpeg',
        },
        {
            'title': 'Labour Hiring',
            'path': 'images/images.jpeg',
        },
        {
            'title': 'portfolio',
            'path': 'images/download (6).jpeg',
        }
    ]
    return render(request,"projects.html",{"projects_show": projects_show})

def experience(request):
    experience=[
        {"company":"ABC",
         "position":"python developer"},
        {"company": "ABC2",
         "position": "python developer2"},
        {"company": "ABC3",
         "position": "python developer3"}
    ]
    return render(request,"experience.html",{"experience":experience})

def certificate(request):
    return render(request,"certificate.html")

def contact(request):
    return render(request,"contact.html")


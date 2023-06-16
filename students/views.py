from django.shortcuts import render, redirect
from .models import Studentmodel


# Create your views here.
# Register

def register(request):
    if request.method == 'POST':
        sid = request.POST['s2']
        name = request.POST['n2']
        age = request.POST['a2']
        gender = request.POST['g2']
        email = request.POST['e2']
        clas = request.POST['c2']
        data = Studentmodel.objects.create(
            student_id=sid, name=name, age=age, gender=gender, email=email, classs=clas
        )
        data.save()
        redirect('/students/register/')
    return render(request, 'sindex.html')

# Display


def display(request):
    if request.method == 'GET':
        data = Studentmodel.objects.all()
    return render(request, 'sdisplay.html', {'x': data})

# Edit


def update(request, pk3):
    student = Studentmodel.objects.get(id=pk3)
    context = {
        'x': student
    }
    if request.method == 'POST':
        objj = Studentmodel.objects.get(id=pk3)
        objj.student_id = request.POST.get('s2')
        objj.name = request.POST.get('n2')
        objj.age = request.POST.get('a2')
        objj.gender = request.POST.get('g2')
        objj.email = request.POST.get('e2')
        objj.classs = request.POST.get('c2')
        objj.save()
        return redirect('/students/display/')
    return render(request, 'supdate.html', context)

# Delete


def delete(request, pk2):
    data = Studentmodel.objects.get(pk=pk2)
    data.delete()
    return display(request)

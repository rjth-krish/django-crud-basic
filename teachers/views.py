from rest_framework.views import APIView
from teachers.serializers import and_serializers
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Teachermodel


# Create your views here.
# Register


def postt(request):
    if request.method == 'POST':
        tid = request.POST['t1']
        name = request.POST['n1']
        gender = request.POST['g1']
        email = request.POST['e1']
        sub = request.POST['s1']
        data = Teachermodel.objects.create(
            teacher_id=tid, name=name, gender=gender, email=email, subject=sub
        )
        data.save()
        redirect('/teachers/register/')
    return render(request, 'index.html')

# Display


def display(request):
    if request.method == 'GET':
        data = Teachermodel.objects.all()
    return render(request, 'display.html', {'x': data})

# Edit


def update(request, pk1):
    teacher = Teachermodel.objects.get(id=pk1)
    context = {
        'x': teacher
    }
    if request.method == 'POST':
        obj = Teachermodel.objects.get(id=pk1)
        obj.teacher_id = request.POST.get('t1')
        obj.name = request.POST.get('n1')
        obj.gender = request.POST.get('g1')
        obj.email = request.POST.get('e1')
        obj.subject = request.POST.get('s1')
        obj.save()
        return redirect('/teachers/display/')
    return render(request, 'update.html', context)


# Delete


def delete(request, pk):
    data = Teachermodel.objects.get(pk=pk)
    data.delete()
    return display(request)


# API Views


class teacher_view(APIView):
    def get(self, request):
        ob = Teachermodel.objects.all()
        ser = and_serializers(ob, many=True)
        return Response(ser.data)

    def post(self, request):
        
        return HttpResponse('YES')

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from student.models import Student, StudentProfile


def index(request):
    return render_to_response('index.html', {'name': 'You'})


def user_login(request):

    if request.method == 'POST':
        try:
            student = Student.objects.get(user_number=request.POST['number'])
            request.session['number'] = student.user_number
            return redirect('dashboard')
        except:
            return HttpResponse('Some error')
    else:
        if 'number' in request.session:
            student = Student.objects.get(user_number=request.session['number'])
            return redirect('dashboard')
        context = RequestContext(request)
        return render_to_response('login.html', context)


def dashboard(request):

    return render_to_response('dashboard.html', RequestContext(request))


def update_info(request):

    return redirect('dashboard')

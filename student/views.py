# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from student.models import Student, StudentProfile, AdminUser


def index(request):
    return redirect('user_login')


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
            return redirect('dashboard')
        context = RequestContext(request)
        return render_to_response('login.html', context)


def get_student_profile(student):
    try:
        return StudentProfile.objects.get(user=student)
    except:
        return None


def get_student(request):
    try:
        if 'number' in request.session:
            return Student.objects.get(user_number=request.session['number'])
    except:
        return None


def dashboard(request):
    if 'number' in request.session:
        student = Student.objects.get(user_number=request.session['number'])
        profile = get_student_profile(student)
        context = RequestContext(request)
        context['student'] = student
        context['profile'] = profile
        return render_to_response('dashboard.html', context)
    else:
        return redirect('login')


def update_info(request):
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']
    student = get_student(request)
    profile = get_student_profile(student)
    if profile is None:
        profile = StudentProfile(user=student)
    profile.email = email
    profile.username = name
    profile.phone = phone
    profile.save()

    return redirect('dashboard')


def admin_auth(username, password):
    try:
        return AdminUser.objects.get(username=username, password=password)
    except:
        return None


def get_login_admin(request):
    if 'admin' in request.session:
        try:
            return AdminUser.objects.get(username=request.session['admin'])
        except:
            return None
    return None


def manage_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = admin_auth(username, password)
        if user is None:
            return render_to_response('manage/login.html', RequestContext(request))
        else:
            request.session['admin'] = user.username
            return redirect('student_manage')
    else:
        return render_to_response('manage/login.html', RequestContext(request))


def add_student(request):
    if request.method == 'POST':
        student = Student()
        student.user_number = request.POST['number']
        student.password = request.POST['password']
        student.save()
        profile = StudentProfile()
        profile.user = student
        profile.username = request.POST['username']
        profile.email = request.POST['email']
        profile.phone = request.POST['phone']
        profile.save()
        return redirect('student_manage')
    else:
        return render_to_response('manage/new.html', RequestContext(request))


def student_update(request):
    password = request.POST['password']
    name = request.POST['username']
    email = request.POST['email']
    phone = request.POST['phone']
    number = request.POST['number']
    student = Student.objects.get(user_number=number)
    profile = StudentProfile.objects.get(user=student)
    student.password = password
    student.save()
    profile.phone = phone
    profile.username = name
    profile.email = email
    profile.save()
    return redirect('student_manage')


def student_manage(request):
    admin_user = get_login_admin(request)
    if admin_user is None:
        return redirect('manage_login')
    context = RequestContext(request)
    context['profiles'] = StudentProfile.objects.all()
    return render_to_response('manage/manage.html', context)


def edit_profile(request):

    student = Student.objects.get(user_number=request.GET['number'])
    profile = StudentProfile.objects.get(user=student)
    context = RequestContext(request)
    context['student'] = student
    context['profile'] = profile
    return render_to_response('manage/edit.html', context)


def delete_student(request):
    student = Student.objects.get(user_number=request.GET['number'])
    profile = StudentProfile.objects.get(user=student)
    profile.delete()
    student.delete()
    return redirect('student_manage')

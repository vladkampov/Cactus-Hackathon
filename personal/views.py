from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from personal.forms import RegistrationForm, LoginForm


@csrf_exempt
def registration(request):
    if request.method == 'POST':
        if 'type' in request.POST:
            form = RegistrationForm(request.POST.type, request.POST)
            if form.is_valid():
                profile = form.save()
                login(request, profile.user)
                return HttpResponseRedirect('/stream/')
        else:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                login(request, login_form.user)
                return HttpResponseRedirect('/stream/')
            student_form = RegistrationForm("student")
            teacher_form = RegistrationForm("teacher")
    else:
        student_form = RegistrationForm("student")
        teacher_form = RegistrationForm("teacher")
        login_form = LoginForm()

    return render(request, 'registration.html', {'student_form': student_form,
                                                 'teacher_form': teacher_form,
                                                 'login_form': login_form})

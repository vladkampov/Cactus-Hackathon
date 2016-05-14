from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from personal.forms import RegistrationForm, LoginForm


@csrf_exempt
def registration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/stream/')
    if request.method == 'POST':
        if 'type' in request.POST:
            # Registration. A little bit hacky.
            form = RegistrationForm(request.POST, request.FILES)
            if form.is_valid():
                profile = form.save()
                user = authenticate(username=profile.user.username,
                                    password=request.POST['password1'])
                login(request, user)
                return HttpResponseRedirect('/stream/')
            login_form = LoginForm()
            if request.POST['type'] == "student":
                teacher_form = RegistrationForm(initial={'type': "teacher"})
                student_form = form
            else:
                student_form = RegistrationForm(initial={'type': "student"})
                teacher_form = form

            return render(request, 'registration.html', {'student_form': student_form,
                                                         'teacher_form': teacher_form,
                                                         'login_form': login_form})
        else:
            # Login
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                user = authenticate(username=login_form.user.username,
                                    password=request.POST['password'])
                login(request, user)
                return HttpResponseRedirect('/stream/')
    else:
        login_form = LoginForm()

    student_form = RegistrationForm(initial={'type': "student"})
    teacher_form = RegistrationForm(initial={'type': "teacher"})


    return render(request, 'registration.html', {'student_form': student_form,
                                                 'teacher_form': teacher_form,
                                                 'login_form': login_form})

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from personal.forms import RegistrationForm


@csrf_exempt
def registration(request, type):
    if request.method == 'POST':
        form = RegistrationForm(type, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = RegistrationForm(type)

    return render(request, 'registration.html', {'form': form})

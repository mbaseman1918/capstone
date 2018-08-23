from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from .forms import MyUser, AddressForm
from django.contrib.auth import login, authenticate

def register(request):
    if request.method == "POST":
        form = MyUser(request.POST)
        address_form = AddressForm(request.POST)
        if form.is_valid() and address_form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.clean_password2()
            new_address = address_form.save(commit=False)
            new_address.user = get_object_or_404(User, username=username)
            new_address.save()
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            return redirect('fmsapp:index')
            # return HttpResponse(f'User:{user}, Pass:{password}')
        else:
            return HttpResponse("Invalid Form")
    context = {
    'form':MyUser(),
    'addressform':AddressForm(),
    }
    return render(request, 'registration/register.html', context)

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterFrom


def index(request):
    return render(request,'app/index.html')

@login_required
def profile(request):
    return render(request,'app/profile.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"new user '{username}' created seccefully")
            return redirect('login')
    else:
        form = UserRegisterFrom()
    return render(request, 'app/register.html', {'form':form})



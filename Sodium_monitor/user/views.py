from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# from .forms import UserRegisterForm
from .forms import signForm

# Create your views here.

def sign_create_view(request):
    form1 = signForm(request.POST)
    if form1.is_valid():
        form1.save()
        return redirect('login')
    else:
        form1 = signForm()
#    context = {'form' : form}
    return render(request,"user/sign_create.html", {'form1':form1})
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You can Log In now')
            return redirect('sign')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form':form})

from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm  # We will use RegisterForm which we have created for adding an email field
                                #instead of using UserCreationForm which is default provided by Django. 


# Create your views here.

def register(request):
    if request.method == "POST":  # Corrected condition
        form = RegisterForm(request.POST)
        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Welcome {username}, you are logged in.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'Users/register.html', {'form': form})

    # This line is added to handle fallback for invalid form submission.
    return HttpResponse("Invalid form submission")

    """This HttpResponse is added above to handle this error
    raise ValueError( ValueError: The view Users.views.register didn't return an HttpResponse object. 
    It returned None instead.
    """

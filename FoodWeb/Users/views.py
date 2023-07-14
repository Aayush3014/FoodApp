from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == "POST":  # Corrected condition
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account is created.')
            return redirect('Food:index')
    else:
        form = UserCreationForm()
    return render(request, 'Users/register.html', {'form': form})

    return HttpResponse("Invalid form submission")   # This line is added to handle fallback for invalid form submission.

    """This HttpResponse is added above to handle this error
    raise ValueError( ValueError: The view Users.views.register didn't return an HttpResponse object. 
    It returned None instead.
    """
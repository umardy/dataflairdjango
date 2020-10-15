from django.shortcuts import render
from . import forms

#DataFlair #Form #View Functions
def regform(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        html = 'We have received this form again'
    else:
        html = 'Welcome for first time'
    return render(request, 'registration/signup.html', {'html': html, 'form': form})
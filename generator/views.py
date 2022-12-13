from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html',{'password':'abadpass'})

def password(request):
    #Random characters to choose from
    characterset = list('abcdf')
    created_pass = ''
    #Here we use the dictionary that was passed in and search for 'pass_len' using default if not found
    pl_str = request.GET.get('pass_len',8)
    #The returned value is a STRING, and we are going to convert that to an int
    pass_len = int(pl_str)
    if request.GET.get('uppercase'):
        characterset.extend(list('VWXYZ'))
    if request.GET.get('special'):
        characterset.extend(list('!@#$%'))
    if request.GET.get('numbers'):
        characterset.extend(list('0123456789'))
    #Loop and add a character each time
    for x in range(pass_len):
        created_pass += random.choice(characterset)

    return render(request,'generator/password.html',{'password':created_pass})
def about(request):
    return render(request,'generator/about.html')

from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    return render(request, "index.html")

def processMoney(request):
    #print("inside")
    if request.method == "POST":
        type = request.POST.get('type')
        #print(type)
        if type == 'farm':
            request.session['gold'] += random.randint(10, 20)
        elif type == 'cave':
            request.session['gold'] += random.randint(5, 10)
        elif type == 'home':
            request.session['gold'] += random.randint(2, 5)
        elif type == 'casino':
            request.session['gold'] += random.randint(-50, 50)
    return redirect("/")

from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'log' not in request.session:
        request.session['log'] = []
    return render(request, "index.html")

def processMoney(request):
    #print("inside")
    if request.method == "POST":
        #print(type(request.session['gold']))
        #print(type(request.session['log']))
        bldType = request.POST.get('type')
        #print(type)
        if bldType == 'farm':
            coins = random.randint(10, 20)
            request.session['gold'] += coins
            request.session['log'].insert(0, f"You just farmed for {coins} coins. 🌿")
            #print(request.session['log'])
        elif bldType == 'cave':
            coins = random.randint(5, 10)
            request.session['gold'] += coins
            request.session['log'].insert(0, f"You just found {coins} coins in the cave. 🗻")
        elif bldType == 'home':
            coins = random.randint(2, 5)
            request.session['gold'] += coins
            request.session['log'].insert(0, f"You just found {coins} coins in your house. 🏠")
        elif bldType == 'casino':
            coins = random.randint(-50, 50)
            request.session['gold'] += coins
            if coins >= 0:
                request.session['log'].insert(0, f"You just won {coins} coins at the casino. 🎲")
            else:
                request.session['log'].insert(0, f"You just lost {coins} coins at the casino. 🎲")
    return redirect("/")

def reset(request):
    request.session['gold'] = 0
    request.session['log'] = []
    return redirect('/')
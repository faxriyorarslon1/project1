from django.shortcuts import render
from .models import Talaba
from .forms import DavomatForm

# Create your views here.

def index(request):
    form = DavomatForm()
    talabalar = Talaba.objects.all()

    malumot = {
        'talabalar':talabalar,
        "form":form
    }
    return render(request, 'main.html', context=malumot)


from django.shortcuts import render
from .models import Chair

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):

    thmub_nails=[]
    chairs=Chair.objects.all()
    for chair in chairs:
        thmub_nails.append(chair.chairimages_set.first())

    context={'chairs':chairs,'thumb_nails':thmub_nails}
    return render(request,'index.html',context)

def details(request, id):
    chair=Chair.objects.get(pk=id)
    images=chair.chairimages_set.all()
    context={'chair':chair,'images':images}
    return render(request,'detail.html',context)

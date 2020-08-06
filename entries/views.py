from django.shortcuts import render,redirect
from .models import Entry
from django.contrib.auth.models import User

# Create your views here.  
def home(request):
    log_user=request.user
    entries = Entry.objects.filter(user=log_user).order_by('-date_posted')  
    return render(request,'home.html',{'m':entries})
  #  entries = Entry.objects.order_by('-date_posted')
   # context = {'entries' : entries}
    #return render(request,'home.html',context)

def add(request):
    if request.method == 'POST':
        data=request.POST['data']
        new=Entry(text=data, user=request.user)
        new.save()
        log_user=request.user
        entries = Entry.objects.filter(user=log_user).order_by('-date_posted')
        return render(request,'home.html',{'m':entries})
        
        #if form.is_valid():
         #   form.save()
          #  return redirect('/')   
    else:
        return render(request,'add.html')
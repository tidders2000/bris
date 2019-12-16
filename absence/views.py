from django.shortcuts import render, get_object_or_404, redirect
from .models import Absence, Reason
from .forms import absence_form
# Create your views here.

def absence(request):
    
    form=absence_form()
    if request.method=='POST':
        
        af=absence_form(request.POST)
        if af.is_valid():
            af.save(commit=True)
            
            
            return render(request,'absence.html',{'form':form})
       
    return render(request,'absence.html',{'form':form})

def absence_edit(request,id):
   
    abs = get_object_or_404(Absence, id=id)
    form = absence_form(instance=abs)
    if request.method=='POST':
       
        af=absence_form(request.POST,instance=abs)
        if af.is_valid():
            if af.is_valid():
             af.save(commit=True)
             return redirect('index.html',{'form':form})
    else:   
     
     return render(request, 'absence.html', {'form': form})
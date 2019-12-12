from django.shortcuts import render
from django.views.generic import CreateView
from .form import PostForm
from django.http import HttpResponse
import subprocess

class FormCreateView(CreateView):
    model = PostForm
    fields = ('arg1', 'arg2')

def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # p1 = form.cleaned_data["p1"]
            # p2 = form.cleaned_data["p2"]
            # x = form.cleaned_data["x"]
            # y = form.cleaned_data["y"]
            # z = form.cleaned_data["z"]
            # if p2:
            #     command = f'screen -S mcpe -X stuff \'tp {p1} {p2}\\n\''
            # else:
            #     command = f'screen -S mcpe -X stuff \'tp {p1} {x} {y} {z}\\n\''
            
            arg1=form.cleaned_data["arg1"]
            arg2=form.cleaned_data["arg2"]
            command = f'screen -S mcpe -X stuff \'tp {arg1} {arg2}\\n\''
            _ = subprocess.call(command,shell = True)
    form = PostForm()
    return render(request,'form.html',{'form':form})         

    # return HttpResponse(script.players)
from django.shortcuts import render, redirect
from aplicativo.forms import AlunosForm
from aplicativo.models import Alunos

# Create your views here.
def home(request):
    data = {}
    data['db'] = Alunos.objects.all()
    return render(request, 'index.html', data)
 
def forms(request):
    data = {}
    data['form'] = AlunosForm()
    return render(request, 'forms.html', data)

def create(request):
    form = AlunosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(home)
    
def view(request, pk):
    data = {}
    data['db'] = Alunos.objects.get(pk=pk)   
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Alunos.objects.get(pk=pk)   
    data['form'] = AlunosForm(instance=data['db'])
    return render(request, 'forms.html', data)

def update(request, pk):
    data = {}
    data ['db'] = Alunos.objects.get(pk=pk)
    form = AlunosForm(request.POST or None, instance= data['db'])
    if form.is_valid():
        form.save()
        return redirect(home)
    
def delete(request, pk):
    db = Alunos.objects.get(pk=pk)
    db.delete()
    return redirect(home)

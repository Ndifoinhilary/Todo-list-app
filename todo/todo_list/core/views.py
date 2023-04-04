from django.http import HttpResponse
from django.shortcuts import redirect, render
from core.forms import TodoForm
from django.db.models import Q
from core.models import Todo

# Create your views here.


def home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        # posts = Todo.objects.filter(title__icontains = q)
        some = Q(Q(title__icontains = q)|Q(description__icontains = q) )
        posts = Todo.objects.filter(some)
    else:
        posts = Todo.objects.all()
    context = {
        'posts':posts
    }
    
    return render(request , 'home.html',context )



def upload(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm()
        return render(request , 'form-de.html', {'form':form})
    


def update(request , pk):
    pk = int(pk)
    try:
        updated = Todo.objects.get(pk = pk)
    
    except Todo.DoesNotExist:
        return redirect('home')
    form = TodoForm(request.POST or None, instance= updated)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request , 'form-de.html', {'form':form})


def deletel(request,pk):
    pk = int(pk)
    try:
        dele = Todo.objects.get(pk = pk)
    except Todo.DoesNotExist:
        return redirect('home')
    dele.delete()
    return redirect('home')



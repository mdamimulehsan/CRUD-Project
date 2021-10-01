from django.shortcuts import render, redirect
from .models import Cricketers


# Create your views here.
def home(request):
    cricketer = Cricketers.objects.all()
    print(cricketer)
    if len(cricketer) == 0:
        return render(request, template_name='list.html', context={'message': 'h'})
    else:
        cricketers_list = []
        for x in cricketer:
            temp = {
                'id': x.id,
                'name': x.name,
                'role': x.role,
            }
            cricketers_list.append(temp)
        return render(request, template_name='list.html', context={'message': 'c', 'cricketers': cricketers_list})


def update(request, id):
    crickter = Cricketers.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['Fullname']
        role = request.POST['PlayingRole']
        crickter.name = name
        crickter.role = role
        crickter.save()
        return redirect('app:home')
    else:
        data = {
            'id': id,
            'name': crickter.name,
            'role': crickter.role,
        }
        return render(request, template_name='update.html', context=data)


def delete(request, id):
    cricketer = Cricketers.objects.get(id=id)
    cricketer.delete()
    return redirect('app:home')


def create(request):
    if request.method == "POST":
        name = request.POST['Fullname']
        role = request.POST['PlayingRole']
        users = Cricketers.objects.create(name=name, role=role)
        users.save()
        return redirect('app:home')
    else:
        return render(request, template_name='signup.html')

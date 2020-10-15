from django.shortcuts import render, redirect
from .models import Pet, Like

def landing_page(request):
    return render(request, 'landing_page.html')

def original(request):
    pass

def pet_list(request):
    pets = Pet.objects.all()
    context = {
        'pets': pets,
    }
    return render(request, 'partials/pet_list.html', context)

def pet_detail(request, id):
    pet = Pet.objects.get(pk=id)
    like = Pet.objects.filter(like__pet=id).count()
    context = {
        'pet': pet,
        'like': like,
    }
    return render(request, 'partials/pet_detail.html', context)

def pet_like(request, id):
    pet = Pet.objects.get(id=id)
    like = Like(pet=pet)
    like.save()
    return redirect('petstagram:pet_detail', id)

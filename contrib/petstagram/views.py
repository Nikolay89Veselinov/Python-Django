from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Pet, Like, Comment
from .forms import CommenForm, PetForm
from contrib.accounts.decorators import user_required


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

@login_required
def pet_detail(request, id):
    pet = Pet.objects.get(pk=id)
    like = Pet.objects.filter(like__pet=id).count()
    if request.method == 'GET':
        context = {
            'pet': pet,
            'like': like,
            'form': CommenForm(),
            'can_delete': request.user == pet.user,
            'can_edit': request.user == pet.user,
            'can_like': request.user != pet.user,
            'has_liked': pet.like_set.filter(user_id=request.user.id).exists(),
            'can_comment': request.user != pet.user,

        }
        return render(request, 'partials/pet_detail.html', context)
    else:
        form = CommenForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'])
            comment.pet = pet
            comment.user = request.user
            comment.save()
            return redirect('petstagram:pet_detail', id)
        context = {
            'pet': pet,
            'like': like,
            'form': form,
        }
        return render(request, 'partials/pet_detail.html', context)
@login_required
def pet_like(request, id):
    like = Like.objects.filter(user_id=request.user.id, pet_id=id).first()
    if like:
        like.delete()
    else:
        pet = Pet.objects.get(id=id)
        like = Like(pet=pet, user=request.user)
        like.save()
    return redirect('petstagram:pet_detail', id)

@login_required
def pet_delete(request, id):
    pet = Pet.objects.get(pk=id)

    if request.method == 'GET':
        context = {
            'pet': pet,
        }
        return render(request, 'partials/pet_delete.html', context)
    else:
        pet.delete()
        return redirect('petstagram:pet_list')

@user_required(Pet)
def pet_edit(request, id):
    pet = Pet.objects.get(pk=id)
    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
        return redirect('petstagram:pet_detail', pet.id)

    else:
        form = PetForm(instance=pet)
    context = {
        'form': form,
        'pet': pet,
    }
    return render(request, 'partials/pet_edit.html', context)

@login_required
def pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('petstagram:pet_list')
    else:
        form = PetForm()
    
    context = {
        'form': form,
    }

    return render(request, 'partials/pet_create.html', context)

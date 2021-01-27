from contrib.petstagram.core.clead_up import clean_up_files
from django.contrib.auth import mixins as auth_mixins, views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views import generic as views
from .models import Pet, Like, Comment
from .forms import CommenForm, PetForm, CommenViewsForm
from contrib.accounts.decorators import user_required


def landing_page(request):
    return render(request, 'landing_page.html')

class LandingPageViews(TemplateView):
    template_name = 'landing_page.html'

def original(request):
    pass

def pet_list(request):
    pets = Pet.objects.all()
    context = {
        'pets': pets,
    }
    return render(request, 'partials/pet_list.html', context)


class PetsListViews(ListView):
    model = Pet
    template_name = 'partials/pet_list.html'
    context_object_name = 'pets'

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

class PetDedailsView(views.DetailView):
    model = Pet
    template_name = 'partials/pet_detail.html'
    context_object_name = 'pet'

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # import ipdb; ipdb.set_trace()
        pet = self.get_object()
        like = Pet.objects.filter(like__pet=pet.id).count()
        context['form'] = CommenForm()
        context['like'] = like
        context['can_delete'] = self.request.user == pet.user
        context['can_edit'] = self.request.user == pet.user
        context['can_like'] = self.request.user != pet.user
        context['has_liked'] = pet.like_set.filter(user_id=self.request.user.id).exists()
        context['can_comment'] = self.request.user != pet.user
        return context


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


class PetLikeViews(views.View):
    def get(self, request, *args, **kwargs):
        # import ipdb; ipdb.set_trace()
        pet = Pet.objects.get(pk=self.kwargs['pk'])
        like = Like.objects.filter(user_id=request.user.id, pet_id=self.kwargs['pk']).first()
        if like:
            like.delete()
        else:
            like = Like(pet=pet, user=request.user)
            like.save()        
        return redirect('petstagram:pet_detail', pet.id)

class PetCommentViews(auth_mixins.LoginRequiredMixin, views.FormView):
    form_class = CommenViewsForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.pet = Pet.objects.get(pk=self.kwargs['pk'])
        comment.save()
        return redirect('petstagram:pet_detail', self.kwargs['pk'])

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

class PetDeleteViews(DeleteView):
    model = Pet
    template_name = 'partials/pet_delete.html'
    success_url = reverse_lazy('petstagram:pet_list')

    def dispatch(self, request, *args, **kwargs):
        pet = self.get_object()
        if pet.user_id != request.user.id:
            handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

@user_required(Pet)
def pet_edit(request, id):
    pet = Pet.objects.get(pk=id)
    if request.method == 'POST':
        old_image = pet.image_url
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            if old_image:
                clean_up_files(old_image.path)
            form.save()
        return redirect('petstagram:pet_detail', pet.id)

    else:
        form = PetForm(instance=pet)
    context = {
        'form': form,
        'pet': pet,
    }
    return render(request, 'partials/pet_edit.html', context)

class EditPetViews(auth_mixins.LoginRequiredMixin, UpdateView):
    template_name = 'partials/pet_edit.html'
    model = Pet
    form_class = PetForm

    def get_absolute_url(self):
        success_url = reverse_lazy('petstagram:pet_detail', kwargs={'pk': self.object.id})
        return success_url

    def form_valid(self, form):
        old_image = self.get_object().image_url
        if old_image:
            clean_up_files(old_image.path)
        return super().form_valid(form)

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


class CreatePetViews(auth_mixins.LoginRequiredMixin, CreateView):
    template_name = 'partials/pet_create.html'
    model = Pet
    form_class = PetForm

    def get_absolute_url(self):
        success_url = reverse_lazy('petstagram:pet_detail', kwargs={'id': self.object.id})
        return success_url

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.user = self.request.user
        pet.save()
        return super().form_valid(form)
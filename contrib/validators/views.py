from django.shortcuts import render

from .forms import ValidatorModelForm

def validator(request):
    if request.method == 'POST':
        form = ValidatorModelForm(request.POST)
        if form.is_valid:
            form.save()
            return render(request, 'success.html')
    else:
        form = ValidatorModelForm()
    return render(request, 'validator_form.html', {'form': form})



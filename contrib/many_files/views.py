from django.shortcuts import render

from .models import File, FileCollection, Image
from.forms import FileCollectionForm


def files(request):
    files = File.objects.all()
    images = Image.objects.all()
    if request.method == 'POST':
        form = FileCollectionForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            # for file in form.files.getlist('upload_file'):
            #     File.objects.create(
            #         file=file,
            #         collection=instance
            #     )
            return render(request, 'success.html')
    else:
        form = FileCollectionForm()

    context = {
        'files': files,
        'form': form,
        'images': images
    }
    return render(request, 'file.html', context)

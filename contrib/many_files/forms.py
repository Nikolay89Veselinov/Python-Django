from django import forms
from .models import FileCollection, File



class FileCollectionForm(forms.ModelForm):

    upload_file = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = FileCollection
        fields = ('upload_file', )
        
    def save(self, commit=True):
        instance = super(FileCollectionForm, self).save(commit=commit)
        for file in self.files.getlist('upload_file'):
            File.objects.create(
                file=file,
                collection=instance
            )
        if commit:
            instance.save()
        return instance

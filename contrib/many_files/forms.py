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

    def clean(self):
        """
        Checks the format of each of the attached files.
        """
        allowed_formats = ('doc', 'docx', 'pdf', 'jpg', 'png')
        format_error = 'Прикачи файл във формат {}'.format(', '.join(allowed_formats))
        for field, value in self.files.items():
            extension = value.name.split('.')[-1]
            if extension not in allowed_formats:
                self.add_error(field, forms.ValidationError(format_error))

    # def clean(self):
    #     cleaned_data = super().clean()
    #     file = cleaned_data.get('file')
    #     import ipdb; ipdb.set_trace()

    #     allowed_formats = ('.doc', '.docx', '.pdf', '.jpg')
    #     for _, x in self.files.items():
    #         if x.name.split('.')[-1] in allowed_formats:
    #             print('yes')
    #         else:
    #             print('no')
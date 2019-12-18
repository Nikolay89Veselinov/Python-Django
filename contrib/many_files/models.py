from django.db import models
from .managers import MyManager

class FileCollection(models.Model):
    pass

    def __str__(self):
        return 'File collections {}'.format(self.pk)

class File(models.Model):
    file = models.FileField(upload_to='files')
    collection = models.ForeignKey(FileCollection, on_delete=models.CASCADE, related_name='files')

    def __str__(self):
        return '{}'.format(self.file)


class Form(models.Model):
    name = models.CharField(max_length=255,)
    upload_file = models.FileField(upload_to='photo', )

    objects = MyManager()

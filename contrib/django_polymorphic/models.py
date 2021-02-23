import pdfkit
from django.db import models
from django.urls import reverse
from django.template.loader import render_to_string

from polymorphic.models import PolymorphicModel


def render_pdf(template, context):
    html = render_to_string(template, context)
    return pdfkit.from_string(html, False)


class Animals(PolymorphicModel):
    breed = models.CharField(max_length=30)

    def __str__(self):
        return self.breed

    def get_admin_url(self):
        animals_class = self.get_real_instance_class()
        animals = self.get_real_instance()
        return reverse('admin:%s_%s_change' % (animals_class._meta.app_label,  animals_class._meta.model_name),  args=[animals.pk])

    @property
    def results_pdf_template(self):
        return 'animals_pdf.html'

    def render_results_pdf(self, template=None):
        if template is None:
            template = self.results_pdf_template
        try:
            return render_pdf(template, {'animal': self})
        except Exception:
            return None


class Cat(Animals):
    name = models.CharField(max_length=30)
    abilities = models.CharField(max_length=255)
    age = models.IntegerField(default=0)

    def __str__(self):
        return  self.__class__.__name__
        
    @property
    def results_pdf_template(self):
        return 'animals_pdf.html'

class Dog(Animals):
    name = models.CharField(max_length=30)
    abilities = models.CharField(max_length=255)
    age = models.IntegerField(default=0)

    def __str__(self):
        return  self.__class__.__name__
        
    @property
    def results_pdf_template(self):
        return 'animals_pdf.html'

class Bird(Animals):
    name = models.CharField(max_length=30)
    abilities = models.CharField(max_length=255)
    age = models.IntegerField(default=0)

    def __str__(self):
        return  self.__class__.__name__
        
    @property
    def results_pdf_template(self):
        return 'animals_pdf.html'

class Fish(Animals):
    name = models.CharField(max_length=30)
    abilities = models.CharField(max_length=255)
    age = models.IntegerField(default=0)

    def __str__(self):
        return  self.__class__.__name__
        
    @property
    def results_pdf_template(self):
        return 'animals_pdf.html'

class Bear(Animals):
    name = models.CharField(max_length=30)
    abilities = models.CharField(max_length=255)
    age = models.IntegerField(default=0)

    def __str__(self):
        return  self.__class__.__name__
        
    @property
    def results_pdf_template(self):
        return 'animals_pdf.html'

class ImageAnimals(models.Model):
    img = models.ImageField(upload_to='images')
    animal = models.ForeignKey(
        'Animals',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return  self.__class__.__name__
        
    @property
    def results_pdf_template(self):
        return 'animals_pdf.html'
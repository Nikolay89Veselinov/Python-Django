import pdfkit
import uuid
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User

from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


def render_pdf(template, context):
    html = render_to_string(template, context)
    return pdfkit.from_string(html, False)


class Pet(models.Model):

    DOG = 'Dog'
    CAT = 'Cat'
    PARROT = 'Parrot'
    UNKNOWN = 'Unknown'

    PET_TYPES_CHOICES = (
        (DOG, 'Dog'),
        (CAT, 'Cat'),
        (PARROT, 'Parrot'),
        (UNKNOWN, 'Unknown'),
    )
    slug = models.SlugField()
    # slug = models.SlugField(editable=False)
    type = models.CharField(max_length=6, choices=PET_TYPES_CHOICES, default=UNKNOWN)
    name = models.CharField(max_length=6)
    age = models.IntegerField(default=0)
    description = models.TextField()
    image_url = models.ImageField(upload_to='images/pets')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('petstagram:pet_detail', kwargs={'pk': self.id})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    # def get_admin_url(obj):
    #     return reverse('admin:%s_%s_change' % (obj._meta.app_label,  obj._meta.model_name),  args=[obj.id] )

    def get_admin_url(obj):
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label,  obj._meta.model_name),  args=[obj.id])
        return mark_safe('<a href="%spdf">Download pdf</a>' % (url))

    @property
    def results_pdf_template(self):
        return 'pet_pdf.html'

    def results_pdf(self, template=None):
        if template is None:
            template = self.results_pdf_template
        return render_pdf(template, {'pet': self})
        # return pdfkit.from_string(render_to_string(template, {'pet': self}), False)

class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('petstagram:pet_like', kwargs={'pk': self.id})


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

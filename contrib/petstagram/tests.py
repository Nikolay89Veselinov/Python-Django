from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User

from .models import Pet

class PetModelTests(TestCase):

    def create_test_image(self):
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        return SimpleUploadedFile(
            'small.gif',
            small_gif,
            content_type='image/gif'
        )
    # Call test: ./manage.py test contrib.petstagram.tests.PetModelTests.create_pet
    def create_pet(self):
        User(username='qwe').save() 
        user = User.objects.all()[0]
        Pet.objects.create(
            slug="lion",
            type="Dog",
            name="lion",
            age=15,
            description="lion",
            image_url=self.create_test_image(),
            user=user,
            )

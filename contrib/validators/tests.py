from django.urls.base import reverse
from .models import ValidatorModel
from .forms import ValidatorModelForm
from django.test import TestCase
from selenium import webdriver
from tastypie.test import ResourceTestCase


class EntryResourceTest(ResourceTestCase):
    
    def test_get_api_json(self):
        resp = self.api_client.get('/api/whatever/', format='json')
        self.assertValidJSONResponse(resp)

    def test_get_api_xml(self):
        resp = self.api_client.get('/api/whatever/', format='xml')
        self.assertValidXMLResponse(resp)


class ValidatorsTests(TestCase):
    def create_validators(self):
        return ValidatorModel.objects.create(
            even_field="123",
            phone='0896343439',
            name='stana',
            description="qeweqwwqeeqweqwewqeqwewq",
            egn='8905236341',
            email='qweqweqwe@abv.bg',
            active=True,
            url='google.bg',
            password='123123123',
            confirm_password='123123123'
            )


    def test_validators(self):
        w = self.create_validators()
        self.assertTrue(isinstance(w, ValidatorModel))
        self.assertEqual(len(w.name), 5)


    def test_view_validators(self):
        validators = self.create_validators()
        url = reverse("validators")
        resp = self.client.get(url)
        # import ipdb; ipdb.set_trace()
        self.assertEqual(resp.status_code, 200)
        # self.assertIn(validators.confirm_password, resp.content)




    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_signup_fire(self):
        driver = self.driver

        driver.get("http://localhost:8000/validators/")
        driver.find_element_by_id('name').send_keys("Nikolay")
        driver.find_element_by_id('c_phone').send_keys("0897454647")
        driver.find_element_by_id('c_password').send_keys("123123123")
        driver.find_element_by_id('c_confirm_password').send_keys("123123123")
        driver.find_element_by_id('c_description').send_keys("adsdasads adsdassad adssadads")
        driver.find_element_by_id('c_egn').send_keys("8905236341")
        driver.find_element_by_id('c_email').send_keys("tests@abv.bg")
        driver.find_element_by_id('c_url').send_keys("www.google.com")
        driver.find_element_by_id('submit').click()
        self.assertIn("http://localhost:8000/", self.driver.current_url)

    def tearDown(self):
        self.driver.quit


    def test_valid_form(self):
        w = ValidatorModel.objects.create(
            even_field="123",
            phone='0896343439',
            name='stana',
            description="qeweqwwqeeqweqwewqeqwewq",
            egn='8905236341',
            email='qweqweqwe@abv.bg',
            active=True,
            url='google.bg',
            password='123123123',
            confirm_password='123123123'
            )
        data = {
            'even_field': w.even_field,
            'phone': w.phone,
            'name': w.name,
            'description': w.description,
            'egn': w.egn,
            'email': w.email,
            'active': w.active,
            'url': w.url,
            'password': w.password,
            'confirm_password': w.confirm_password,
        }
        form = ValidatorModelForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        w = ValidatorModel.objects.create(
            even_field="123",
            phone='0896343439',
            name='stana',
            description="qeweqwwqeeqweqwewqeqwewq",
            egn='8905236341',
            email='qweqweqwe@abv.bg',
            active=True,
            url='google.bg',
            password='123123123',
            confirm_password='123123123'
            )
        data = {
            'even_field': w.even_field,
            'phone': '098978787878',
            'name': w.name,
            'description': w.description,
            'egn': w.egn,
            'email': w.email,
            'active': w.active,
            'url': w.url,
            'password': w.password,
            'confirm_password': w.confirm_password,
        }
        form = ValidatorModelForm(data=data)
        self.assertFalse(form.is_valid())
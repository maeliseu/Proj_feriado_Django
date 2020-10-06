from django.test import TestCase


class NatalTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'Natal')

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'natal.html')

class Natal2Test(TestCase):    
    def setUp(self):
        self.resp = self.client.get('/natal')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'Natal')

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'natal.html')


class CarnavalTest(TestCase):    
    def setUp(self):
        self.resp = self.client.get('/carnaval')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'Carnaval')

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'carnaval.html')


class TiradentesTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/tiradentes')
        
    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'Tiradentes')

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'tiradentes.html')
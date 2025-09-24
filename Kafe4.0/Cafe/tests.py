from django.test import TestCase

class ModelNameTestCase(TestCase):
    def test_model_str(self):
        model = ModelName.objects.create(name="Test Model", description="Test Description")
        self.assertEqual(str(model), "Test Model")
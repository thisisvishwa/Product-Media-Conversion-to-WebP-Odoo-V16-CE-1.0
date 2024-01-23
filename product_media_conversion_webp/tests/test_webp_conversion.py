from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError

class TestWebPConversion(TransactionCase):

    def setUp(self):
        super(TestWebPConversion, self).setUp()
        self.ProductTemplate = self.env['product.template']
        self.WebPSettings = self.env['webp.settings']
        self.ErrorLog = self.env['error.log']

    def test_image_conversion_to_webp(self):
        # Create a dummy product template with a test image
        product_template = self.ProductTemplate.create({
            'name': 'Test Product',
            'image_1920': b'base64_test_image_data'
        })

        # Simulate image conversion to WebP
        product_template.convert_to_webp()

        # Check if the image field has been updated to WebP format
        self.assertTrue(product_template.image_1920_webp, "Image was not converted to WebP format.")

    def test_webp_settings_access(self):
        # Access WebP settings
        webp_settings = self.WebPSettings.search([], limit=1)
        self.assertTrue(webp_settings, "WebP settings could not be accessed.")

    def test_error_logging(self):
        # Simulate an error during image conversion
        try:
            self.ProductTemplate.create({
                'name': 'Test Product with Error',
                'image_1920': b'invalid_image_data'
            }).convert_to_webp()
        except UserError:
            pass

        # Check if the error has been logged
        error_logs = self.ErrorLog.search([])
        self.assertTrue(error_logs, "Error during image conversion was not logged.")

    def test_webp_conversion_button(self):
        # Simulate clicking the WebP conversion button
        product_template = self.ProductTemplate.create({
            'name': 'Test Product for Button',
            'image_1920': b'base64_test_image_data'
        })
        product_template.with_context({'active_id': product_template.id}).convert_to_webp()

        # Check if the image field has been updated to WebP format
        self.assertTrue(product_template.image_1920_webp, "Image was not converted to WebP format after button click.")
from odoo import models, fields, api
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    webp_image = fields.Binary("WebP Image", attachment=True)
    webp_conversion_status = fields.Selection([
        ('pending', 'Pending'),
        ('done', 'Done'),
        ('failed', 'Failed')
    ], string='WebP Conversion Status', default='pending', readonly=True)

    @api.model
    def create(self, vals):
        record = super(ProductTemplate, self).create(vals)
        if 'image_1920' in vals:
            record._convert_to_webp()
        return record

    def write(self, vals):
        res = super(ProductTemplate, self).write(vals)
        if 'image_1920' in vals:
            self._convert_to_webp()
        return res

    def _convert_to_webp(self):
        for record in self:
            try:
                # Placeholder for the actual image conversion logic
                # This should be replaced with the logic to convert the image to WebP format
                # and assign it to the webp_image field.
                record.webp_image = record.image_1920
                record.webp_conversion_status = 'done'
            except Exception as e:
                _logger.error("WebP conversion failed: %s", e)
                record.webp_conversion_status = 'failed'
                self.env['product_media_conversion_webp.error_log'].create({
                    'product_template_id': record.id,
                    'error_message': str(e)
                })

    @api.model
    def get_webp_settings(self):
        # Placeholder for getting WebP settings
        # This should be replaced with the logic to retrieve the settings from the database
        return {}

    @api.model
    def set_webp_settings(self, settings):
        # Placeholder for setting WebP settings
        # This should be replaced with the logic to save the settings to the database
        pass

class ErrorLog(models.Model):
    _name = 'product_media_conversion_webp.error_log'
    _description = 'Error Log for WebP Conversion'

    product_template_id = fields.Many2one('product.template', string='Product Template', required=True)
    error_message = fields.Text('Error Message', required=True)
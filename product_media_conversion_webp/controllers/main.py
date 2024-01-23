from odoo import http, _
from odoo.http import request
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class ProductMediaConversionWebPController(http.Controller):

    @http.route('/webp_conversion/convert', type='json', auth='user')
    def convert_to_webp(self, **kwargs):
        product_id = kwargs.get('product_id')
        if not product_id:
            return {'error': _('No product ID provided.')}

        ProductTemplate = request.env['product.template']
        product = ProductTemplate.browse(int(product_id))

        try:
            if product.exists():
                product.convert_image_to_webp()
                return {'success': _('Image converted to WebP format successfully.')}
            else:
                return {'error': _('Product not found.')}
        except Exception as e:
            _logger.exception("WebP conversion failed: %s", e)
            request.env['product_media_conversion_webp.error_log'].create({
                'name': 'Conversion Error',
                'error_detail': str(e),
                'product_id': product_id
            })
            return {'error': _('WebP conversion failed: %s') % e}

    @http.route('/webp_conversion/settings', type='json', auth='user')
    def get_webp_settings(self):
        WebPSettings = request.env['product_media_conversion_webp.webp_settings'].search([], limit=1)
        if WebPSettings:
            return {
                'quality': WebPSettings.quality,
                'overwrite': WebPSettings.overwrite
            }
        return {'error': _('WebP settings not found.')}

    @http.route('/webp_conversion/settings/save', type='json', auth='user')
    def set_webp_settings(self, **kwargs):
        try:
            WebPSettings = request.env['product_media_conversion_webp.webp_settings'].search([], limit=1)
            if not WebPSettings:
                WebPSettings = request.env['product_media_conversion_webp.webp_settings'].create({})

            WebPSettings.write({
                'quality': kwargs.get('quality'),
                'overwrite': kwargs.get('overwrite')
            })
            return {'success': _('Settings saved successfully.')}
        except Exception as e:
            _logger.exception("Saving WebP settings failed: %s", e)
            return {'error': _('Saving settings failed: %s') % e}
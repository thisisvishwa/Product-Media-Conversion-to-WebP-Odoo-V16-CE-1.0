from odoo import api, fields, models
from odoo.exceptions import UserError

class WebPConversionWizard(models.TransientModel):
    _name = 'webp.conversion.wizard'
    _description = 'Wizard for converting product images to WebP format'

    product_template_ids = fields.Many2many(
        'product.template', string='Products', help='Select products for WebP image conversion.'
    )

    @api.model
    def default_get(self, fields):
        res = super(WebPConversionWizard, self).default_get(fields)
        res['product_template_ids'] = self.env.context.get('active_ids')
        return res

    def action_convert_images(self):
        self.ensure_one()
        product_templates = self.product_template_ids
        for product_template in product_templates:
            try:
                product_template.convert_to_webp()
            except Exception as e:
                self.env['error.log'].create({
                    'name': 'WebP Conversion Error',
                    'error_description': str(e),
                    'model': 'product.template',
                    'res_id': product_template.id,
                })
                raise UserError('Error during WebP conversion: %s' % str(e))
        return {'type': 'ir.actions.act_window_close'}
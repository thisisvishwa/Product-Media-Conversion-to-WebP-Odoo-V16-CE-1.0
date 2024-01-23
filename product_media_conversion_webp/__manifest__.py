{
    'name': 'Product Media Conversion to WebP',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Converts product images to WebP format for faster loading',
    'sequence': '10',
    'author': 'Vishwa G',
    'website': 'https://thisis.com',
    'license': 'AGPL-3',
    'depends': ['base', 'website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/webp_conversion_settings_views.xml',
        'views/error_log_views.xml',
        'data/initial_data.xml',
        'wizards/webp_conversion_wizard.py',
    ],
    'demo': [
        'demo/demo_data.xml',
    ],
    'qweb': [
        'static/src/xml/webp_conversion_templates.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'assets': {
        'web.assets_backend': [
            'product_media_conversion_webp/static/src/js/webp_conversion.js',
            'product_media_conversion_webp/static/src/css/webp_conversion.css',
        ],
    },
    'images': ['static/description/banner.png'],
    'description': """
Product Media Conversion to WebP Module
=======================================
This module automatically converts product images to the WebP format, optimizing them for faster loading on browsers and devices while maintaining the original image quality.
    """,
}
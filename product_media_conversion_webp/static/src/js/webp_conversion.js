odoo.define('product_media_conversion_webp.webp_conversion', function (require) {
    "use strict";

    var ajax = require('web.ajax');
    var core = require('web.core');
    var Widget = require('web.Widget');
    var QWeb = core.qweb;

    var WebPConversionButton = Widget.extend({
        template: 'webp_conversion_templates.webp_conversion_button',
        events: {
            'click': '_onClick',
        },
        init: function (parent, options) {
            this._super(parent);
            this.options = options || {};
        },
        _onClick: function () {
            var self = this;
            ajax.jsonRpc('/webp/conversion', 'call', {
                'product_id': this.options.product_id
            }).then(function (result) {
                if (result.success) {
                    self.do_notify(core._t('Conversion Success'), core._t('The image has been successfully converted to WebP format.'));
                } else {
                    self.do_warn(core._t('Conversion Error'), core._t('There was an error converting the image to WebP format.'));
                }
            }).guardedCatch(function (error) {
                self.do_warn(core._t('Conversion Error'), core._t('There was an error converting the image to WebP format.'));
            });
        },
    });

    core.action_registry.add('webp_conversion_button', WebPConversionButton);

    return {
        WebPConversionButton: WebPConversionButton,
    };
});
{
    'name': 'Arts & Crafts Store',
    'version': '1.0',
    'category': 'Retail',
    'depends': [
        'hr_hourly_cost',
        'knowledge',
        'pos_sale',
        'product_email_template',
        'purchase_stock',
        'sale_service',
        'stock_delivery',
        'web_studio',
        'website_crm',
        'website_sale_autocomplete',
        'website_sale_collect',
        'website_sale_comparison',
        'website_sale_loyalty',
        'website_sale_wishlist',
    ],
    'data': [
        'data/res_config_settings.xml',
        'data/base_automation.xml',
        'data/ir_actions_server.xml',
        'data/ir_attachment_pre.xml',
        'data/ir_model_fields.xml',
        'data/ir_ui_view.xml',
        'data/qweb_view.xml',
        'data/product_public_category.xml',
        'data/product_category.xml',
        'data/uom_uom.xml',
        'data/pos_category.xml',
        'data/product_template.xml',
        'data/product_attribute.xml',
        'data/product_attribute_value.xml',
        'data/product_pricelist.xml',
        'data/product_template_attribute_line.xml',
        'data/product_template_attribute_value.xml',
        'data/product_product.xml',
        'data/product_pricelist_item.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
        'data/knowledge_article_favorite.xml',
        'data/pos_payment_method.xml',
        'data/pos_config.xml',
        'data/mail_message.xml',
        'data/website_view.xml',
        'data/knowledge_tour.xml',
    ],
    'demo': [
        'demo/res_partner.xml',
        'demo/crm_lead.xml',
        'demo/product_supplierinfo.xml',
        'demo/product_template.xml',
        'demo/loyalty_program.xml',
        'demo/loyalty_rule.xml',
        'demo/loyalty_reward.xml',
        'demo/purchase_order.xml',
        'demo/purchase_order_line.xml',
        'demo/purchase_order_post.xml',
        'demo/sale_order.xml',
        'demo/sale_order_line.xml',
        'demo/sale_order_post.xml',
        'demo/payment_provider_demo_post.xml',
        'demo/website_view.xml',
        'demo/website_ir_attachment.xml',
        'demo/website_page.xml',
        'demo/website_menu.xml',
        'demo/website_theme_apply.xml',
        'demo/website.xml',
    ],
    'license': 'OPL-1',
    'assets': {
        'web.assets_backend': [
            'art_craft/static/src/js/my_tour.js',
        ]
    },
    'author': 'Odoo S.A.',
    "cloc_exclude": [
        "data/knowledge_article.xml",
        "data/qweb_view.xml",
        "static/src/js/my_tour.js",
        "data/website_view.xml",
        "demo/website_view.xml",
    ],
    'images': ['images/main.png'],
}

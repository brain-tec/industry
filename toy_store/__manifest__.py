{
    'name': 'Toy Store',
    'version': '1.0',
    'category': 'Retail',
    'depends': [
        'hr',
        'knowledge',
        'point_of_sale',
        'purchase_stock',
        'stock',
        'website_sale_comparison_wishlist',
        'website_sale_loyalty',
    ],
    'data': [
        'data/res_config_settings.xml',
        'data/ir_attachment_pre.xml',
        'data/product_public_category.xml',
        'data/pos_category.xml',
        'data/pos_config.xml',
        'data/product_tag.xml',
        'data/product_template.xml',
        'data/product_attribute.xml',
        'data/product_attribute_value.xml',
        'data/product_template_attribute_line.xml',
        'data/product_template_attribute_value.xml',
        'data/product_product.xml',
        'data/product_image.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
        'data/knowledge_article_favorite.xml',
        'data/mail_message.xml',
        'data/ir_attachment_post.xml',
        'data/knowledge_tour.xml',
    ],
    'demo': [
        'demo/res_partner.xml',
        'demo/hr_employee.xml',
        'demo/product_template.xml',
        'demo/product_attribute_value.xml',
        'demo/product_template_attribute_line.xml',
        'demo/product_template_attribute_value.xml',
        'demo/stock_quant.xml',
        'demo/product_supplierinfo.xml',
        'demo/loyalty_program.xml',
        'demo/loyalty_reward.xml',
        'demo/loyalty_rule.xml',
        'demo/loyalty_card.xml',
        'demo/website_view.xml',
        'demo/website_theme_apply.xml',
        'demo/purchase_order.xml',
        'demo/purchase_order_line.xml',
        'demo/purchase_order_confirm.xml',
        'demo/stock_warehouse_orderpoint.xml',
        'demo/payment_provider_demo_post.xml',
        'demo/website.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'toy_store/static/src/js/my_tour.js',
        ]
    },
    "cloc_exclude": [
        "data/knowledge_article.xml",
        "static/src/js/my_tour.js",
        "demo/website_view.xml",
    ],
    'license': 'OPL-1',
    'author': 'Odoo S.A.',
    'images': ['images/main.png'],
}

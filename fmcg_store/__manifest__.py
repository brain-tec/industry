{
    'name': 'Grocery Store',
    'version': '1.0',
    'category': 'Retail',
    'depends': [
        'account_followup',
        'knowledge',
        'loyalty',
        'pos_discount',
        'pos_sale',
        'product_expiry',
        'purchase_stock',
        'stock_barcode',
        'stock_delivery',
    ],
    'data': [
        'data/res_config_settings.xml',
        'data/ir_attachment_pre.xml',
        'data/product_category.xml',
        'data/pos_category.xml',
        'data/product_tag.xml',
        'data/pos_config.xml',
        'data/product_template.xml',
        'data/product_attribute.xml',
        'data/product_attribute_value.xml',
        'data/product_template_attribute_line.xml',
        'data/product_template_attribute_value.xml',
        'data/product_product.xml',
        'data/product_packaging.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
        'data/knowledge_article_favorite.xml',
        'data/mail_message.xml',
        'data/knowledge_tour.xml',
    ],
    'demo': [
        'demo/res_partner.xml',
        'demo/product_supplierinfo.xml',
        'demo/loyalty_program.xml',
        'demo/loyalty_rule.xml',
        'demo/loyalty_reward.xml',
        'demo/sale_order.xml',
        'demo/sale_order_line.xml',
        'demo/stock_lot.xml',
        'demo/purchase_order.xml',
        'demo/purchase_order_line.xml',
        'demo/purchase_order_post.xml',
        'demo/sale_order_post.xml',
        'demo/pos_payment_method.xml',
        'demo/payment_provider_demo_post.xml',
        'demo/payment_provider.xml',
        'demo/payment_method.xml',
        'demo/pos_config.xml',
        'demo/pos_session.xml',
        'demo/pos_order.xml',
        'demo/pos_order_line.xml',
        'demo/pos_confirm.xml',
    ],
    'license': 'OPL-1',
    'assets': {
        'web.assets_backend': [
            'fmcg_store/static/src/js/my_tour.js',
        ]
    },
    'author': 'Odoo S.A.',
    "cloc_exclude": [
        "data/knowledge_article.xml",
        "static/src/js/my_tour.js",
    ],
    'images': ['images/main.png'],
}

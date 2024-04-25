{
    'name': 'Restaurant (Foods & Cafes)',
    'version': '1.0',
    'category': 'Services',
    'description': """
        This Odoo module is designed to streamline and enhance the management of your restaurant operations.
        Whether you own a fine dining establishment, a cafe, or fast-food joints, cafés, food trucks, cloud kitchens, and more.
    """,
    'depends': [
        'account_followup',
        'knowledge',
        'payment_demo',
        'pos_enterprise',
        'pos_loyalty',
        'pos_online_payment_self_order',
        'pos_restaurant_appointment',
        'sale_management',
        'website_appointment',
        'website_sale',
    ],
    'data': [
        'data/res_config_settings.xml',
        'data/restaurant_floor.xml',
        'data/restaurant_table.xml',
        'data/appointment_type.xml',
        'data/ir_attachment_pre.xml',
        'data/product_public_category.xml',
        'data/pos_category.xml',
        'data/pos_payment_method.xml',
        'data/pos_config.xml',
        'data/product_category.xml',
        'data/pos_combo.xml',
        'data/product_product.xml',
        'data/pos_combo_line.xml',
        'data/payment_provider_demo.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
    ],
    'demo': [
        'demo/pos_payment_method.xml',
        'demo/pos_config.xml',
        'demo/res_partner.xml',
        'demo/appointment_type.xml',
        'demo/calendar_event.xml',
        'demo/stock_quant.xml',
        'demo/sale_order.xml',
        'demo/sale_order_line.xml',
        'demo/sale_order_post.xml',
        'demo/pos_session.xml',
        'demo/pos_order.xml',
        'demo/pos_order_line.xml',
        'demo/pos_confirm.xml',
        'demo/pos_payment.xml',
        'demo/pos_preparation_display.xml',
        'demo/pos_preparation_display_order.xml',
        'demo/pos_preparation_display_orderline.xml',
        'demo/pos_preparation_display_stage.xml',
        'demo/pos_preparation_display_confirm.xml',
        'demo/payment_provider_demo.xml',
        'demo/website_view.xml',
    ],
    'license': 'OPL-1',
    'images': ['images/main.png'],
}
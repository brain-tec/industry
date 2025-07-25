{
    'name': 'Florist',
    'version': '1.0',
    'category': 'Retail',
    'author': 'Odoo S.A.',
    'depends': [
        'crm_enterprise',
        'knowledge',
        'pos_enterprise',
        'pos_hr',
        'pos_loyalty',
        'pos_online_payment',
        'project_enterprise',
        'sale_crm',
        'sale_loyalty',
        'sale_purchase',
        'spreadsheet_sale_management',
        'website_crm',
    ],
    'data': [
        'data/res_config_settings.xml',
        'data/ir_attachment_pre.xml',
        'data/pos_category.xml',
        'data/pos_payment_method.xml',
        'data/pos_config.xml',
        'data/product_category.xml',
        'data/uom_uom.xml',
        'data/product_template.xml',
        'data/product_attribute.xml',
        'data/product_attribute_value.xml',
        'data/product_pricelist.xml',
        'data/product_pricelist_item.xml',
        'data/product_template_attribute_line.xml',
        'data/product_template_attribute_value.xml',
        'data/product_product.xml',
        'data/project_project_stage.xml',
        'data/project_task_type.xml',
        'data/sale_order_template.xml',
        'data/sale_order_template_line.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
        'data/mail_message.xml',
        'data/mail_template.xml',
        'data/knowledge_article_favorite.xml',
        'data/knowledge_tour.xml',
        'data/website_view.xml',
        'data/website_theme_apply.xml',
    ],
    'demo': [
        'demo/crm_stage.xml',
        'demo/crm_tag.xml',
        'demo/crm_team.xml',
        'demo/loyalty_program.xml',
        'demo/hr_job.xml',
        'demo/res_partner.xml',
        'demo/res_users.xml',
        'demo/loyalty_rule.xml',
        'demo/hr_department.xml',
        'demo/pos_session.xml',
        'demo/hr_employee.xml',
        'demo/crm_lead.xml',
        'demo/purchase_order.xml',
        'demo/purchase_order_line.xml',
        'demo/pos_order.xml',
        'demo/loyalty_reward.xml',
        'demo/pos_order_line.xml',
        'demo/sale_order.xml',
        'demo/ir_attachment_post.xml',
        'demo/project_project.xml',
        'demo/project_task.xml',
        'demo/mail_activity.xml',
        'demo/sale_order_line.xml',
        'demo/sale_order_confirm.xml',
        'demo/product_supplierinfo.xml',
        'demo/website_view.xml',
        'demo/website_theme_apply.xml',
        'demo/website.xml',
    ],
    'license': 'OPL-1',
    'assets': {
        'web.assets_backend': [
            'florist/static/src/js/my_tour.js'
        ]
    },
    'cloc_exclude': [
        'data/knowledge_article.xml',
        'static/src/js/my_tour.js',
        'data/website_view.xml',
        'demo/website_view.xml',
    ],
    'images': [
        'images/main.png',
    ],
}

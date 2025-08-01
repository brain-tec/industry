{
    'name': 'Surveying & Mapping',
    'version': '1.0',
    'category': 'Services',
    'depends': [
        'base_automation',
        'crm',
        'documents',
        'hr_timesheet',
        'knowledge',
        'planning',
        'sale_project',
        'web_studio',
        'website',
    ],
    'data': [
        'data/res_config_settings.xml',
        'data/ir_attachment_pre.xml',
        'data/base_automation.xml',
        'data/ir_actions_server.xml',
        'data/project_task_type.xml',
        'data/documents_folder.xml',
        'data/account_analytic_plan.xml',
        'data/account_analytic_account.xml',
        'data/project_project.xml',
        'data/planning_role.xml',
        'data/product_template.xml',
        'data/product_product.xml',
        'data/sale_order_template.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
        'data/knowledge_article_favorite.xml',
        'data/mail_message.xml',
        'data/website_view.xml',
        'data/knowledge_tour.xml',
    ],
    'demo': [
        'demo/res_partner.xml',
        'demo/crm_stage.xml',
        'demo/crm_lead.xml',
        'demo/sale_order.xml',
        'demo/planning_slot.xml',
        'demo/website_view.xml',
        'demo/website_page.xml',
        'demo/website_menu.xml',
        'demo/website_theme_apply.xml',
        'demo/website_ir_attachment.xml',
        'demo/website.xml',
    ],
    'license': 'OPL-1',
    'assets': {
        'web.assets_backend': [
            'surveyor/static/src/js/my_tour.js',
        ]
    },
    'author': 'Odoo S.A.',
    'images': ['images/main.png'],
    "cloc_exclude": [
        "data/knowledge_article.xml",
        "data/website_view.xml",
        "static/src/js/my_tour.js",
        "demo/website_view.xml",
    ],
}

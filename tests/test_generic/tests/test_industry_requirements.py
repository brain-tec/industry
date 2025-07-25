# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import re

from odoo.tests import tagged, get_db_name
from odoo.tools import cloc

from .industry_case import IndustryCase

_logger = logging.getLogger(__name__)


@tagged('post_install', '-at_install')
class TestEnv(IndustryCase):

    def test_payment_demo(self):
        db_name = get_db_name()
        if not db_name.endswith('imported_with_demo'):
            return
        no_online_payment_industries = [
            'bike_leasing',
            'real_estate',
        ]
        if any(m in self.installed_modules for m in no_online_payment_industries):
            # we don't pay the cart in this industry, we get a quote or fill a form
            return
        if self.env['ir.module.module']._get('website_sale').state == 'installed':
            self.assertTrue(
                self.env['ir.module.module']._get('payment_demo').state == 'installed',
                "Payment Demo module should be installed in demo when Website Sale is installed. "
                "Call 'button_immediate_install' on 'base.module_payment_demo' in demo."
            )

    def test_welcome_article_exists(self):
        for module in self.installed_industries:
            ref = self.env.ref(f"{module}.welcome_article", raise_if_not_found=False)
            self.assertTrue(
                ref, f"You forgot to define a record with id='welcome_article' in module '{module}'."
            )

    def test_welcome_article_body_exists(self):
        for module in self.installed_industries:
            ref = self.env.ref(f"{module}.welcome_article_body", raise_if_not_found=False)
            self.assertTrue(
                ref, f"You forgot to define a template with id='welcome_article_body' in module '{module}'."
            )

    def test_knowledge_article_notification(self):
        for module in self.installed_industries:
            if not self.env.ref(module + '.knowledge_tour', raise_if_not_found=False):
                _logger.warning("You forgot to define a `knowledge.tour` with `id=knowledge_tour`.")

            if not (ref := self.env.ref(module + '.notification_knowledge', raise_if_not_found=False)):
                _logger.warning("You forgot to define a `mail.message` with `id=notification_knowledge`.")
            notif = ref and self.env['mail.message'].browse(ref.id)
            if notif and '/knowledge/article/' not in notif.body:
                _logger.warning("The mail.message should contain a link to the knowledge article.")

            knowledge = self.env['ir.model.data'].search(
                [('model', '=', 'knowledge.article'), ('module', '=', module)], limit=1
            )
            if not knowledge:
                _logger.warning("Missing knowledge article for the industry module.")
            knowledge_article = knowledge and self.env.ref(knowledge.complete_name)
            if knowledge and knowledge_article.favorite_count == 0:
                _logger.warning("The knowledge article should be in the favorite category")
            if notif and knowledge and '/knowledge/article/%s' % knowledge_article.id not in notif.body:
                _logger.warning("The notification link should target the module-related knowledge article.")

    def test_cloc_exclude_view(self):
        c = cloc.Cloc()
        c.count_database(self.env.cr.dbname)
        c.report(True)  # show details of cloc in the logs
        for module in self.installed_modules:
            for cloc_entry in c.modules.get(module, {}):
                message = "The view '%s' is counted in the maintenance lines. " % cloc_entry
                message += "Please add the file in 'cloc_exclude' list of the manifest."
                self.assertEqual(len(cloc_entry.split(':')), 2, message)

    def test_sale_ok_and_is_published_in_db(self):
        models = ["product.template", "product.product"]
        for model in models:
            if "is_published" in self.env[model]._fields:
                records = self.env[model].search(
                    [("is_published", "=", True), ("sale_ok", "=", False)]
                )

                self.assertFalse(
                    records,
                    "Found records with 'is_published=True' and 'sale_ok=False' in the database. Records: %s"
                    % ", ".join(
                        ["%s (ID: %s)" % (record.display_name, record.id) for record in records],
                    ),
                )

    def test_knowledge_article_links_use_latest(self):
        pattern = r'https?://www\.odoo\.com/documentation/(?!latest/)(\d+\.\d+|master)/'
        for module in self.installed_modules:
            knowledge = self.env['ir.model.data'].search(
                [('model', '=', 'knowledge.article'), ('module', '=', module)], limit=1
            )
            if not knowledge:
                continue
            knowledge_article = self.env.ref(knowledge.complete_name)
            content = knowledge_article.body or ''
            matches = re.findall(pattern, content)
            self.assertFalse(
                matches,
                "Found links to Odoo documentation using version-specific URLs in module '%s' knowledge article: %s. Please use '/latest/' instead."
                % (module, matches),
            )

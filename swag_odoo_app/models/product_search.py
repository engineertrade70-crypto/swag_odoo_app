
import xmlrpc.client
from odoo import models, fields, api

class SwagProductSearch(models.Model):
    _name = "swag.product.search"
    _description = "SWAG Product Comparison Search"

    config_id = fields.Many2one("swag.odoo.config", "Config")
    search_codes = fields.Text("Product Codes (one per line)")
    exact_match = fields.Boolean("Exact Match", default=False)
    low_stock = fields.Integer("Low Stock Threshold", default=5)

    results = fields.Text("Search Results JSON")
    excel_file = fields.Binary("Export Excel")
    filename = fields.Char("Filename")

    @api.model
    def search_multi_odoo(self, codes, config):
        """Search across 4 Odoo systems"""
        systems = {
            "SWAG": (config.swag_url, config.swag_db, config.swag_user, config.swag_password),
            "La Rouche": (config.larouche_url, config.larouche_db, config.larouche_user, config.larouche_password),
            "Different Clothes": (config.diff_clothes_url, config.diff_clothes_db, config.diff_clothes_user, config.diff_clothes_password),
            "Fashion Limits": (config.fashion_limits_url, config.fashion_limits_db, config.fashion_limits_user, config.fashion_limits_password),
        }

        all_results = []
        for name, (url, db, user, pwd) in systems.items():
            try:
                common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
                uid = common.authenticate(db, user, pwd, {})
                if uid:
                    models_proxy = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                    domain = [["default_code", "in", codes]]
                    products = models_proxy.execute_kw(db, uid, pwd, 
                        "product.product", "search_read", [domain], 
                        {"fields": ["default_code", "name", "qty_available", "list_price"]})
                    for p in products:
                        p["system"] = name
                    all_results.extend(products)
            except Exception as e:
                all_results.append({"system": name, "error": str(e)})

        return all_results

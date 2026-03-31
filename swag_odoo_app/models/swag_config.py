
from odoo import models, fields

class SwagOdooConfig(models.Model):
    _name = "swag.odoo.config"
    _description = "SWAG Multi Odoo Configuration"

    name = fields.Char("Config Name", default="SWAG Systems")

    # 4 Systems
    swag_url = fields.Char("SWAG URL")
    swag_db = fields.Char("SWAG Database")
    swag_user = fields.Char("SWAG User")
    swag_password = fields.Char("SWAG Password")

    larouche_url = fields.Char("La Rouche URL")
    larouche_db = fields.Char("La Rouche Database")
    larouche_user = fields.Char("La Rouche User")
    larouche_password = fields.Char("La Rouche Password")

    diff_clothes_url = fields.Char("Different Clothes URL")
    diff_clothes_db = fields.Char("Different Clothes Database")
    diff_clothes_user = fields.Char("Different Clothes User")
    diff_clothes_password = fields.Char("Different Clothes Password")

    fashion_limits_url = fields.Char("Fashion Limits URL")
    fashion_limits_db = fields.Char("Fashion Limits Database")
    fashion_limits_user = fields.Char("Fashion Limits User")
    fashion_limits_password = fields.Char("Fashion Limits Password")

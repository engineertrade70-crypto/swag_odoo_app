
{
    "name": "SWAG Product Comparison Dashboard",
    "version": "17.0.1.0",
    "summary": "Multi Odoo Product Search + Filters + PDF Parsing + Excel Export",
    "description": """
        SWAG Product Comparison Dashboard
        • 4 Odoo systems sync (SWAG, La Rouche, Different Clothes, Fashion Limits)
        • Advanced search + filters + sort
        • PDF invoice code extraction
        • Excel export with charts
        • Dark theme + Arabic/English
    """,
    "author": "swag",
    "category": "Inventory/Analytics",
    "depends": ["base", "sale", "stock", "web", "spreadsheet"],
    "data": [
        "security/ir.model.access.csv",
        "views/swag_dashboard.xml",
        "views/multi_config.xml",
        "views/product_search.xml",
        "wizards/pdf_parser_wizard.xml",
        "reports/excel_export.xml"
    ],
    "assets": {
        "web.assets_backend": [
            "swag_odoo_app/static/src/**/*",
        ],
        "web.assets_spreadsheet": [
            "swag_odoo_app/static/src/spreadsheet/**/*",
        ],
    },
    "application": True,
    "installable": True,
    "auto_install": False,
}

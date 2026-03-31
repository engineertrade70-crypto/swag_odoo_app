
from odoo import models, fields, api
import re
from pypdf import PdfReader

class PdfParserWizard(models.TransientModel):
    _name = "swag.pdf.parser"

    pdf_file = fields.Binary("Upload PDF Invoice")
    filename = fields.Char()

    extracted_codes = fields.Text("Extracted Codes")

    def parse_pdf(self):
        """Extract product codes from PDF invoice"""
        if not self.pdf_file:
            return {"type": "ir.actions.client", "tag": "display_notification", "params": {"title": "No file", "message": "Upload PDF first", "type": "warning"}}

        import io
        reader = PdfReader(io.BytesIO(self.pdf_file))
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"

        # Your regex patterns
        patterns = [
            r'\[([A-Za-z0-9\-\_]{3,30})\]',
            r'([A-Z]{2,6}\d+(?:-\d+)?(?:-[A-Z0-9()]{1,10})?)\s+.{0,80}?\d+\.?\d*\s+SR'
        ]

        codes = set()
        for pattern in patterns:
            codes.update(re.findall(pattern, text, re.MULTILINE))

        self.extracted_codes = "\n".join(sorted(codes))
        return {"type": "ir.actions.client", "tag": "reload"}

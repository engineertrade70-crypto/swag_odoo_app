FROM odoo:19.0

USER root

# Install pypdf for PDF parsing
RUN pip3 install pypdf openpyxl --break-system-packages

# Copy custom module
COPY ./swag_odoo_app /mnt/extra-addons/swag_odoo_app

# Copy odoo config
COPY ./odoo.conf /etc/odoo/odoo.conf

# Fix permissions
RUN chown -R odoo:odoo /mnt/extra-addons

USER odoo

EXPOSE 8069

CMD ["odoo", "--config=/etc/odoo/odoo.conf"]

# Copyright 2021 openNova - Juan Pablo Garza <juanp@opennova.com.ar>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api

class WhatsappTemplate(models.Model):
    _name = 'on.whatsapp.template'
    _description = 'Message default in Whatsapp'
    
    name = fields.Char(string="Nombre")
    template_message = fields.Text(string="Mensaje")
    category = fields.Selection([('other', 'Other')], default='other', string="Categoría")

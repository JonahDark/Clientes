from odoo import models, fields, api


class producto_model(models.Model):

    _name = 'clientes.producto_model'
    _description = 'Modelo de producto'

    name = fields.Char(string="Referencia", required=True, index=True)
    descripcion = fields.Html(string="Descripcion", required=True)
    pvp = fields.Integer(string="Precio")
    factura = fields.Many2one("clientes.factura_model",string="Factura")

from odoo import models, fields, api
from datetime import datetime


class factura_model(models.Model):

    _name = 'clientes.factura_model'
    _description = 'Modelo de factura'

    name = fields.Char(string="Ref", index=True, required=True)
    fecha = fields.Date(string="Fecha", required=True, default=datetime.now())
    cliente = fields.Many2one('clientes.cliente_model', string="Cliente")
    productos = fields.One2many("clientes.producto_model","factura", string="Productos")
    base = fields.Integer(string="Base", compute="_calculoBase", default=0.0)
    iva = fields.Selection([('21%', 0.21), ('15%',0.15), ('7%',0.07), ('0%',0.0)], string="IVA", default=[('21%',0.21)])
    total = fields.Integer(string="Total", compute="_calculoTotal")

    @api.depends("productos")
    def _calculoBase(self):
        for i in self.productos:
            self.base += i.pvp

    @api.depends("base")
    def _calculoTotal(self):
        for i in self.iva:
            self.total = (self.base * int(i)) + self.base

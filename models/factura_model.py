from odoo import models, fields, api
from datetime import datetime


class factura_model(models.Model):

    _name = 'clientes.factura_model'
    _description = 'Modelo de factura'

    name = fields.Char(string="Ref", index=True, required=True)
    fecha = fields.Date(string="Fecha", required=True, default=datetime.now())
    cliente = fields.Many2one('clientes.cliente_model', string="Cliente")
    base = fields.Integer(string="Base", compute="_calculoBase", default=0.0, store=True)
    iva = fields.Selection([('21', '21%'), ('15', '15%'),('7', '7%'), ('0', '0%')], string="IVA", default='21')
    total = fields.Integer(string="Total", compute="_calculoTotal", store=True)

    # Una factura puede tener muchas lineas de detalle
    detalle_factura = fields.One2many("clientes.detalle_model", "id_factura", "Factura")

    @api.depends("detalle_factura")
    def _calculoBase(self):
        self.ensure_one()
        _base = 0
        for i in self.detalle_factura:
            _base += i.id_producto.precio * i.cantidad
        self.base = _base

    @api.depends("base","iva")
    def _calculoTotal(self):
        self.ensure_one()
        self.total=self.base * int(self.iva) + self.base
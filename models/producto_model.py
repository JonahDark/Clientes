from odoo import models, fields, api


class producto_model(models.Model):

    _name = 'clientes.producto_model'
    _description = 'Modelo de producto'

    name = fields.Char(string="Nombre", required=True, index=True)
    descripcion = fields.Html(string="Descripcion", required=True)
    precio = fields.Integer(string="Precio")

    
    detalle_producto=fields.One2many("clientes.detalle_model","id_producto","producto")#Un producto puede estar en muchas lineas de detalle
    

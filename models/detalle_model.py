from odoo import models, fields, api


class detalle_model(models.Model):

    _name = 'clientes.detalle_model'
    _description = 'Detalle de la factura'

    id_producto = fields.Many2one("clientes.producto_model","Producto")#Pueden haber muchas lineas con un producto 
    id_factura = fields.Many2one("clientes.factura_model","Factura") #Pueden haber muchas lineas con una factura
    cantidad = fields.Integer(string="Cantidad")

    #Al ser un pojo, en el modelo donde se encuentre el One2many referenciado al Many2one de aquí, podemos acceder a 
    #cualquier atributo y si este atributo a su vez es otro pojo, tambien accederemos a sus atributos correspondientes.

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class cliente_model(models.Model):

    _name = 'clientes.cliente_model'
    _description = 'Modelo de cliente'

    
    name = fields.Char(string="Nombre", required=True)
    dni = fields.Char(string="DNI", index=True, required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    foto = fields.Binary(string="Foto")
    telefono = fields.Char(string="Telefono", required=True)
    email = fields.Char(string="Email", required=True)
    facturas = fields.One2many('clientes.factura_model','cliente',string="Facturas")

    @api.constrains('dni')
    def _validarDNI(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        letra = self.dni[-1]
        num = self.dni[:-1]
        posi = int(num) % 23
        if letra != letras[posi]:
            raise ValidationError("DNI no valido")
        if len(self.dni) > 9:
            raise ValidationError("El DNI no puede ser mayor de 9 caracteres")
        if letra.isnumeric():
            raise ValidationError("El DNI debe terminar con una letra")

    @api.constrains('telefono')
    def _validarTelefono(self):
        if len(self.telefono)>9 or len(self.telefono)<9:
            raise ValidationError("El telefono debe contener 9 digitos")        

    @api.constrains('email')
    def _validarEmail(self):
        if '@' not in self.email:
            raise ValidationError("El email debe contener un @")
        if '.' not in self.email:
            raise ValidationError("El email debe contener un .")
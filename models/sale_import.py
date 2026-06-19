from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ImportedSale(models.Model):
    _name = 'imported.sale'
    _description = 'Imported Sales'
    _rec_name = 'customer'

    date = fields.Date(
        string='Fecha',
        required=True
    )

    customer = fields.Char(
        string='Cliente',
        required=True
    )

    seller = fields.Char(
        string='Vendedor',
        required=True
    )

    product = fields.Char(
        string='Producto',
        required=True
    )

    quantity = fields.Float(
        string='Cantidad',
        required=True
    )

    unit_value = fields.Float(
        string='Valor Unitario'
    )

    total_value = fields.Float(
        string='Valor Total',
        required=True
    )

    state = fields.Selection([
        ('confirmada', 'Confirmada'),
        ('pendiente', 'Pendiente'),
        ('cancelada', 'Cancelada')
    ], string='Estado', required=True)

    @api.constrains('quantity')
    def _check_quantity(self):
        for rec in self:
            if rec.quantity <= 0:
                raise ValidationError(
                    "La cantidad debe ser mayor a cero."
                )

    @api.constrains('total_value')
    def _check_total(self):
        for rec in self:
            if rec.total_value <= 0:
                raise ValidationError(
                    "El valor total debe ser mayor a cero."
                )
import base64
import io
import openpyxl

from odoo import models, fields
from odoo.exceptions import ValidationError


class ImportSalesWizard(models.TransientModel):
    _name = 'import.sales.wizard'
    _description = 'Import Sales Wizard'

    file = fields.Binary(
        string='Archivo de Excel',
        required=True
    )

    filename = fields.Char()

    def action_import(self):

        file_data = base64.b64decode(self.file)

        workbook = openpyxl.load_workbook(
            io.BytesIO(file_data)
        )

        sheet = workbook.active

        row_number = 1

        for row in sheet.iter_rows(
                min_row=2,
                values_only=True):

            row_number += 1

            (
                date,
                customer,
                seller,
                product,
                quantity,
                unit_value,
                total_value,
                state
            ) = row

            if not date:
                raise ValidationError(
                    f"Fila {row_number}: Fecha obligatoria"
                )

            if not customer:
                raise ValidationError(
                    f"Fila {row_number}: Cliente obligatorio"
                )

            if not seller:
                raise ValidationError(
                    f"Fila {row_number}: Vendedor obligatorio"
                )

            if not product:
                raise ValidationError(
                    f"Fila {row_number}: Producto obligatorio"
                )

            if not state:
                raise ValidationError(
                    f"Fila {row_number}: Estado obligatorio"
                )

            if quantity <= 0:
                raise ValidationError(
                    f"Fila {row_number}: Cantidad inválida"
                )

            if total_value <= 0:
                raise ValidationError(
                    f"Fila {row_number}: Valor total inválido"
                )

            self.env['imported.sale'].create({
                'date': date,
                'customer': customer,
                'seller': seller,
                'product': product,
                'quantity': quantity,
                'unit_value': unit_value,
                'total_value': total_value,
                'state': str(state).lower(),
            })

        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }
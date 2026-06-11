from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CarAgency(models.Model):
    _name = 'car.car'
    _description = 'Car'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string="Car Model", required=True, tracking=True)
    registration_number = fields.Char(string="Registration Number", required=True)
    mileage = fields.Float(string="Mileage")
    state = fields.Selection([
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('damaged', 'Damaged')
    ], string="State",
        default='available',
        required=True,
        tracking=True)

    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    sequence = fields.Char(string='Sequence Number', readonly=True, copy=False)
    image = fields.Image(string="Car Image")

    customer_id = fields.Many2one('res.partner', string="Customer")
    agency_id = fields.Many2one('car.agency', string="Agency")
    damage_reason = fields.Text(string="Damage Reason")

    @api.constrains('registration_number')
    def _check_registration_number(self):
        for rec in self:
            if not rec.registration_number.isdigit():
                raise ValidationError("Registration number must be positive!")
        if len(str(rec.registration_number)) != 8:
            raise ValidationError("Registration number must contain exactly 8 digits!")

        existing_car = self.search([
            ('registration_number', '=', rec.registration_number)
        ])
        if len(existing_car) > 1:
            raise ValidationError(
                "Registration number must be unique!"
            )

    def action_open_damage_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Damage Wizard',
            'res_model': 'damage.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_car_id': self.id,
            }
        }

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['sequence'] = self.env['ir.sequence'].next_by_code('car.sequence')
            vals['state'] = vals.get('state') or 'available'

        return super().create(vals_list)

    def action_set_available(self):
        self.state = 'available'

    def action_set_rented(self):
        self.state = 'rented'

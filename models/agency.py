from odoo import models, fields

class Agency(models.Model):
    _name = 'car.agency'
    _description = 'Agency'
    name = fields.Char(string='Agency Name', required=True)

    responsible_id = fields.Many2one( 'res.partner',string="Responsible", required=True )
    car_ids = fields.One2many('car.car', 'agency_id', string="Cars")
    brand_ids = fields.One2many('car.brand','agency_id',string='Brands')
    brand_count = fields.Integer(string='Brands Count',compute='_compute_brand_count')

    def _compute_brand_count(self):
        for rec in self:
            rec.brand_count = len(rec.brand_ids)

    def action_open_brands(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Brands',
            'res_model': 'car.brand',
            'view_mode': 'list,form',
            'domain': [('agency_id', '=', self.id)],
            'target': 'current',
        }







from odoo import models, fields
class Brand(models.Model):
    _name = 'car.brand'
    _description = 'Brand'

    name = fields.Char( string="Brand Name",required=True)
    image = fields.Binary( string="Image")
    description = fields.Text( string="Description")
    agency_id = fields.Many2one(
        'car.agency'
        , string="Agency", required=True)


    brand_ids = fields.One2many(
        'car.brand',
        'agency_id',
        string='Brands'
    )
    brand_count = fields.Integer(
        string='Brands Count',
        compute='_compute_brand_count'
    )

    def _compute_brand_count(self):
        for rec in self:
            rec.brand_count = len(rec.brand_ids)

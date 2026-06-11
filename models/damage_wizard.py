from odoo import models, fields

class DamageWizard(models.TransientModel):
   _name = 'damage.wizard'
   _description = 'Damage Wizard'
   reason = fields.Text(string="Damage Reason")
   car_id = fields.Many2one(
       'car.car',
       string="Car"
   )
   def action_confirm_damage(self):
       self.car_id.state = 'damaged'
       self.car_id.damage_reason = self.reason
       return {'type': 'ir.actions.act_window_close'}
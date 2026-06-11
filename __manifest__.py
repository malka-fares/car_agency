{
   'name': 'Car Agency',
   'version': '1.0',
   'summary': 'Car Rental Management',
   'depends': ['base', 'mail'],
   'data': [
      'data/sequence.xml',
      'security/groups.xml',
      'security/ir.model.access.csv',
       'views/car_views.xml',
      'views/brand_views.xml',
      'views/damage_wizard_views.xml',
   ],
   'application': True,
}
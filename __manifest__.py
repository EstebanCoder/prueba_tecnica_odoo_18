{
    'name': 'Sales Dashboard Import',
    'version': '18.0.1.0.0',
    'category': 'Sales',
    'summary': 'Importacion de ventas desde Excel',
    'author': 'Johan Esteban Rodriguez Duarte',
    'depends': [
        'base',
        'web',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_import_views.xml',
        'views/wizard_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
}
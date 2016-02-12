#-*- coding: utf-8 -*-

from openerp.osv import fields, osv

class Denuncia(osv.Model):
	_name = "cein.denuncia"
	_columns = {
		'name': fields.char(string="Codigo Oficial",	 size=256, required=True,help="Nombre sin acentos opcionalmente para optimizar busquedas"),		
		'code_temporal': fields.char(string="Codigo Temporal",	 size=256, required=True,help="Nombre con acentos a mostrar"),
		'tipo_denuncia_id': fields.many2one('cein.tipo_denuncia','Tipo de Denuncia'),
		'relacion_id': fields.one2many('cein.implicado','name_id','Implicados en la Denuncia'),

		'activo': fields.boolean("Activado"),
	
	}
	_defaults = {
		'activo': True,	
	}


class Implicados(osv.Model):
	_name = "cein.implicado"
	_columns = {
		 'name_id': fields.many2one('cein.denuncia','Many2one obligado',help="obligado por one2many, no necesario aparezca en vista"),
    	 'nombre': fields.many2one('cein.persona','Nombre'),
    	 'relacion': fields.many2one('cein.tipo_implicados','Tipo de Implicacion con los hechos'),
	}
	_defaults = {
		'activo': True,	
	}
	
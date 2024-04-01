from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime,timezone

class Oficina(db.Model):
	Cod_Ofi=db.Column(db.String(5),primary_key=True)
	NOMBRE=db.Column(db.String(100),unique=True,index=True)
	DESCRIPCION=db.Column(db.String(200))
	gerar=db.relationship('Gerarquia',back_populates='ofi')
	empleado=db.relationship('Persona',back_populates='servicio')
	def __repr__(self):
		return"<oficina {}>".format(self.NOMBRE)

class Gerarquia(db.Model):
	Id_Gerar=db.Column(db.Integer,primary_key=True)
	Cod_Ofi_Ante=db.Column(db.String(5))
	Cod_Ofi=db.Column(db.String(5),db.ForeignKey('oficina.Cod_Ofi'))
	ofi=db.relationship('Oficina',back_populates='gerar')

	def __repr__(self):
		return"<Gerar {}>".format(self.Cod_Ofi_Ante)

class Persona(db.Model):
	DNI=db.Column(db.String(11),index=True,primary_key=True)
	NOMBRE=db.Column(db.String(50))
	APELLIDO_PATERNO=db.Column(db.String(100))
	APELLIDO_MATERNO=db.Column(db.String(100))
	FECHA_NAC=db.Column(db.Date)
	EMAIL=db.Column(db.String(100),unique=True)
	TELEFONO=db.Column(db.String(9))
	DIRECCION=db.Column(db.String(100))
	Cod_Ofi=db.Column(db.String(5),db.ForeignKey('oficina.Cod_Ofi'))
	servicio=db.relationship('Oficina',back_populates='empleado')
	perreg=db.relationship('Perregimen',back_populates='emple')
	user=db.relationship('Usuario',back_populates='perso')

	def __repr__(self):
		return "Persona< {}>".format(self.NOMBRE)

class Regimen(db.Model):
	IdRegimen=db.Column(db.Integer,primary_key=True)
	DENOMINACION=db.Column(db.String(50),unique=True)
	HORASMENSUALES=db.Column(db.Integer)
	perr=db.relationship('Perregimen',back_populates='reg')

	def __repr__(self):
		return "Regimen <{}>".format(self.DENOMINACION)

class Perregimen(db.Model):
	IdRegPer=db.Column(db.Integer,primary_key=True)
	fecha=db.Column(db.Date,default=datetime.now(timezone.utc).date())
	DNI=db.Column(db.String(11),db.ForeignKey('persona.DNI'))
	IdRegimen=db.Column(db.Integer,db.ForeignKey('regimen.IdRegimen'))
	emple=db.relationship('Persona',back_populates='perreg')
	reg=db.relationship('Regimen',back_populates='perr')

	def __repr__(self):
		return 'fecha <{}>'.format(self.fecha)

class Turno(db.Model):
	IdTurno=db.Column(db.Integer,primary_key=True)
	NOMBRE=db.Column(db.String(20),unique=True)
	CODIGO=db.Column(db.String(5),unique=True)
	HORAS=db.Column(db.Integer)

	def __repr__(self):
		return 'turno <{}>'.format(self.NOMBRE)

class Programacion(db.Model):
	IdProgramacion=db.Column(db.Integer,primary_key=True)
	FECHAI=db.Column(db.DateTime)
	FECHAF=db.Column(db.DateTime)
	IdRegPer=db.Column(db.Integer,db.ForeignKey('perregimen.IdRegPer'))
	IdTurno=db.Column(db.Integer,db.ForeignKey('turno.IdTurno'))

	def __repr__(self):
		return "programacion <{}>".format(self.IdProgramacion)



class Perfil(db.Model):
	Idnivel=db.Column(db.Integer,primary_key=True)
	DENOMINACION=db.Column(db.String(60),unique=True)
	DESCRIPCION=db.Column(db.String(100))

	def __repr__(self):
		return "Perfil <{}>".format(self.DENOMINACION)

class Usuario(db.Model):
	DNI=db.Column(db.String(11),db.ForeignKey('persona.DNI'),primary_key=True)
	username=db.Column(db.String(50),unique=True,index=True)
	password_hash=db.Column(db.String(256))
	estado=db.Column(db.Boolean,default=True)
	Idnivel=db.Column(db.Integer,db.ForeignKey('perfil.Idnivel'))
	perso=db.relationship('Persona',back_populates='user')

	def setPassword(self,password):
		self.password_hash=generate_password_hash(password)
	def checkPassword(self,password):
		return check_password_hash(self.password_hash,password)

	def __repr__(self):
		return " username <{}>".format(self.username)

class Asignacion(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	menu=db.Column(db.String(100))
	Idnivel=db.Column(db.Integer,db.ForeignKey('perfil.Idnivel'))



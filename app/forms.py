from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,PasswordField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	usuario=StringField('Usuario',validators=[DataRequired(message="Campo Obligatorio")])
	contrasenia=PasswordField('Contraseña',validators=[DataRequired("Campo Obligatorio")])
	check_recordar=BooleanField('Recordar')
	submit=SubmitField('Iniciar Session',render_kw={'class':'btn btn-primary'})
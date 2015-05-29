from flask_wtf import Form
from wtforms import  TextField, TextAreaField, SubmitField, validators, ValidationError
 
class ContactForm(Form):
  nombre = TextField("Nombre")
  email = TextField("Email")
  telefono = TextField("Telefono")
  message = TextAreaField("Mensage")
  submit = SubmitField("Enviar")
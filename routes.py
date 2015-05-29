from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask.ext.mail import Message, Mail
 
mail = Mail()
 
app = Flask(__name__)
 
app.secret_key = 'development key'
 
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'gypnetwork.info@gmail.com'
app.config["MAIL_PASSWORD"] = 'charchatel'
 
mail.init_app(app)
 
@app.route('/')
@app.route('/inicio')
def home():
  return render_template('home.html')

@app.route('/sobre')
def sobre():
  return render_template('sobre.html')

@app.route('/ubicacion')
def ubicacion():
  return render_template('ubicacion.html')

@app.route('/galeria')
def galeria():
  return render_template('galeria.html')



@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
  form = ContactForm()
 
  if request.method == 'POST':

      msg = Message('Mensaje enviado a traves de www.gypnetwork.cl', sender=form.email.data, recipients=['gypnetwork.info@gmail.com'])
      msg.body = """\n
      Nombre: %s \ne-mail:  %s \nTelefono: %s \nMensaje: 
      %s
      """ % (form.nombre.data, form.email.data, form.telefono.data, form.message.data)
      mail.send(msg)
 
      return render_template('contacto.html', success=True)
 
  elif request.method == 'GET':
    return render_template('contacto.html', form=form)
 
if __name__ == '__main__':
  app.run(debug=True)
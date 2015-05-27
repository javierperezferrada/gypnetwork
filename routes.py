from flask import Flask, render_template, request, flash
from forms import ContactForm

app = Flask(__name__)
 
app.secret_key = 'development key'
 

 
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

@app.route('/contacto')
def contacto():
  return render_template('contacto.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
 
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      return 'Form posted.'
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form)
 
if __name__ == '__main__':
  app.run(debug=True)
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/admin/<nome>')
def admin(nome):
  return "bem vindo"

@app.route('/login/',methods = ['POST', 'GET'])
def login():
  if request.method =='POST':
    usuario = request.form['c_user']
    return redirect(url_for('admin',nome = usuario))

  else:
    usuario = request.args.get('c_user')
    return redirect(url_for('admin',nome = usuario))

@app.route('/login/')
def admin_index():
  return render_template('login.html')

if __name__ == '__main__':
  app.run('0.0.0.0')

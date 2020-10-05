from  flask import Flask, request, make_response, redirect, render_template
#Instancia
app = Flask(__name__)

todos = ['TODO 1', 'TODO 2', 'TODO 3']

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)
#Rutas
@app.route('/')
def index():
    user_ip = request.remote_addr # puede ver la ip del usuario que visita la pagina
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip',user_ip)

    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip' : user_ip, 
        'todos': todos,
    }

    return render_template('hello.html', **context)


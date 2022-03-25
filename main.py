from flask import Flask, jsonify, request, redirect, url_for, session, render_template, g, url_for
from flask_bootstrap import Bootstrap
import random, sqlite3
# Store data on 'g' object of Flask

app = Flask(__name__)
bootstrap = Bootstrap(app)


# App configuration, spec. in Debug mode 
app.config['DEBUG'] = True 
app.config['SECRET_KEY'] = 'SECRETKEYHERE'


@app.route('/', methods=['POST', 'GET'])
def home():

    if request.method == 'POST':
        k = request.form['keywords']
        if len(k) > 0:
            print('Method POST')
            return redirect(url_for('services', k = k ))
        
    #Averiguar como identificar espacios sin caracteres 
    else:
        print('Method GET')
        return render_template('home.html')


@app.route('/servicios', methods=['GET', 'POST'], defaults = { 'k' : 'default'})
@app.route('/servicios/<string:k>', methods=['GET', 'POST'])
def services(k):
    
    return render_template('services.html', k = k)


@app.route('/nosotros')
def about_us():
    return render_template('aboutus.html')

if __name__ == '__main__':
    app.run(debug=True)
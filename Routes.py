from flask import * #importamos todo de flask
app = Flask(__name__)

#RUTAS DE LA PAGINA

@app.route('/')
def index():
	return render_template('index.html')





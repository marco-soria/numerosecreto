from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    nombre_args = request.args.get('nombre', 'Marco Antonio')
    lista_monedas = ["soles", "dolares", "euros"]
    #monto_origen = request.args.get('monto_origen', '0')
    monto_destino = 0
    if request.method == 'POST':
        monto_origen = request.form['monto_origen']
        monto_destino = float(monto_origen) / 3.8
        monto_destino = round(monto_destino, 2)
    return render_template('index.html', nombre=nombre_args, monto_destino=monto_destino, monedas=lista_monedas)

app.run(debug=True)
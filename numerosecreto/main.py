from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Clave secreta para la sesión, puedes cambiarla a algo más seguro

numero_secreto = random.randint(1, 10)

@app.route('/', methods=['GET', 'POST'])
def adivina():
    if 'intentos_restantes' not in session:
        session['intentos_restantes'] = 3

    if request.method == 'POST':
        try:
            intento = int(request.form.get('numero', '0'))

            if 1 <= intento <= 10:
                if intento == numero_secreto:
                    mensaje = "¡Adivinaste!"
                    session.pop('intentos_restantes', None)  # Eliminar la variable de sesión
                else:
                    session['intentos_restantes'] -= 1
                    if session['intentos_restantes'] > 0:
                        mensaje = f"Fallaste. Te quedan {session['intentos_restantes']} intentos."
                    else:
                        mensaje = f"Perdiste. El número secreto era {numero_secreto}."
                        session.pop('intentos_restantes', None)  # Eliminar la variable de sesión
            else:
                mensaje = "Ingresa un número entre 1 y 10."
        except ValueError:
            mensaje = "Ingresa un número entero válido."

    else:
        mensaje = None

    return render_template('index.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)



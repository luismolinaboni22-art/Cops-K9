from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Usuario quemado para prueba
USERS = {
    "CoordinadorHolcim": "123"
}

# Memoria temporal para visitantes
VISITORS = []


# ------------------------
#       LOGIN
# ------------------------
@app.route("/")
def login():
    return render_template("login.html")


@app.route("/auth", methods=["POST"])
def auth():
    username = request.form.get("username")
    password = request.form.get("password")

    if username in USERS and USERS[username] == password:
        return redirect(url_for("home"))

    return render_template("login.html", error="Credenciales incorrectas")


# ------------------------
#   PÁGINA PRINCIPAL
# ------------------------
@app.route("/home")
def home():
    return render_template("home.html")


# ------------------------
#   REGISTRO DE VISITANTES
# ------------------------
@app.route("/registro", methods=["GET", "POST"])
def registro():

    if request.method == "POST":
        nombre = request.form["nombre"]
        cedula = request.form["cedula"]
        empresa = request.form["empresa"]
        responsable = request.form["responsable"]
        placa = request.form["placa"]
        motivo = request.form["motivo"]
        hora_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        visitante = {
            "nombre": nombre,
            "cedula": cedula,
            "empresa": empresa,
            "responsable": responsable,
            "placa": placa,
            "motivo": motivo,
            "hora_ingreso": hora_ingreso,
            "hora_salida": None
        }

        VISITORS.append(visitante)

        return render_template("visitor_success.html", visitante=visitante)

    # ➜ CONTAR VISITANTES DENTRO
    cantidad_dentro = sum(1 for v in VISITORS if v["hora_salida"] is None)

    return render_template("visitor_form.html", visitors=VISITORS, cantidad_dentro=cantidad_dentro)



# ------------------------
#     REGISTRAR SALIDA
# ------------------------
@app.route("/salida/<int:index>")
def salida(index):
    VISITORS[index]["hora_salida"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return redirect(url_for("registro"))


# ------------------------
#       RUN LOCAL
# ------------------------
if __name__ == "__main__":
    app.run(debug=True)

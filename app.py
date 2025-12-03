from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# ------------------------
#   USUARIOS
# ------------------------
USERS = {
    "CoordinadorHolcim": "123"
}

# ------------------------
#   MEMORIAS TEMPORALES
# ------------------------
VISITORS = []
CONTRACTORS = []
PROVIDERS = []

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
        visitante = {
            "nombre": request.form["nombre"],
            "cedula": request.form["cedula"],
            "empresa": request.form["empresa"],
            "responsable": request.form["responsable"],
            "placa": request.form["placa"],
            "motivo": request.form["motivo"],
            "hora_ingreso": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "hora_salida": None
        }

        VISITORS.append(visitante)

        return render_template("visitor_success.html", visitante=visitante)

    return render_template("visitor_form.html", visitors=VISITORS)


@app.route("/salida/<int:index>")
def salida(index):
    VISITORS[index]["hora_salida"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return redirect(url_for("registro"))


# ------------------------
#   REGISTRO DE CONTRATISTAS
# ------------------------
@app.route("/contratistas", methods=["GET", "POST"])
def contratistas():

    if request.method == "POST":
        contratista = {
            "nombre": request.form["nombre"],
            "cedula": request.form["cedula"],
            "empresa": request.form["empresa"],
            "responsable": request.form["responsable"],
            "hora_ingreso": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "hora_salida": None
        }

        CONTRACTORS.append(contratista)

        return render_template("contractor_success.html", contratista=contratista)

    return render_template("contractor_form.html", contractors=CONTRACTORS)


@app.route("/salida_contratista/<int:index>")
def salida_contratista(index):
    CONTRACTORS[index]["hora_salida"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return redirect(url_for("contratistas"))


# ------------------------
#   REGISTRO DE PROVEEDORES
# ------------------------
@app.route("/proveedores", methods=["GET", "POST"])
def proveedores():

    if request.method == "POST":
        proveedor = {
            "nombre": request.form["nombre"],
            "cedula": request.form["cedula"],
            "empresa": request.form["empresa"],
            "responsable": request.form["responsable"],
            "motivo": request.form["motivo"],
            "hora_ingreso": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "hora_salida": None
        }

        PROVIDERS.append(proveedor)

        return render_template("provider_success.html", proveedor=proveedor)

    return render_template("provider_form.html", providers=PROVIDERS)


@app.route("/salida_proveedor/<int:index>")
def salida_proveedor(index):
    PROVIDERS[index]["hora_salida"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return redirect(url_for("proveedores"))
# ------------------------
#       REPORTES
# ------------------------
@app.route("/reportes", methods=["GET"])
def reportes():
    return render_template(
        "reportes.html",
        visitantes=VISITORS,
        contratistas=CONTRACTORS,
        proveedores=PROVIDERS
    )


# ------------------------
#       RUN LOCAL
# ------------------------
if __name__ == "__main__":
    app.run(debug=True)



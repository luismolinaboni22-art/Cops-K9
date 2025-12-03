# Memoria temporal para proveedores
PROVIDERS = []


# ------------------------
#   REGISTRO DE PROVEEDORES
# ------------------------
@app.route("/proveedores", methods=["GET", "POST"])
def proveedores():

    if request.method == "POST":
        nombre = request.form["nombre"]
        cedula = request.form["cedula"]
        empresa = request.form["empresa"]
        responsable = request.form["responsable"]
        motivo = request.form["motivo"]
        hora_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        proveedor = {
            "nombre": nombre,
            "cedula": cedula,
            "empresa": empresa,
            "responsable": responsable,
            "motivo": motivo,
            "hora_ingreso": hora_ingreso,
            "hora_salida": None
        }

        PROVIDERS.append(proveedor)

        return render_template("provider_success.html", proveedor=proveedor)

    return render_template("provider_form.html", providers=PROVIDERS)


# ------------------------
#     REGISTRAR SALIDA PROVEEDOR
# ------------------------
@app.route("/salida_proveedor/<int:index>")
def salida_proveedor(index):
    PROVIDERS[index]["hora_salida"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return redirect(url_for("proveedores"))


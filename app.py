# ---------------------------------------------------
# FORMULARIO DE REGISTRO
# ---------------------------------------------------
@app.route('/contact_form', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        nuevo = Contact(
            nombre=request.form['nombre'],
            extension=request.form['extension'],
            canal_radio=request.form['canal_radio'],
            correo=request.form['correo']
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('contact_list'))
    return render_template('contact_form.html')


# ---------------------------------------------------
# LISTA DE CONTACTOS + BÚSQUEDA
# ---------------------------------------------------
@app.route('/contact_list')
def contact_list():
    query = request.args.get("q", "")
    if query:
        contactos = Contact.query.filter(
            (Contact.nombre.ilike(f"%{query}%")) |
            (Contact.extension.ilike(f"%{query}%"))
        ).all()
    else:
        contactos = Contact.query.all()

    return render_template("contact_list.html", contactos=contactos, q=query)


# ---------------------------------------------------
# EDITAR
# ---------------------------------------------------
@app.route("/contact_edit/<int:id>", methods=["GET", "POST"])
def contact_edit(id):
    contacto = Contact.query.get_or_404(id)

    if request.method == "POST":
        contacto.nombre = request.form['nombre']
        contacto.extension = request.form['extension']
        contacto.canal_radio = request.form['canal_radio']
        contacto.correo = request.form['correo']

        db.session.commit()
        return redirect(url_for("contact_list"))

    return render_template("contact_edit.html", contacto=contacto)


# ---------------------------------------------------
# ELIMINAR
# ---------------------------------------------------
@app.route("/contact_delete/<int:id>")
def contact_delete(id):
    contacto = Contact.query.get_or_404(id)
    db.session.delete(contacto)
    db.session.commit()
    return redirect(url_for("contact_list"))


# ---------------------------------------------------
# EXPORTAR A EXCEL
# ---------------------------------------------------
@app.route('/contact_export_excel')
def contact_export_excel():
    contactos = Contact.query.all()

    df = pd.DataFrame([
        [c.nombre, c.extension, c.canal_radio, c.correo]
        for c in contactos
    ], columns=['Nombre', 'Extensión', 'Canal Radio', 'Correo'])

    file_path = "contactos.xlsx"
    df.to_excel(file_path, index=False)

    return send_file(file_path, as_attachment=True)


# ---------------------------------------------------
# EXPORTAR A PDF
# ---------------------------------------------------
from reportlab.pdfgen import canvas

@app.route('/contact_export_pdf')
def contact_export_pdf():
    contactos = Contact.query.all()
    file_path = "contactos.pdf"

    c = canvas.Canvas(file_path)
    y = 800

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Lista de Contactos")
    y -= 40

    c.setFont("Helvetica", 10)

    for cont in contactos:
        c.drawString(50, y, 
            f"{cont.nombre} | Ext: {cont.extension} | Radio: {cont.canal_radio} | {cont.correo}"
        )
        y -= 20
        if y < 50:
            c.showPage()
            y = 800

    c.save()

    return send_file(file_path, as_attachment=True)




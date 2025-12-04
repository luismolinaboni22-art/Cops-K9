from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
from models import db, User, Visitor, Contractor, Provider
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


# -----------------------
# LOGIN
# -----------------------
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()

        if user and user.check_password(request.form['password']):
            session['user'] = user.username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Credenciales incorrectas")

    return render_template('login.html')


# -----------------------
# LOGOUT
# -----------------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# -----------------------
# HOME CON CONTADORES
# -----------------------
@app.route('/home')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))

    visitantes_dentro = Visitor.query.filter_by(hora_salida=None).count()
    contratistas_dentro = Contractor.query.filter_by(hora_salida=None).count()
    proveedores_dentro = Provider.query.filter_by(hora_salida=None).count()

    return render_template(
        'home.html',
        visitantes_dentro=visitantes_dentro,
        contratistas_dentro=contratistas_dentro,
        proveedores_dentro=proveedores_dentro
    )


# -----------------------
# REGISTRO VISITANTES
# -----------------------
@app.route('/visitor', methods=['GET', 'POST'])
def visitor_form():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        nuevo = Visitor(
            nombre=request.form['nombre'],
            cedula=request.form['cedula'],
            empresa=request.form['empresa'],
            persona_visita=request.form['persona_visita'],
            motivo=request.form['motivo'],
            placa=request.form['placa'],
            hora_ingreso=datetime.now()
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('visitor_success'))

    return render_template('visitor_form.html')


@app.route('/visitor_success')
def visitor_success():
    return render_template('visitor_success.html')


# -----------------------
# REPORTES (INGRESO + SALIDA)
# -----------------------
@app.route('/reportes')
def reportes():
    visitantes = Visitor.query.all()
    contratistas = Contractor.query.all()
    proveedores = Provider.query.all()

    return render_template(
        'reportes.html',
        visitantes=visitantes,
        contratistas=contratistas,
        proveedores=proveedores
    )


# -----------------------
# MAIN
# -----------------------
if __name__ == "__main__":
    app.run(debug=True)



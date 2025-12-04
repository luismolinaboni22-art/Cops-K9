<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Panel Principal - Holcim</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #eef2f5;
            margin: 0;
        }

        .top-bar {
            background: #003e70;
            padding: 15px;
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .dashboard {
            display: flex;
            justify-content: center;
            margin-top: 40px;
            gap: 25px;
        }

        .card {
            background: white;
            width: 260px;
            padding: 25px;
            border-radius: 14px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.15);
            text-align: center;
        }

        .card h2 {
            margin: 0;
            font-size: 38px;
            color: #003e70;
        }

        .card p {
            font-size: 18px;
            margin-top: 10px;
            font-weight: bold;
            color: #555;
        }

        .btn-menu {
            display: block;
            width: 300px;
            margin: 40px auto;
            padding: 15px;
            background: #005baa;
            color: white;
            text-align: center;
            border-radius: 8px;
            font-weight: bold;
            text-decoration: none;
            transition: 0.3s;
        }

        .btn-menu:hover {
            background: #004682;
        }

        .logout-btn {
            background: red;
            color: white;
            padding: 10px 18px;
            border-radius: 6px;
            text-decoration: none;
            font-weight: bold;
        }

        .logout-btn:hover {
            background: #a30000;
        }
    </style>
</head>

<body>

    <div class="top-bar">
        <div>Sistema Holcim Costa Rica</div>
        <a class="logout-btn" href="/logout">Cerrar Sesión</a>
    </div>

    <div class="dashboard">

        <div class="card">
            <h2>{{ visitantes_dentro }}</h2>
            <p>Visitantes dentro</p>
        </div>

        <div class="card">
            <h2>{{ contratistas_dentro }}</h2>
            <p>Contratistas dentro</p>
        </div>

        <div class="card">
            <h2>{{ proveedores_dentro }}</h2>
            <p>Proveedores dentro</p>
        </div>

    </div>

    <a class="btn-menu" href="/visitor">Registrar Visitante</a>
    <a class="btn-menu" href="/reportes">Reportes Históricos</a>

</body>
</html>


# 🌐 FABRICA_API

Este proyecto crea un entorno automatizado en Docker que simula un sistema de producción en tres fábricas, con múltiples entornos de bases de datos (DEV, PROD, PRE-PROD, SIT), una API REST, servidor Apache y automatización con crontab.

---

## 🧱 Arquitectura

```
Docker Compose levanta los siguientes servicios:

📦 API Flask (Puerto 5050)
📦 MySQL (PROD, DEV, PRE-PROD, SIT)
📦 Apache con PHP (Puerto 8080)
📦 Cronjob que automatiza tareas entre contenedores
```

---

## ⚙️ Componentes

### 1. `/api`
API Flask con endpoint `/produccion` que devuelve datos estáticos de producción diaria.

### 2. `/mysql/init.sql`
Script que crea la tabla `produccion` automáticamente en cada base de datos.

### 3. `/cron`
Contenedor que ejecuta:
- `script_insert.py`: lee de la API e inserta en `mysql_prod` y `mysql_dev`
- `script_sync.py`: sincroniza datos de `mysql_prod` hacia `mysql_sit` a las 19:00

### 4. `/apache`
Servidor Apache + PHP que consulta y muestra los datos insertados en `mysql_prod`.

---

## 🚀 Cómo usar

1. Clona el repo:
```bash
git clone https://github.com/tu-usuario/fabrica_api.git
cd fabrica_api
```

2. Levanta los servicios:
```bash
docker compose up --build
```

3. Accede a los servicios:
- API Flask: [http://localhost:5050/produccion](http://localhost:5050/produccion)
- Apache Web: [http://localhost:8080](http://localhost:8080)

---

## 📝 Licencia

Distribuido bajo licencia [GNU General Public License v3.0](LICENSE).
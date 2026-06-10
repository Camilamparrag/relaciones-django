# Modulo 7 Leccion 3

# Relaciones-django

Proyecto Django que demuestra los tres tipos de relaciones entre modelos de base de datos: uno a muchos (1:N), muchos a muchos (M:N) y uno a uno (1:1).

## Pasos realizados

### 1. Entorno con Docker
Se creó un archivo `docker-compose.yml` con dos servicios:
- **PostgreSQL 17**: base de datos `relaciones_db`, usuario `usuario`, contraseña `1234`, puerto `5432`
- **pgAdmin4**: interfaz gráfica en `http://localhost:5050` (email: `admin@admin.com`, password: `admin`)

### 2. Creación del proyecto y app Django
```bash
django-admin startproject config .
python manage.py startapp relaciones
```

### 3. Configuración de la base de datos
En `config/settings.py` se configuró PostgreSQL como motor de base de datos y se agregó `relaciones` a `INSTALLED_APPS`.

### 4. Definición de modelos
En `relaciones/models.py` se crearon tres pares de modelos que cubren los tres tipos de relaciones:

| Relación | Modelo A | Modelo B | Campo de relación |
|---|---|---|---|
| 1 a muchos (ForeignKey) | `Categoria` | `Producto` | `categoria = ForeignKey(Categoria, on_delete=CASCADE)` |
| Muchos a muchos (ManyToManyField) | `Curso` | `Estudiante` | `curso = ManyToManyField(Curso)` |
| 1 a 1 (OneToOneField) | `Usuario` | `Perfil` | `usuario = OneToOneField(Usuario, on_delete=CASCADE)` |

### 5. Migraciones
Se generaron y aplicaron las migraciones para propagar los modelos a PostgreSQL:
```bash
python manage.py makemigrations
python manage.py migrate
```

Esto creó 3 migraciones:
- `0001_initial` → Categoria y Producto
- `0002_curso_estudiante` → Curso y Estudiante
- `0003_usuario_perfil` → Usuario y Perfil

### 6. Registro en el admin
Los 6 modelos se registraron en `relaciones/admin.py` para poder gestionarlos desde el panel de administración de Django (`/admin/`).

### 7. Consultas ORM
Se implementaron vistas de ejemplo en `relaciones/views.py` con consultas ORM que demuestran:
- Creación de registros con `get_or_create()`
- Filtros por campos relacionados (`filter(categoria__nombre=...)`)
- Navegación de relaciones directas e inversas (`producto.categoria`, `categoria.producto_set.all()`)
- Relaciones muchos a muchos (`estudiante.curso.all()`, `curso.estudiante_set.all()`)
- Relaciones uno a uno (`perfil.usuario`, `usuario.perfil`)




![ORM](/img/m7_l3.png)
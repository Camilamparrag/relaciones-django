from django.http import JsonResponse
from .models import Categoria, Producto, Curso, Estudiante, Usuario, Perfil


def consultas_orm(request):
    resultados = {}

    # --- RELACIÓN 1 A MUCHOS (Categoria → Producto) ---
    cat1, _ = Categoria.objects.get_or_create(nombre="Electrónica")
    cat2, _ = Categoria.objects.get_or_create(nombre="Ropa")

    Producto.objects.get_or_create(nombre="Teléfono", precio=500, categoria=cat1)
    Producto.objects.get_or_create(nombre="Laptop", precio=1000, categoria=cat1)
    Producto.objects.get_or_create(nombre="Camiseta", precio=20, categoria=cat2)

    productos_electronica = Producto.objects.filter(categoria__nombre="Electrónica")
    resultados["productos_electronica"] = [
        {"nombre": p.nombre, "precio": p.precio} for p in productos_electronica
    ]

    productos_de_cat1 = cat1.producto_set.all()
    resultados["productos_de_categoria"] = [
        {"nombre": p.nombre, "precio": p.precio} for p in productos_de_cat1
    ]

    # --- RELACIÓN MUCHOS A MUCHOS (Curso ↔ Estudiante) ---
    curso1, _ = Curso.objects.get_or_create(nombre="Matemáticas")
    curso2, _ = Curso.objects.get_or_create(nombre="Historia")

    est1, _ = Estudiante.objects.get_or_create(nombre="Ana")
    est2, _ = Estudiante.objects.get_or_create(nombre="Carlos")

    est1.curso.add(curso1, curso2)
    est2.curso.add(curso1)

    resultados["cursos_ana"] = [c.nombre for c in est1.curso.all()]
    resultados["estudiantes_mate"] = [e.nombre for e in curso1.estudiante_set.all()]

    # --- RELACIÓN 1 A 1 (Usuario → Perfil) ---
    user1, _ = Usuario.objects.get_or_create(nombre="Juan")
    user2, _ = Usuario.objects.get_or_create(nombre="María")

    Perfil.objects.get_or_create(bio="Desarrollador web", usuario=user1)
    Perfil.objects.get_or_create(bio="Diseñadora gráfica", usuario=user2)

    perfil_juan = Perfil.objects.get(usuario=user1)
    resultados["perfil_juan"] = perfil_juan.bio

    usuario_del_perfil = Usuario.objects.get(perfil=perfil_juan)
    resultados["usuario_del_perfil"] = usuario_del_perfil.nombre

    return JsonResponse(resultados, json_dumps_params={"indent": 2, "ensure_ascii": False})

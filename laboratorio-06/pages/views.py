from django.shortcuts import render


def home(request):
    context = {
        "welcome_message": "Un espacio sencillo para encontrar recursos y continuar aprendiendo.",
        "featured_topics": ["Python", "Git y GitHub", "Desarrollo web"],
    }
    return render(request, "pages/home.html", context)


def resources(request):
    context = {
        "resources": [
            {
                "title": "Fundamentos de Python",
                "category": "Programación",
                "description": "Variables, tipos de datos, operadores y funciones.",
                "available": True,
            },
            {
                "title": "Git y GitHub",
                "category": "Colaboración",
                "description": "Versionado, ramas y seguimiento de cambios.",
                "available": True,
            },
            {
                "title": "Modelos de Django",
                "category": "Desarrollo web",
                "description": "Persistencia y relaciones para una etapa posterior.",
                "available": False,
            },
        ],
    }
    return render(request, "pages/resources.html", context)


def about(request):
    context = {
        "description": "ClassroomHub es una aplicación educativa construida con Django para practicar rutas, vistas y plantillas.",
        "technologies": ["Python", "Django", "HTML", "GitHub"],
    }
    return render(request, "pages/about.html", context)

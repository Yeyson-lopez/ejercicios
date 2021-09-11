from django.contrib import admin
from .models import Cliente, TipoCliente, Ventas, estudiante, docente, Grados, AcercaDe

# Register your models here.
admin.site.register(Cliente)
admin.site.register(TipoCliente)
admin.site.register(Ventas)
admin.site.register(estudiante)
admin.site.register(docente)
admin.site.register(Grados)
admin.site.register(AcercaDe)




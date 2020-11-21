from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
	path('contacto/',views.mostrarContacto ,name="mostrarContacto"),
    path('asesores/<int:id_region>/',views.mostrarAsesores ,name="mostrarAsesores"),
    path('asesor/<int:id>/',views.mostrarAsesor ,name="mostrarAsesor"),
    path('index/',views.mostrarIndex ,name="mostrarIndex"),
    path('nosotros/',views.mostrarNosotros ,name="mostrarNosotros"),
    path('servicios/',views.mostrarServicios ,name="mostrarServicios"),
    path('pago/<int:id>/',views.mostrarPago ,name="mostrarPago"),
    path('asesor/registrar/',views.registrarAsesor ,name="registrarAsesor"),
    path('region/registrar/',views.registrarRegion ,name="registrarRegion"),
    path('contrata/listar/',views.listarContrata ,name="listarContrata"),

    #API
    path('api/asesor/registrar/',views.registarAsesorAPI ,name="registrarAsesorAPI"),
    path('api/region/registrar/',views.registarRegionAPI ,name="registrarRegionAPI"),
    path('api/contrata/registrar/<int:id>/',views.registrarContrataAPI ,name="registrarContrataAPI"),

]

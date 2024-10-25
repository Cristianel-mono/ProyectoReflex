# ProyectoFinal/views/form_mapping.py
from ProyectoFinal.views.FormulariosProducto import bolsa_form, rollo_form, rolloProviAgro_form, servicio_form

# Mapeo de formularios según el tipo de producto
product_form_mapping = {
    "Bolsa": bolsa_form,
    "Rollo": rollo_form,
    "Rollo Proviagro": rolloProviAgro_form,
    "Servicio": servicio_form
}
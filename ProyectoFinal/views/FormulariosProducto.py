
import reflex as rx

from ProyectoFinal.components.form_field import form_field




# Función que se encarga de gestionar el estado de la selección de los usuarios
def ocultar_mostrar(label: str, field_name: str, field_component: rx.Component) -> rx.Component:
    # El estado ya está gestionado por Reflex automáticamente
    from ProyectoFinal.backend.backend import States_pagina
    checkbox = rx.checkbox(
        label=f"¿Desea ingresar {label}?",
        name=f"{field_name}_option",
        on_change=lambda value: States_pagina.set_is_checked(value),  # Utiliza el setter generado automáticamente
    )
    
    # Devuelve el componente con la checkbox y el campo condicional
    return rx.vstack(
        checkbox,
        rx.cond(States_pagina.is_checked, field_component),  # Reflex evalúa el estado con el getter automático
    )

# Función para el formulario de producto Bolsa 
def bolsa_form():
    return rx.vstack(
        rx.text("Creacion de referencia para Bolsas", weight="bold", size="xl"),
        rx.text(
            "Por favor complete los campos opcionales y selecione las caracteristicas del producto",
            italic=True,
            margin_botton="1em",
        ),

        rx.text("Selecciona los parámetros opcionales que desea agregar a su bolsa", weight="bold"),
        ocultar_mostrar("Fuelle Lateral", "fulleL", form_field("Fuelle Lateral", "Ingrese el fuelle Lateral", "number", "fuelle", "ruler")),
        ocultar_mostrar("Fuelle fondo", "fuelleF", form_field("Fuelle Fondo", "Ingrese el fuelle de Fondo", "number", "fuelle", "ruler")),
        ocultar_mostrar("Calibre", "calibre", form_field("Calibre", "Ingrese el calibre (mm)", "number", "calibre", "ruler")),
        ocultar_mostrar("Referencia", "referencia", form_field("Referencia", "Ingrese la referencia de la bolsa","text", "referencia", "ruler")),

        rx.text("Selecciona el material de su Bolsa"),
        rx.select(
            ["Aluminio", "Poliamida Bi-Orientada", "Polipropileno Bi-Orientado Mate",
             "Polipropileno Bi-Orientado Metalizado", "Polipropileno Bi-Orientado Perlado",
             "Polipropileno Bi-Orientado Transparente", "Polipropileno Cast", "EVOH Co-extruido",
             "Polipropileno Mono-Orientado", "Nylon Co-extruido", "Papel", "Polietileno de Alta Densidad", 
             "Polietileno de Alta Densidad Co-extruído", "Polietileno de Alta Densidad Corriente", 
             "Polietileno de Baja Densidad", "Polietileno de Baja Densidad Co-extruido", 
             "Polietileno de Baja Densidad Corriente", "Polietileno de Media Densidad", 
             "Polietileno de Media Densidad Co-extruído", "Poliéster Mate", "Poliéster Metalizado",
             "Poliéster Transparente", "Polipropileno Co-extruído", "Polietileno Stretch"],
            placeholder="Elije el material",
            name="material",
            required=True,
        ),
        rx.text("Seleccione el color"),
        rx.select(
            ["Amarillo", "Azul", "Blanco-Negro", "Blanco", "Naranja", "Negro", "Rojo",
             "Transparente", "Verde", "Blanco-Blanco", "Gris", "Plata-Negro"],
            placeholder="Elija el color",
            name="color",
            required=True,  
        ),
        form_field("Ancho (cm)", "Ingrese el Ancho", "number", "ancho", "ruler"),
        form_field("Largo (cm)" , "Ingrese el Largo", "number", "largo", "ruler"),
    )

def rollo_form():
    return rx.vstack(
        rx.text("Creacion de referencia para Rollos", weight="bold", size="xl"),
        rx.text(
            "Por favor complete los campos opcionales y selecione las caracteristicas del producto",
            italic=True,
            margin_botton="1em",
        ),


        rx.text("Selecciona los parámetros opcionales que desea agregar:", weight="bold"),
        ocultar_mostrar("Fuelle Lateral", "fulleL_R", form_field("Fuelle Lateral", "Ingrese el fuelle Lateral", "number", "fuelle_R", "ruler")),
        ocultar_mostrar("Calibre", "calibre_R", form_field("Calibre", "Ingrese el calibre (mm)","number", "calibre_R", "ruler")),
        ocultar_mostrar("Largo", "largo_R", form_field("Largo (cm)", "Ingrese el Largo (cm)", "number", "largo_R", "ruler")),
        ocultar_mostrar("Referencia", "referencia_R", form_field("Referencia", "Ingrese la referencia", "number", "referencia_R", "ruler")),

        rx.text("Selecciona el material de su Rollo"),
        rx.select(
            ["Aluminio", "Poliamida Bi-Orientada", "Polipropileno Bi-Orientado Mate",
             "Polipropileno Bi-Orientado Metalizado", "Polipropileno Bi-Orientado Perlado",
             "Polipropileno Bi-Orientado Transparente", "Polipropileno Cast", "EVOH Co-extruido",
             "Polipropileno Mono-Orientado", "Nylon Co-extruido", "Papel", "Polietileno de Alta Densidad", 
             "Polietileno de Alta Densidad Co-extruído", "Polietileno de Alta Densidad Corriente", 
             "Polietileno de Baja Densidad", "Polietileno de Baja Densidad Co-extruido", 
             "Polietileno de Baja Densidad Corriente", "Polietileno de Media Densidad", 
             "Polietileno de Media Densidad Co-extruído", "Poliéster Mate", "Poliéster Metalizado",
             "Poliéster Transparente", "Polipropileno Co-extruído", "Polietileno Stretch"],
            placeholder="Elije el material",
            name="material_R",
            required=True,
        ),
        rx.text("Seleccione el color"),
        rx.select(
            ["Amarillo", "Azul", "Blanco-Negro", "Blanco", "Naranja", "Negro", "Rojo",
             "Transparente", "Verde", "Blanco-Blanco", "Gris", "Plata-Negro"],
            placeholder="Elija el color",
            name="color_R",
            required=True,  
        ),
        rx.text("Seleccione el Tipo de Bobinado"),
        rx.select(
            ["Tubular", "Semitubular", "Lámina", "Lámina doble"],
            placeholder="Elija el tipo de bobinado",
            name="bobinado_R",
            required=True,
        ),
        form_field("Ancho (cm)", "Ingrese el Ancho", "number", "ancho_R", "ruler"),
    )

def rolloProviAgro_form():
    return rx.vstack(
         rx.text("Creacion de referencia para Rollos Proviagro", weight="bold", size="xl"),
        rx.text(
            "Por favor complete los campos opcionales y selecione las caracteristicas del producto",
            italic=True,
            margin_botton="1em",
        ),

        rx.text("Seleccione los parámetros del Rollo de la Línea Industrial", weight="bold"),
        rx.select(
            ["ROLLO PROVIAGRO ENERGY", "ROLLO PROVIAGRO BLACK", "ROLLO PROVIAGRO LUMINANCE", "ROLLO PROVIAGRO SPECTRUM"],
            placeholder="Elija el tipo de rollo",
            name="tipoRollo",
            required=True,
        ),
        rx.text("Seleccione el color"),
        rx.select(
            ["Amarillo", "Azul", "Blanco-Negro", "Blanco", "Naranja", "Negro", "Rojo",
             "Transparente", "Verde", "Blanco-Blanco", "Gris", "Plata-Negro"],
            placeholder="Elija el color",
            name="color_R",
            required=True,  
        ),
        form_field("Ancho (cm)", "Ingrese el Ancho", "number", "anchoRolloProviagro", "ruler"),
        form_field("Calibre (mm)", "Ingrese el Calibre", "number", "calibreRolloProviagro", "ruler"),
        form_field("Largo (cm)", "Ingrese el Largo", "number", "largo", "ruler"),
        rx.text("Seleccione el Tipo de Bobinado"),
        rx.select(
            ["Tubular", "Semitubular", "Lámina", "Lámina doble"],
            placeholder="Elija el tipo de bobinado",
            name="bobinadoRolloProviagro",
            required=True,
        ),
    )

def servicio_form():
    return rx.vstack(
         rx.text("Creacion de referencia para Servicios", weight="bold", size="xl"),
        rx.text(
            "Por favor complete los campos opcionales y selecione las caracteristicas del producto",
            italic=True,
            margin_botton="1em",
        ),

        rx.text("Seleccione el tipo de servicio que desea crear"),
        rx.select(
            ["Co-extrusión", "Corte", "Extrusión", "Maquila enfuellado", 
             "Impresión", "Laminación", "Peletizado", "Precorte", "Maquila precorte", 
             "Refilado", "Sellado", "Troquelado"],
            name="TipoServicio",
            required=True,
        ),
        ocultar_mostrar(
            label="Agregar otro servicio",
            field_name="TipoServicio2",
            field_component=rx.select(
                ["Co-extrusión", "Corte", "Extrusión", "Maquila enfuellado", 
                 "Impresión", "Laminación", "Peletizado", "Precorte", "Maquila precorte", 
                 "Refilado", "Sellado", "Troquelado"],
                name="TipoServicio2",
            )
        ),
         form_field("Informacion del Producto", "Ingrese la info", "text", "infoServicio", "ruler"),
    )


        
    
    
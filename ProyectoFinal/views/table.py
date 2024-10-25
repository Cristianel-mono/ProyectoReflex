import reflex as rx

from ProyectoFinal.views.FormulariosProducto import bolsa_form , rollo_form , rolloProviAgro_form , servicio_form
from ..backend.backend import States_pagina, Customer , product_types
from ..components.form_field import form_field
from ..components.status_badges import status_badge
from ..views.form_mapping import product_form_mapping
 
#Funcion para restaurar formulaior 
def base_form():
    return rx.fragment(
        # Selector para el tipo de producto
        rx.vstack(
            rx.select(
                product_types,  # Opciones de productos
                value=States_pagina.selected_product_type,
               on_change=lambda e: States_pagina.set_selected_product_type(str(e.target.value)),  # Asegurar string
            ),
            margin_bottom="1em",
        
        ),
        
        # Mostrar tipo de producto seleccionado
        rx.cond(
            States_pagina.selected_product_type != "",  
            rx.text(f"Tipo de producto seleccionado: {type(States_pagina.selected_product_type)}"), 
            rx.text("Seleccione un tipo de producto.", italic=True, color="gray")
        ),
        
        # Mostrar el formulario actual desde el backend
        rx.cond(
            States_pagina.selected_product_type != "",
            
            rx.form.root(
                States_pagina.selected_form,  # Renderiza el formulario desde el state
                rx.flex(
                    rx.form.submit(
                        rx.button("Enviar", color_scheme="blue"),
                        as_child=True,
                    ),
                    justify="space-between",
                    width="100%",
                    padding_top="1em",
                ),
                on_submit=States_pagina.add_customer_to_db,  
            ),
            rx.text("Seleccione un tipo de producto para continuar.", italic=True),  
        ),
        max_width="450px",
        padding="1.5em",
        border=f"2px solid {rx.color('accent', 7)}",
        border_radius="25px",
    )

   



def show_customer(user: Customer):
    """Show a customer in a table row."""

    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.phone),
        rx.table.cell(user.address),
        rx.table.cell(f"${user.payments:,}"),
        rx.table.cell(user.date),
        rx.table.cell(
            rx.match(
                user.status,
                ("Delivered", status_badge("Delivered")),
                ("Pending", status_badge("Pending")),
                ("Cancelled", status_badge("Cancelled")),
                status_badge("Pending"),
            )
        ),
        rx.table.cell(
            rx.hstack(
                update_customer_dialog(user),
                rx.icon_button(
                    rx.icon("trash-2", size=22),
                    on_click=lambda: States_pagina.delete_customer(getattr(user, "id")),
                    size="2",
                    variant="solid",
                    color_scheme="red",
                ),
            )
        ),
        style={"_hover": {"bg": rx.color("gray", 3)}},
        align="center",
    )

def add_customer_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Crear nueva Referencia", size="4", display=["none", "none", "block"]),
                size="3",
            ),
        ),
        rx.dialog.content(
            rx.hstack(  # para alinear horizontalmente
                rx.badge(
                    rx.icon(tag="file", size=34),  # Muestra el icono de documentos
                    color_scheme="grass",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(  # para alinear verticalmente
                    rx.dialog.title(
                        "Creación de una Nueva Referencia",  # Se configura el título
                        weight="bold",
                        margin="0",
                    ),
                    
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
            ),
            base_form(),  # Llama al formulario base
            max_width="450px",
            padding="1.5em",
            border=f"2px solid {rx.color('accent', 7)}",  # Corrección en las comillas
            border_radius="25px",
        )
    )


def update_customer_dialog(user):
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("square-pen", size=22),
                rx.text("Edit", size="3"),
                color_scheme="blue",
                size="2",
                variant="solid",
                on_click=lambda: States_pagina.get_user(user),
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="square-pen", size=34),
                    color_scheme="grass",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title(
                        "Edit Customer",
                        weight="bold",
                        margin="0",
                    ),
                    rx.dialog.description(
                        "Edit the customer's info",
                    ),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
            ),
            rx.flex(
                rx.form.root(
                    rx.flex(
                        # Name
                        form_field(
                            "Name",
                            "Customer Name",
                            "text",
                            "name",
                            "user",
                            user.name,
                        ),
                        # Email
                        form_field(
                            "Email",
                            "user@reflex.dev",
                            "email",
                            "email",
                            "mail",
                            user.email,
                        ),
                        # Phone
                        form_field(
                            "Phone",
                            "Customer Phone",
                            "tel",
                            "phone",
                            "phone",
                            user.phone,
                        ),
                        # Address
                        form_field(
                            "Address",
                            "Customer Address",
                            "text",
                            "address",
                            "home",
                            user.address,
                        ),
                        # Payments
                        form_field(
                            "Payment ($)",
                            "Customer Payment",
                            "number",
                            "payments",
                            "dollar-sign",
                            user.payments.to(str),
                        ),
                        # Status
                        rx.vstack(
                            rx.hstack(
                                rx.icon("truck", size=16, stroke_width=1.5),
                                rx.text("Status"),
                                align="center",
                                spacing="2",
                            ),
                            rx.radio(
                                ["Delivered", "Pending", "Cancelled"],
                                default_value=user.status,
                                name="status",
                                direction="row",
                                as_child=True,
                                required=True,
                            ),
                        ),
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancel",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Update Customer"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    on_submit=States_pagina.update_customer_to_db,
                    reset_on_submit=False,
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            max_width="450px",
            padding="1.5em",
            border=f"2px solid {rx.color('accent', 7)}",
            border_radius="25px",
        ),
    )


def _header_cell(text: str, icon: str):
    return rx.table.column_header_cell(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(text),
            align="center",
            spacing="2",
        ),
    )


def main_table():
    return rx.fragment(
        rx.flex(
            add_customer_button(),
            rx.spacer(),
            rx.cond(
                States_pagina.sort_reverse,
                rx.icon(
                    "arrow-down-z-a",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    on_click=States_pagina.toggle_sort,
                ),
                rx.icon(
                    "arrow-down-a-z",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    on_click=States_pagina.toggle_sort,
                ),
            ),
            rx.select(
                ["name", "email", "phone", "address", "payments", "date", "status"],
                placeholder="Sort By: Name",
                size="3",
                on_change=lambda sort_value: States_pagina.sort_values(sort_value),
            ),
            rx.input(
                rx.input.slot(rx.icon("search")),
                placeholder="Search here...",
                size="3",
                max_width="225px",
                width="100%",
                variant="surface",
                on_change=lambda value: States_pagina.filter_values(value),
            ),
            justify="end",
            align="center",
            spacing="3",
            wrap="wrap",
            width="100%",
            padding_bottom="1em",
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    _header_cell("Name", "user"),
                    _header_cell("Email", "mail"),
                    _header_cell("Phone", "phone"),
                    _header_cell("Address", "home"),
                    _header_cell("Payments", "dollar-sign"),
                    _header_cell("Date", "calendar"),
                    _header_cell("Status", "truck"),
                    _header_cell("Actions", "cog"),
                ),
            ),
            rx.table.body(rx.foreach(States_pagina.users, show_customer)),
            variant="surface",
            size="3",
            width="100%",
            on_mount=States_pagina.load_entries,
        ),
    )

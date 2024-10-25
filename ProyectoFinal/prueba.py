import reflex as rx

coins = ["BTC", "ETH", "LTC", "DOGE"]

class VarSelectState(rx.State):
    selected: str = "DOGE"

    # Método para actualizar el valor seleccionado
    def set_selected(self, value):
        self.selected = value
        print(f"Tipo de dato de selected_product_type en el backend: {type(self.selected)}")

@rx.page(route="/prueba", title="Prueba")
def var_operations_example():
    # Imprimir el tipo de dato del valor seleccionado en el frontend
    print(f"Tipo de dato de selected en el frontend: {type(VarSelectState.selected)}")
    
    return rx.vstack(
        rx.heading(
            "I just bought a bunch of " + VarSelectState.selected,
        ),
        rx.text(
            f"{VarSelectState.selected} is going to the moon!"
        ),
        rx.select(
            coins,
            value=VarSelectState.selected,
            on_change=VarSelectState.set_selected,  # Llama al método para cambiar el valor
        ),
        rx.text(f"Tipo de dato de selected: {type(VarSelectState.selected)}")  # Mostrar el tipo de dato
    )

import reflex as rx
from typing import Union
from sqlmodel import select, asc, desc, or_, func, cast, String
from datetime import datetime


def _get_percentage_change(value: Union[int, float], prev_value: Union[int, float]) -> float:
    percentage_change = (
        round(((value - prev_value) / prev_value) * 100, 2)
        if prev_value != 0
        else 0
        if value == 0
        else
        float("inf")
    )
    return percentage_change


class Customer(rx.Model, table=True):
    """The customer model."""

    name: str
    email: str
    phone: str
    address: str
    date: str
    payments: float
    status: str


class State(rx.State):
    """The app state."""

    users: list[Customer] = []
    sort_value: str = ""
    sort_reverse: bool = False
    search_value: str = ""
    current_user: Customer = Customer()

    def load_entries(self) -> list[Customer]:
        """Get all users from the database."""
        with rx.session() as session:
            query = select(Customer)
            if self.search_value:
                search_value = f"%{str(self.search_value).lower()}%"
                query = query.where(
                    or_(
                        *[
                            getattr(Customer, field).ilike(search_value)
                            for field in Customer.get_fields()
                            if field not in ["id", "payments"]
                        ],
                        cast(Customer.payments, String).ilike(search_value)
                    )
                )

            if self.sort_value:
                sort_column = getattr(Customer, self.sort_value)
                if self.sort_value == "payments":
                    order = desc(sort_column) if self.sort_reverse else asc(sort_column)
                else:
                    order = desc(func.lower(sort_column)) if self.sort_reverse else asc(func.lower(sort_column))
                query = query.order_by(order)

            self.users = session.exec(query).all()

    def sort_values(self, sort_value: str):
        self.sort_value = sort_value
        self.load_entries()

    def toggle_sort(self):
        self.sort_reverse = not self.sort_reverse
        self.load_entries()

    def filter_values(self, search_value):
        self.search_value = search_value
        self.load_entries()

    def get_user(self, user: Customer):
        self.current_user = user

    def add_customer_to_db(self, form_data: dict):
        self.current_user = form_data # Toma los valores ingresados
        self.current_user["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #Les agrega la fecha actual

        with rx.session() as session:
            if session.exec(
                select(Customer).where(Customer.email == self.current_user["email"])#Verifica si el cliente ya existe 
            ).first():
                return rx.window_alert("User with this email already exists")
            session.add(Customer(**self.current_user))
            session.commit()
        self.load_entries()
        return rx.toast.info(f"User {self.current_user['name']} has been added.", position="bottom-right")

    def update_customer_to_db(self, form_data: dict):
        self.current_user.update(form_data)
        with rx.session() as session:
            customer = session.exec(
                select(Customer).where(Customer.id == self.current_user["id"])
            ).first()
            for field in Customer.get_fields():
                if field != "id":
                    setattr(customer, field, self.current_user[field])
            session.add(customer)
            session.commit()
        self.load_entries()
        return rx.toast.info(f"User {self.current_user['name']} has been modified.", position="bottom-right")

    def delete_customer(self, id: int):
        """Delete a customer from the database."""
        with rx.session() as session:
            customer = session.exec(select(Customer).where(Customer.id == id)).first()
            session.delete(customer)
            session.commit()
        self.load_entries()
        return rx.toast.info(f"User {customer.name} has been deleted.", position="bottom-right")

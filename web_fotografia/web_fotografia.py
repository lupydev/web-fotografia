import reflex as rx

from .pages.contact import contact
from .pages.about import about
from .pages.index import index


app = rx.App()
app.add_page(index, route="/")
app.add_page(about, route="/sobre-mi")
app.add_page(contact, route="/contacto")

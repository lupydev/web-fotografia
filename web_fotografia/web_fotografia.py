import reflex as rx
import web_fotografia.styles.style as style
from .pages.contact import contact
from .pages.about import about
from .pages.index import index


app = rx.App(
    stylesheets=style.STYLESHEETS,
    style=style.BASE_STYLE,
)
app.add_page(index, route="/")
app.add_page(about, route="/sobre-mi")
app.add_page(contact, route="/contacto")

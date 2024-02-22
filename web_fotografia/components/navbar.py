import reflex as rx
from web_fotografia.styles.font import Font, FontWeight
import web_fotografia.styles.style as style


def navbar() -> rx.Component:
    return rx.box(
        rx.tablet_and_desktop(
            rx.hstack(
                rx.link(
                    rx.hstack(
                        rx.image(src="favicon.ico"),
                        rx.heading(
                            "Valentina Mopan",
                            font_family=Font.TITLE.value,
                            font_weight=FontWeight.BOLD.value,
                            color="#fff",
                        ),
                        align="center",
                    ),
                    href="/",
                ),
                rx.hstack(
                    rx.link(
                        "Sobre Mí",
                        href="/sobre-mi",
                    ),
                    rx.link(
                        "Contacto",
                        href="/contacto",
                    ),
                ),
                justify="between",
                align="center",
                style=style.navbar,
            ),
        ),
        # rx.mobile_only(
        #     rx.hstack(
        #         rx.link(
        #             rx.image(
        #                 src="favicon.ico",
        #             ),
        #             rx.heading("Valentina Mopan"),
        #             href="/",
        #         ),
        #         rx.button(
        #             rx.chakra.icon(
        #                 tag="hamburger",
        #             )
        #             # on_click=
        #         ),
        #         rx.drawer(),
        #     )
        # ),
        width="100%",
        z_index="999",
    )

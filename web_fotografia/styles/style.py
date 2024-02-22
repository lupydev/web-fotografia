import reflex as rx
from enum import Enum
from web_fotografia.styles.color import TextColor, Color
from web_fotografia.styles.font import Font, FontWeight

"""
Style convention
    1. Position
    2. Box model
    3. Typographic
    4. Visuals
    5. Miscelaneos
"""

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Tangerine:wght@700&display=swap"
]


class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    MIDDLE = "1.3em"
    LARGE = "1.5em"
    BIG = "2em"
    XL = "3em"
    VERY_BIG = "4em"
    HUGE = "6em"
    EXTREME_BIG = "8em"


BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "line_height": Size.LARGE.value,
    "color": TextColor.BODY.value,
    "background_color": Color.BACKGROUND.value,
    rx.link: {
        "font_weight": "bold",
        "color": TextColor.TITLE.value,
        "_hover": {
            "color": Color.SECUNDARY.value,
        },
    },
}

navbar = dict(
    max_width="64em",
    margin="0 auto",
    padding="1em 2em",
    border_bottom_left_radius=Size.DEFAULT.value,
    border_bottom_right_radius=Size.DEFAULT.value,
    bg=Color.PRIMARY.value,
)

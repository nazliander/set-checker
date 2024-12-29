from enum import StrEnum

from pydantic import BaseModel
from textual.app import ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Select


class Number(StrEnum):
    ONE = "1"
    TWO = "2"
    THREE = "3"


class Color(StrEnum):
    RED = "🔴"
    GREEN = "🟢"
    PURPLE = "🟣"


class Shape(StrEnum):
    DIAMOND = "<> - Diamond"
    SQUIGGLE = "~ - Squiggle"
    OVAL = "O - Oval"


class Shading(StrEnum):
    SOLID = "||| - Solid"
    STRIPED = "/// - Striped"
    OUTLINED = "--- - Outlined"


class Card(BaseModel):
    number: Number
    color: Color
    shape: Shape
    shading: Shading


class CardSelector(Container):
    def __init__(self, card_no: str):
        self.card_no = card_no
        super().__init__()

    def compose(self) -> ComposeResult:
        numbers = [(n.value, n.name) for n in Number]
        shapes = [(s.value, s.name) for s in Shape]
        colors = [(c.value, c.name) for c in Color]
        shadings = [(s.value, s.name) for s in Shading]

        yield Vertical(
            Select(numbers, id=f"number-select-{self.card_no}", prompt="Number"),
            Select(shapes, id=f"shape-select-{self.card_no}", prompt="Shape"),
            Select(colors, id=f"color-select-{self.card_no}", prompt="Color"),
            Select(shadings, id=f"shading-select-{self.card_no}", prompt="Shading"),
            id=f"card-selector-{self.card_no}",
            classes=f"card-selector-{self.card_no}",
        )


class CardHand(Container):
    """Widget displaying the selected cards."""

    def compose(self) -> ComposeResult:
        yield Horizontal(
            CardSelector(card_no="1"),
            CardSelector(card_no="2"),
            CardSelector(card_no="3"),
            id="card-hand",
            classes="card-hand",
        )

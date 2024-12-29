from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Footer, Header, Select

from set_checker.types import Card, CardHand, Color, Number, Shading, Shape


class SetChecker(App):
    """A card game application."""

    CSS = """
    Screen {
        align: center middle;
    }

    #card-container {
        height: auto;
        margin: 1;
        padding: 1;
    }

    .card-selector {
        width: 40;
        height: auto;
        padding: 1;
        border: solid gray;
    }

    Select {
        margin: 1;
    }

    Button {
        margin: 1;
        color: black;
        background: green;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Container(CardHand(), id="main-container")
        yield Container(Button("Check Set", id="check-set"))
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "check-set":
            self.check_set()

    def check_set(self) -> None:
        """Add a new card to the hand."""

        card_hand = self.query_one("#card-hand").children
        card_nodes = [_h.children for _v in card_hand for _h in _v.children]

        if any(_s.value == Select.BLANK for _n in card_nodes for _s in _n):
            self.notify("Please select all card attributes. Before checking for a set.")
            return

        cards = []

        for number, shape, color, shading in card_nodes:
            cards.append(
                Card(
                    number=Number[number.value],
                    shape=Shape[shape.value],
                    color=Color[color.value],
                    shading=Shading[shading.value],
                )
            )

        number_true = (cards[0].number == cards[1].number == cards[2].number) or (
            cards[0].number != cards[1].number != cards[2].number
        )
        color_true = (cards[0].color == cards[1].color == cards[2].color) or (
            cards[0].color != cards[1].color != cards[2].color
        )
        shape_true = (cards[0].shape == cards[1].shape == cards[2].shape) or (
            cards[0].shape != cards[1].shape != cards[2].shape
        )
        shading_true = (cards[0].shading == cards[1].shading == cards[2].shading) or (
            cards[0].shading != cards[1].shading != cards[2].shading
        )

        if number_true and color_true and shape_true and shading_true:
            self.notify("Set!")
        else:
            self.notify("Not a set.")


def main():
    app = SetChecker()
    app.run()


if __name__ == "__main__":
    main()

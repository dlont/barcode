import typer

from typing import Optional

app = typer.Typer()


@app.command()
def barcode(text: str, out: str, print_text: Optional[bool] = True):
    print(f"Text: {text}")

    import barcode
    barcode.base.Barcode.default_writer_options['write_text'] = print_text

    from barcode import Code128
    from barcode.writer import SVGWriter

    # Or to an actual file:
    with open(f"{out}.svg", "wb") as f:
        Code128(text, writer=SVGWriter()).write(f)



if __name__ == "__main__":
    app()

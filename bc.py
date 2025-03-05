import typer

from typing import Optional

app = typer.Typer()


@app.command()
def barcode(text: str,
            out: str,
            print_text: Optional[bool] = True,
            ext: Optional[str] = 'svg',
            height: Optional[float] = 5.0):
    print(f"Text: {text}")

    # Set writer options to customize barcode appearance
    # writer_options = {
    #     "module_height": height,  # Height of the barcode modules (the bars)
    #     "module_width": 0.2,      # Width of each barcode module (optional)
    #     "quiet_zone": 6.5,        # Margin around the barcode (optional)
    #     "font_size": 10,          # Font size for the human-readable text (optional)
    #     "text_distance": 5.0,     # Distance between the barcode and text (optional)
    #     "background": "white",    # Background color (optional)
    #     "foreground": "black",    # Barcode color (optional)
    # }

    import barcode
    barcode.base.Barcode.default_writer_options['write_text'] = print_text
    barcode.base.Barcode.default_writer_options['module_height'] = height

    from barcode import Code128
    from barcode.writer import SVGWriter, ImageWriter

    writer = SVGWriter()
    if ext == 'png': writer = ImageWriter()
    with open(f"{out}.{ext}", "wb") as f:
        Code128(text, writer=writer).write(f)



if __name__ == "__main__":
    app()

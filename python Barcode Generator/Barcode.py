import barcode
from barcode.writer import ImageWriter
from PIL import Image


def generate_and_save_barcode(text, filename='barcode'):
    code=barcode.get('code128',text,writer=ImageWriter())
    full_filename=f'{filename}.png'
    code.save(full_filename)

    return full_filename


barcode_text="Iman's barcode generator"
generated_filename=generate_and_save_barcode(barcode_text)
print(f'Barcode generated and saved as:{generated_filename}')
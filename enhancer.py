from PIL import Image
from io import BytesIO

def enhance_image(input_bytes):
    # Baca gambar dari byte input
    input_io = BytesIO(input_bytes)
    img = Image.open(input_io)

    # Contoh enhance: resize 2x (simulasi)
    img = img.resize((img.width * 2, img.height * 2))

    # Simpan hasil ke memori
    output_io = BytesIO()
    img.save(output_io, format='PNG')
    output_io.seek(0)

    return output_io, 'image/png'

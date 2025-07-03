import cv2
import numpy as np
from PIL import Image
from io import BytesIO

# Load model enhancer sekali saja
sr = cv2.dnn_superres.DnnSuperResImpl_create()
sr.readModel("EDSR_x2.pb")
sr.setModel("edsr", 2)  # Model EDSR dengan scale 2x

def enhance_image(input_bytes):
    input_io = BytesIO(input_bytes)
    img = Image.open(input_io).convert("RGB")
    img_np = np.array(img)

    result = sr.upsample(img_np)

    out_img = Image.fromarray(result)
    output_io = BytesIO()
    out_img.save(output_io, format='PNG')
    output_io.seek(0)

    return output_io, 'image/png'

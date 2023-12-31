import cv2
from pyzbar.pyzbar import decode
import numpy as np

def decode_and_print_qrcode(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Decode QR code
    decoded_objects = decode(image)
    code= []
    # Print the decoded information
    for obj in decoded_objects:
        code.append(f'Type: {obj.type}, Data: {obj.data.decode("utf-8")}')
    return "".join(code)
print(decode_and_print_qrcode('C:/Users/ramac/Desktop/collegeproject/static/qr_code_Ramachandra2.png'))

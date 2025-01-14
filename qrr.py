import qrcode
from PIL import Image

# Replace with the URL of your hosted webpage
webpage_url = "https://bilalo96.github.io/tarek/"

# Generate the QR code
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(webpage_url)
qr.make(fit=True)

# Save the QR code as an image
qr_img = qr.make_image(fill_color="black", back_color="white")
qr_img.save("contact_page_qr.png")
print("QR Code saved as 'contact_page_qr.png'")

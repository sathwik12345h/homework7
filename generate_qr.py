import qrcode

# Replace this with your actual GitHub profile URL
github_url = "https://github.com/sathwik12345h"

# Create a QR Code instance
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(github_url)
qr.make(fit=True)

# Create the image
img = qr.make_image(fill="black", back_color="white")

# Save the image
img.save("github_qr.png")
print("QR Code saved as github_qr.png")
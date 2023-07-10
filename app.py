import streamlit as st
import qrcode
from io import BytesIO

def generate_qr_code(url):
    qr = qrcode.QRCode(version=1, box_size=5, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    qr_image = qr.make_image(fill="black", back_color="white")
    qr_byte_io = BytesIO()
    qr_image.save(qr_byte_io, format='PNG')
    return qr_byte_io

def main():
    st.title("URL to QR Code Converter")
    st.write("Enter a URL and click the 'Generate QR Code' button to get the corresponding QR code image.")

    url = st.text_input("Enter the URL:")
    if st.button("Generate QR Code"):
        if url:
            qr_byte_io = generate_qr_code(url)
            st.image(qr_byte_io, caption="QR Code", use_column_width=True)
        else:
            st.warning("Please enter a URL.")

if __name__ == "__main__":
    main()







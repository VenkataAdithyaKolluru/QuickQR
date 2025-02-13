# Overview
This project is a simple web application that generates QR codes for given links. Users can input a link and select the color of the QR code. The application is built using Flask, a lightweight web framework for Python, and the qrcode library for generating QR codes.
# Structure
qr-code-generator
├── templates
│   ├── index.html
│   └── qr_code.html
├── static
│   └── MyQRCode.png (this will be generated after running the app)
├── app.py
├── requirements.txt
└── README.md

# Usage
Open the web application in your browser.
Enter the link you want to encode in the QR code.
Select the color for the QR code.
Click the "Generate QR Code" button.
The generated QR code will be displayed on a new page.

## Requirements

Install the required libraries using:

```bash
pip install -r requirements.txt

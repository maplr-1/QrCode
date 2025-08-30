QR Code Generator & Decoder

This project provides two simple Python utilities:
1. **QR Code Generator** – Create QR codes from any text and save them as images.
2. **QR Code Decoder** – Read and decode text/data from existing QR code images.

---

Features
- Generate QR codes from any input text.
- Save QR codes in `.png` format.
- Option to store QR codes in a **default folder (`QrCodes/`)** or a **custom path**.
- Decode and extract text from existing QR code images in a given folder.
- Simple command-line interaction.
- Only Read from **default folder (`QrCodes/`)** 

---


Requirements
Make sure you have Python **3.8+** installed.

Install the required libraries:
```bash
pip install qrcode pillow pyzbar
```
Additionally, pyzbar requires the zbar library:

 Linux (Arch/Manjaro):
    
    sudo pacman -S zbar

Ubuntu/Debian: 
    
    sudo apt install libzbar0
    
MacOS: 
   
    brew install zbar

Windows: 
    Install ZBar binaries from ZBar project

---

Usage
Generate a QR Code

Run the generator script:

python qr_generator.py

Follow the prompts:

    Enter a file name.

    Enter the text you want to encode.

    Choose where to save (QrCodes folder or a custom location).

The QR code will be saved as a .png file.

---

Decode QR Codes
Run the decoder script:

python qr_decoder.py

It will:

Look for all .png files in the QrCodes/ folder.

Decode and print the text stored in each QR code.

Example output:

 ./QrCodes/example.png
 Data: https://example.com

---

Notes

Always make sure the QrCodes/ directory exists before running.

Only .png files are scanned by the decoder.

KeyboardInterrupt (Ctrl+C) gracefully exits the generator script.

---

Example

Generate a QR code with text:

Enter The File Name: mylink
Enter The text Which You Want To Make Into a Qrcode:
example

Where to Store The QrCode Image:

1.default(QrCodes)
2.selected location

Choose(1 OR 2): 1

File saved as QrCodes/example.png

Decode all QR codes in the folder:

    ./QrCodes/example.png
    Data: example

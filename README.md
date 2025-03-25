# johnny603_qrCreate
Made with qrcode, tkinter, and Python; Thanks to codedex.io

# QR Code Generator with Tkinter
This Python program allows users to generate customizable QR codes by entering a website link and selecting various styles (fill color, background color, box size, and border size). Users can also generate multiple QR codes for predefined websites.

### Prerequisites
Python 3.x (recommended: Python 3.7 or above)

qrcode library: Install it with the following command:
```
pip install qrcode[pil]
```

tkinter library: Tkinter is usually included with Python. If it’s missing, install it with:
```
pip install tk
```


### How to Use the QR Code Generator
1. Running the Program
Clone or download the Python script file to your local machine.

Make sure all dependencies are installed (as mentioned in the prerequisites section).

Run the Python script in your terminal or your IDE (like PyCharm, VSCode, etc.).

2. Input Fields
Once the application window opens, you will see the following input fields:

Enter Website Link:

This is where you input the website URL you want to generate a QR code for.

```
Example: https://www.google.com
```

Fill Color:

Specify the color you want the QR code to have. The input must be a valid color name or hexadecimal color code.

```
Example: "blue", "#ff5733", "green"
```

Background Color:

Specify the background color of the QR code. This also accepts valid color names or hex codes.

```
Example: "white", "#ffffff", "yellow"
```

Box Size:

Define the size of each box in the QR code grid (higher values mean larger boxes).

```
Example: 4
```

Border Size:

Specify the width of the QR code’s border. A typical value is 4, but you can adjust it.

```
Example: 10
```

3. Generating a QR Code
Generate QR Code:

After filling out the input fields, click the "Generate QR Code" button to create the QR code.

The QR code will be displayed in the default image viewer, and a success message will appear, confirming the QR code has been saved as generated_qr.png in the same directory as the script.

4. Generating Multiple QR Codes
Generate Multiple QR Codes:

If you want to generate QR codes for several predefined websites (like YouTube, Google, GitHub), click the "Generate Multiple QR Codes" button.

This will automatically generate QR codes for the websites: https://youtu.be/U6rV-wZ2qlw, https://www.google.com, and https://www.github.com. Each QR code will be saved with a filename like qrcode_1.png, qrcode_2.png, etc.

5. Saving the QR Code
Once the QR code is generated, the save_qr_code() function will automatically save the image as generated_qr.png (or another specified filename if you modify the code).

Advanced Usage:

Customizing the Code
You can modify the QR code’s settings based on your needs by adjusting the function arguments. For example, to generate QR codes with different sizes or colors, change the default values in the script:

```
qr = qrcode.QRCode(version=1, box_size=6, border=4)  # Adjust box size and border
```
You can also add more predefined websites or adjust the logic for the multiple QR code generation function.

Handling Errors
If the user doesn’t enter a valid URL, a warning message will appear prompting them to enter a valid website link.

### Troubleshooting:

Tkinter not found:

Make sure Tkinter is installed (pip install tk) and compatible with your Python version.

If you're using a virtual environment, ensure Tkinter is included in the environment.

QR Code Image Not Displaying:

Ensure that you have an image viewer installed on your machine that can open .png files.

File Not Saving:

Check the directory where you are running the script to make sure the QR code image file (generated_qr.png) is being saved there.

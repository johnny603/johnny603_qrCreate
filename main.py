import qrcode
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox


def generate_qr_code(website_link, fill_color, back_color, box_size, border_size):
    qr = qrcode.QRCode(
        version=1,
        box_size=box_size,
        border=border_size
    )
    qr.add_data(website_link)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.show()
    return img


def save_qr_code(img, filename):
    img.save(filename)
    messagebox.showinfo("Success", f"QR Code saved as {filename}")


def on_generate_button_click():
    website_link = entry_link.get()
    fill_color = color_fill_entry.get()
    back_color = color_back_entry.get()
    box_size = int(entry_box_size.get())
    border_size = int(entry_border_size.get())

    if website_link:
        img = generate_qr_code(website_link, fill_color, back_color, box_size, border_size)
        save_qr_code(img, 'generated_qr.png')
    else:
        messagebox.showwarning("Input Error", "Please enter a valid website link.")


def generate_multiple_qrs():
    websites = [
        "https://youtu.be/U6rV-wZ2qlw",
        "https://www.google.com",
        "https://www.github.com"
    ]
    for index, site in enumerate(websites):
        img = generate_qr_code(site, 'green', 'yellow', 5, 8)
        save_qr_code(img, f'qrcode_{index + 1}.png')


# Set up Tkinter window
window = tk.Tk()
window.title("QR Code Generator")

# Create input fields and labels
label_link = tk.Label(window, text="Enter website link:")
label_link.pack()

entry_link = tk.Entry(window, width=50)
entry_link.pack()

label_fill_color = tk.Label(window, text="Fill color:")
label_fill_color.pack()

color_fill_entry = tk.Entry(window, width=50)
color_fill_entry.pack()

label_back_color = tk.Label(window, text="Background color:")
label_back_color.pack()

color_back_entry = tk.Entry(window, width=50)
color_back_entry.pack()

label_box_size = tk.Label(window, text="Box size:")
label_box_size.pack()

entry_box_size = tk.Entry(window, width=50)
entry_box_size.pack()

label_border_size = tk.Label(window, text="Border size:")
label_border_size.pack()

entry_border_size = tk.Entry(window, width=50)
entry_border_size.pack()

# Generate button
generate_button = tk.Button(window, text="Generate QR Code", command=on_generate_button_click)
generate_button.pack()

# Generate multiple QR codes button
multiple_button = tk.Button(window, text="Generate Multiple QR Codes", command=generate_multiple_qrs)
multiple_button.pack()

window.mainloop()


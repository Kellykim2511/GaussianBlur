import tkinter as tk
from tkinter import ttk, END
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageFilter

# Create GUI
root = tk.Tk()
root.title("TiKaY - Gaussian Blur App")
root.geometry("900x600")
root.resizable(width = False, height = False)

# Create Label
title_label = ttk.Label(root, text="Gaussian Blur Image", font=("Times New Roman", 30, "bold italic"))
title_label.place(relx = 0.5, rely = 0.1, anchor="center")

# Uploaded image variable
uploaded_image = None

original_image_label = tk.Label(root)
original_image_label.place(relx = 0.05, rely = 0.45)

blurred_image_label = tk.Label(root)
blurred_image_label.place(relx = 0.5, rely = 0.45)

image_origin = tk.Label(root, text = "Original Image", font = ("Times New Roman", 20, "italic"))
image_origin.place(relx = 0.2, rely = 0.35)

image_blur = tk.Label(root, text = "Blurred Image", font = ("Times New Roman", 20, "italic"))
image_blur.place(relx = 0.6, rely = 0.35)

# Upload image
def uploadImage():
    global uploaded_image
    file_path = fd.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        # Resize image
        image.thumbnail((400, 300))
        uploaded_image = image  # Save the uploaded image
        original_photo = ImageTk.PhotoImage(image)
        original_image_label.configure(image=original_photo)
        original_image_label.image = original_photo

# Apply Gaussian blur
def applyBlur():
    global uploaded_image
    if uploaded_image:
        try:
            blur_radius = int(radius_entry.get())
            # Apply Gaussian blur
            blurred_image = uploaded_image.filter(ImageFilter.GaussianBlur(radius=blur_radius))
            blurred_photo = ImageTk.PhotoImage(blurred_image)
            blurred_image_label.configure(image=blurred_photo)
            blurred_image_label.image = blurred_photo
        except ValueError:
            # Handle invalid input for blur radius
            pass

# Create Buttons
upload_btn = tk.Button(root, text = "Upload Image", font = ("Times New Roman", 15, "bold"), bg = "#CA877E",
                       fg = "white", command = uploadImage)
upload_btn.place(relx = 0.1, rely = 0.22)

# Blur radius input
radius_label = tk.Label(root, text = "Blur Radius:", font = ("Times New Roman", 15))
radius_label.place(relx = 0.6, rely = 0.25, anchor = "center")

radius_entry = tk.Entry(root, font = ("Times New Roman", 15), width = 5)
radius_entry.place(relx = 0.7, rely = 0.25, anchor = "center")
radius_entry.insert(0, "10")

blur_btn = tk.Button(root, text = "BLUR", font = ("Times New Roman", 15, "bold"), bg = "#CA877E",
                     fg = "white", command = applyBlur)
blur_btn.place(relx = 0.8, rely = 0.25, anchor = "center")
# Run GUI
root.mainloop()

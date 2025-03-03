import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

# Function to upload an image
def upload_image():
    global uploaded_image
    file_path = filedialog.askopenfilename(
        initialdir=os.path.expanduser("~"),
        filetypes=[("Image files", ["*.png", "*.jpg", "*.gif", "*.jpeg"])]
    )
    if file_path:
        uploaded_image = Image.open(file_path).convert("RGBA")
        img = uploaded_image.resize((500, 500))
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk
        
        # Show watermark input & button
        watermark_entry.pack(pady=5)
        add_watermark_button.pack(pady=5)
        add_watermark_button.config(state=tk.ACTIVE)

# Function to add diagonal watermark
def add_watermark():
    global uploaded_image
    if uploaded_image is None:
        messagebox.showerror("Error", "Please upload an image first!")
        return
    
    watermark_text = watermark_entry.get().strip()
    if not watermark_text:
        messagebox.showerror("Error", "Please enter the watermark text!")
        return

    # Copy image and add watermark
    watermarked_image = uploaded_image.copy()
    draw = ImageDraw.Draw(watermarked_image)
    
    # Load font (Use a valid font file, fallback to default)
    font_size = int(min(watermarked_image.size) / 10)
    font = ImageFont.load_default(size=font_size)

    # Create a transparent image to draw rotated text
    text_layer = Image.new("RGBA", watermarked_image.size, (0, 0, 0, 0))
    text_draw = ImageDraw.Draw(text_layer)

    # Get text size
    text_bbox = text_draw.textbbox((0, 0), watermark_text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

    # Position text diagonally (from bottom-left to top-right)
    text_x = (watermarked_image.width - text_width) // 4
    text_y = (watermarked_image.height - text_height) // 4

    # Draw text on transparent layer
    text_color = (255, 255, 255, 128)  # White with transparency
    text_draw.text((text_x, text_y), watermark_text, fill=text_color, font=font)

    # Rotate the text layer
    rotated_text = text_layer.rotate(30, expand=1)  # Rotate 30 degrees

    # Resize rotated text to match the original image size
    rotated_text_resized = rotated_text.resize(watermarked_image.size)
    
    # Paste resized rotated text onto the original image
    watermarked_image = Image.alpha_composite(watermarked_image, rotated_text_resized)

    # Display updated image
    img_resized = watermarked_image.resize((500, 500))
    img_tk = ImageTk.PhotoImage(img_resized)
    image_label.config(image=img_tk)
    image_label.image = img_tk

    # Save updated image
    uploaded_image = watermarked_image

    # Disable watermark button & show save button
    add_watermark_button.config(state=tk.DISABLED)
    button_save.pack(pady=5)

# Function to save the image
def save_image():
    global uploaded_image
    if uploaded_image is None:
        messagebox.showerror("Error", "No image to save!")
        return

    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("Image files", ["*.png", "*.jpg", "*.gif", "*.jpeg"]), ("All files", ["*.*"])]
    )
    if save_path:
        uploaded_image.convert("RGB").save(save_path)  # Convert to remove alpha
        messagebox.showinfo("Success", "Image saved successfully!")
    else:
        messagebox.showerror("Error", "Image was not saved!")


# Function to limit watermark text length
def limit_text(*args):
    text = watermark_text_var.get()
    if len(text) > 20:
        watermark_text_var.set(text[:20])  # Trim extra characters


# GUI Setup
root = tk.Tk()
root.title('Image Watermarker')
root.geometry("1080x900")

label = tk.Label(root, text="Welcome to the Image Watermarking App", font=("Calibri", 14))
label.pack(pady=20)

uploaded_image = None

# Watermark input field (hidden initially)
watermark_text_var = tk.StringVar()
watermark_text_var.trace_add("write", limit_text)  # Bind limit function

watermark_entry = tk.Entry(root, textvariable=watermark_text_var, width=20)
watermark_entry.insert(0, "Enter Watermark")
watermark_entry.pack_forget()


# Buttons
add_watermark_button = tk.Button(root, text="Add Watermark", command=add_watermark)
add_watermark_button.pack_forget()

upload_button = tk.Button(root, text="Choose Image", command=upload_image)
upload_button.pack(pady=10)

button_save = tk.Button(root, text="Save Image", command=save_image)
button_save.pack_forget()

# Image display label
image_label = tk.Label(root)
image_label.pack()

# Run application
root.mainloop()

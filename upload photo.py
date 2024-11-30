import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

def upload_image():

    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])

    if file_path:
        try:

            image = Image.open(file_path)
            image = image.resize((800, 800))
            photo = ImageTk.PhotoImage(image)


            label.config(image=photo)
            label.image = photo
        except Exception as e:
            messagebox.showerror("Error", f"Unable to open image: {e}")
    else:
        messagebox.showinfo("No file", "No file was selected.")


root = tk.Tk()
root.title("Image Upload Program")

upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=20)

label = tk.Label(root)
label.pack(pady=20)


root.mainloop()

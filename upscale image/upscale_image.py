import os
import tkinter as tk
from tkinter import filedialog, messagebox

from PIL import Image, ImageEnhance, ImageFilter, ImageOps


class ImageResizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Resizer")
        self.geometry("300x150")
        self.resizable(False, False)

        self.select_button = tk.Button(
            self, text="Select Image", command=self.select_image
        )
        self.select_button.pack(pady=20)

        self.status_label = tk.Label(self, text="")
        self.status_label.pack()

    def select_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[
                ("Image Files", ("*.jpg", "*.jpeg", "*.png", "*.bmp")),
                ("All Files", "*.*"),
            ],
        )
        if file_path:
            try:
                output_path = self.process_image(file_path)
                messagebox.showinfo(
                    "Success", f"Image resized successfully!\n\nSaved as:\n{output_path}"
                )
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def process_image(self, file_path):
        with Image.open(file_path) as source:
            # Phone and camera photos often store their orientation in EXIF
            # metadata. Apply it to the pixels before saving so the output is
            # not rotated after metadata is discarded.
            image = ImageOps.exif_transpose(source)

            new_size = (image.width * 4, image.height * 4)
            denoised = image.filter(ImageFilter.MedianFilter(size=3))
            sharpened = denoised.filter(
                ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3)
            )
            corrected = ImageEnhance.Color(sharpened).enhance(1.5)
            resized = corrected.resize(new_size, resample=Image.Resampling.BICUBIC)

            stem, extension = os.path.splitext(file_path)
            output_path = f"{stem}_4k{extension}"
            resized.save(output_path)

        self.status_label.config(text=f"Image saved as: {output_path}")
        return output_path


if __name__ == "__main__":
    app = ImageResizer()
    app.mainloop()

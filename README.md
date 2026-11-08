# Image Resolution Increaser

A small desktop utility that enlarges an image to four times its original width
and height. It applies light denoising, sharpening, and color enhancement before
saving the result beside the original file.

The app supports JPEG, PNG, and BMP images. Camera and phone photo orientation is
applied before processing, so portrait photos remain upright in the saved output.

## Requirements

- Python 3.9 or newer
- Pillow 9.1 or newer
- Tkinter (included with most Python installations)

Install Pillow:

```bash
python -m pip install "Pillow>=9.1"
```

## Run

```bash
python "upscale image/upscale_image.py"
```

Choose an image in the file dialog. The result is written to the same directory
with `_4k` appended to its filename, leaving the original untouched.

> This tool increases pixel dimensions with bicubic interpolation; it does not
> reconstruct missing detail like an AI super-resolution model.

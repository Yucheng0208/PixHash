import tkinter as tk
from tkinter import filedialog, messagebox
import json
import hashlib
from PIL import Image, ImageTk
import numpy as np
import os

def hash_pixels(image_path):
    img = Image.open(image_path).convert('RGB')
    pixels = np.array(img)
    hash_obj = hashlib.sha256(pixels.tobytes())
    return hash_obj.hexdigest(), img.size, pixels.tolist()

def save_hash_json(image_path):
    hash_value, img_size, pixel_data = hash_pixels(image_path)
    data = {
        "image_path": os.path.basename(image_path),
        "hash": hash_value,
        "size": img_size,
        "pixels": pixel_data
    }
    json_path = os.path.splitext(image_path)[0] + "_hash.json"
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=4)
    messagebox.showinfo("Success", f"Hash and pixel data saved to {json_path}")

def verify_and_restore_image(json_path, image_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    new_hash, _, _ = hash_pixels(image_path)
    
    if new_hash == data["hash"]:
        messagebox.showinfo("Verification", "Image matches JSON hash")
    else:
        messagebox.showwarning("Verification", "Image does NOT match JSON hash")
    
    restored_pixels = np.array(data["pixels"], dtype=np.uint8)
    restored_img = Image.fromarray(restored_pixels)
    restored_img.show()

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        save_hash_json(file_path)

def select_verify():
    json_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if not json_path:
        return
    img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if img_path:
        verify_and_restore_image(json_path, img_path)

def main():
    root = tk.Tk()
    root.title("Image Hash Encoder & Verifier")
    root.geometry("400x200")
    
    btn_upload = tk.Button(root, text="Upload Image & Generate JSON", command=select_image)
    btn_upload.pack(pady=10)
    
    btn_verify = tk.Button(root, text="Verify & Restore Image", command=select_verify)
    btn_verify.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
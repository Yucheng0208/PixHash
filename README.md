# Image Hash Encoder & Verifier (DDW)

This project provides a Python-based tool for image encryption and verification.  
Using SHA-256 hashing on pixel data, supporting both verification and restoration.

## 📢 Publication Information

This work will be presented at the  
**2025 IEEE International Conference on Computation, Big-Data and Engineering (IEEE ICCBE 2025)**.

## 🚀 Features

- Image upload and `SHA-256` hash generation.
- Image verification and restoration.
- User-friendly GUI with Tkinter.

## 📦 Installation Requirements

- Python Version: Python 3.7 or higher.
- Required libraries: `tkinter`, `pillow`, `numpy`.
**Install dependencies via:**
``` bash
pip install pillow numpy
```

## 🔥 Quick Start

```bash
python DDW.py
```

## 🛡️ License

This project is licensed under the [GNU General Public License v3.0 (GPLv3)](LICENSE).
> 📢 Before using this project, please carefully read the [LICENSE](LICENSE) file and comply with the GNU GPLv3 terms.

## ⚠️ Notes

- Even slight modifications (such as compression or format conversion) to the image will cause hash verification to fail.
- The generated JSON file contains complete pixel data; file size may vary depending on image resolution.

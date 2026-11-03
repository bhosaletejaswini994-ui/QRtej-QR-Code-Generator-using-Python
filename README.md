# 📱 QRtej – QR Code Generator using Python

## 📌 Project Overview

**QRtej** is a desktop-based QR Code Generator application developed using Python and CustomTkinter. It allows users to generate QR codes instantly by entering a website URL or any text-based information.

The application provides a simple and attractive graphical user interface (GUI). Users can preview their generated QR codes and download them as PNG image files.

## 🚀 Features

- Simple and user-friendly graphical interface.
- Generate QR codes from website URLs and text.
- Instant QR code generation.
- Preview generated QR codes inside the application.
- Download QR codes as PNG images.
- Input validation for empty fields.
- Success and error messages.
- Clean and modern interface using CustomTkinter.

## 🛠️ Technologies Used

- **Python** – Main programming language.
- **CustomTkinter** – GUI development.
- **qrcode** – QR code generation.
- **Pillow (PIL)** – Image processing and displaying QR codes.

## 📂 Project Structure

```text
QRtej/
│
├── QRGenerator.py
└── qrcode.png
```

## ⚙️ Installation

### Step 1: Install Python

Download Python from:

https://www.python.org/

### Step 2: Install Required Libraries

Open the VS Code terminal or PowerShell and run:

```bash
pip install customtkinter qrcode pillow
```

### Step 3: Run the Application

Navigate to your project folder and execute:

```bash
python QRGenerator.py
```

## 📖 How It Works

1. Open the QRtej application.
2. Enter a website URL or text in the input field.
3. Click the **Generate QR Code** button.
4. The application generates a QR code using the qrcode library.
5. The generated QR code appears in the preview section.
6. Click **Download QR Code** to save the QR code as a PNG image.

## 💼 Real-World Applications

QR code generators are useful in many industries:

- **Retail Businesses:** Generate QR codes for product information.
- **Restaurants:** Create QR codes for digital menus.
- **Marketing:** Share website links and promotional pages.
- **Education:** Share notes, study materials, and learning resources.
- **Banking:** Generate QR codes for payment-related information.
- **Business Cards:** Share contact details through QR codes.

## 🎯 Learning Outcomes

Through this project, I learned:

- Developing desktop applications using CustomTkinter.
- Creating GUI layouts using frames, labels, and buttons.
- Generating QR codes using Python.
- Displaying images using Pillow and CTkImage.
- Handling user input and validation.
- Saving and downloading images using file dialogs.
- Connecting GUI buttons with Python functions.

## 👩‍💻 Author

**Tejaswini Bhosale**

## ⭐ Conclusion

QRtej demonstrates how Python can be used to develop a practical desktop application with a graphical user interface. It provides an easy way to generate, preview, and download QR codes for personal, educational, and business purposes.

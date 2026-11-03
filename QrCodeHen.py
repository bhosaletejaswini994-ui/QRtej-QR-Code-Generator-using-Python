# import qrcode

# code = qrcode.make("https://www.youtube.com/")
# code.save("OpenUTube.png")

import qrcode
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("light")
window = ctk.CTk()
window.geometry("900x600")
window.title("QR Code Generator")
# window.resizable(width=False, height=False)

window.configure(fg_color="#F5F7FA")

header = ctk.CTkFrame(window,height=70,fg_color="white", corner_radius=0)
header.pack(fill="x")

logo = ctk.CTkLabel(header,text="QRtej",font=("Arial", 24, "bold"),text_color="#2563EB")
logo.pack(side="left", padx=30, pady=18)


home = ctk.CTkLabel(header,text="QR Generator",font=("Arial", 15),text_color="#555555")
home.pack(side="right", padx=30)


title = ctk.CTkLabel(window,text="Create Your QR Code",font=("Arial", 32, "bold"),text_color="#222222")
title.pack(pady=(40, 5))

subtitle = ctk.CTkLabel(window,text="Generate a QR code from your link in seconds",font=("Arial", 16),text_color="#666666")
subtitle.pack(pady=(0, 25))

main_frame = ctk.CTkFrame(window,fg_color="transparent")
main_frame.pack(pady=10)


input_card = ctk.CTkFrame(main_frame,width=400,height=300,corner_radius=20,fg_color="white")
input_card.grid(row=0, column=0, padx=15)
input_card.grid_propagate(False)


input_title = ctk.CTkLabel(input_card,text="Enter your link",font=("Arial", 20, "bold"),text_color="#222222")
input_title.pack(pady=(30, 15))

qrdata = ctk.CTkEntry(input_card,placeholder_text="Paste your URL here",width=330,height=45,corner_radius=10)
qrdata.pack(pady=10)

code=None

# label = ctk.CTkLabel(window, text="QR Code Generator", font=("Arial", 25))
# label.pack(pady=30)

def generate_qr():
      data = qrdata.get()
      if data == "":
       alert_label.configure(text="Please enter a link",text_color="red") 
       return
      code = qrcode.make(data)
      code.save("qrcode.png")
   
      image = ctk.CTkImage(light_image=Image.open("qrcode.png"), size=(200, 200))
      qr_label.configure(image=image,text="")
      
      alert_label.configure(text="QR Code generated successfully!",text_color="green")

generate_button = ctk.CTkButton(input_card,text="Generate QR Code",width=330,height=45,corner_radius=10,font=("Arial", 16, "bold"),fg_color="#2563EB",hover_color="#1D4ED8",command=generate_qr)
generate_button.pack(pady=20)

def download_qr():
    if code is None:
        alert_label.configure(text="Please generate a QR code first",text_color="red")
        return
    file_path = ctk.filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        code.save(file_path)
        alert_label.configure(text="QR Code downloaded successfully!",text_color="green")

download_button = ctk.CTkButton(input_card,text="Download QR Code",width=330,height=45,corner_radius=10,font=("Arial", 16, "bold"),fg_color="#2563EB",hover_color="#1D4ED8",command=download_qr)
download_button.pack(pady=10)

alert_label = ctk.CTkLabel(input_card,text="",font=("Arial", 12))
alert_label.pack()


qr_card = ctk.CTkFrame(main_frame,width=300,height=300,corner_radius=20,fg_color="white")
qr_card.grid(row=0, column=1, padx=15)

qr_card.grid_propagate(False)

qr_title = ctk.CTkLabel(qr_card,text="Your QR Code",font=("Arial", 20, "bold"),text_color="#222222")
qr_title.pack(pady=(25, 15))


qr_label = ctk.CTkLabel(qr_card,text="Your QR will appear here",font=("Arial", 13),text_color="#888888")
qr_label.pack(pady=10)

window.mainloop()




import customtkinter as ctk
from tkinter import PhotoImage
import crud


def create_GUI_login():
    GUI = ctk.CTk()
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    GUI.geometry("800x400")
    x = 'Python System'
    GUI.title(x)
    
    #Frames
    frame1 = ctk.CTkFrame(master=GUI, width = 400, height= 800)
    frame1.place(x = 400, y = 0)

    #Image
    image_dir = 'background.png'
    img =  PhotoImage(file= image_dir)
    label_img = ctk.CTkLabel(master= GUI, image= img)
    label_img.place(x=50, y=45)

    #Title GUI
    title_label = ctk.CTkLabel(master=GUI, text='Python Login', font=('Roboto', 18))
    title_label.place(x=550, y=40)

    #Entry
    entry_email = ctk.CTkEntry(master=GUI, placeholder_text="insert your e-mail", width= 300, height=30)
    entry_email.place(x=453, y = 100)
    entry_password = ctk.CTkEntry(master=GUI, placeholder_text="insert your password", width= 300, height=30)
    entry_password.place(x=453, y = 150)

    #Botton
    bt_confirm = ctk.CTkButton(master=GUI, text='Confirm', font=('Roboto', 12), command= lambda: crud.login_user(entry_email.get(), entry_password.get(), GUI))
    bt_confirm.place(x= 613, y= 200)
    bt_cancel = ctk.CTkButton(master=GUI, text='Cancel', font=('Roboto', 12), command= lambda: GUI.destroy())
    bt_cancel.place(x= 453, y= 200)
    bt_registry = ctk.CTkButton(master=GUI, text='Registry', font=('Roboto', 12), width= 300)
    bt_registry.place(x= 453, y= 250)

    #Develop
    label_develop = ctk.CTkLabel(master=GUI, text='Development Mesquita', font=('Roboto', 10))
    label_develop.place(x=550, y=360)

    GUI.mainloop()

def create_GUI_register():
    GUI = ctk.CTk()
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    GUI.geometry("800x400")
    x = 'Python System'
    GUI.title(x)
    
    GUI.mainloop()

def create_GUI_edit_delete():
    GUI = ctk.CTk()
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    GUI.geometry("800x400")
    x = 'Python System'
    GUI.title(x)
    
    GUI.mainloop()
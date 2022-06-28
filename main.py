import customtkinter
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk,font
import plotly.express as px
import tkintermapview as tkmapv
import plotly.graph_objects as go
from src.data import calles, intersc, calles_list
import customtkinter as ctk


def main() -> None:
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.geometry("900x700")
    root.title("Tkinter MapView")
    root.resizable(False,False)
    main_title = ctk.CTkLabel(text="Tkinter MapView",text_font=("Arial",30))
    main_title.pack()

    init_g_label = ctk.CTkLabel(text="Inicio",text_font=("Arial",20))
    init_g_label.place(x=272,y=590)

    final_g_label = ctk.CTkLabel(text="Destino", text_font=("Arial",20))
    final_g_label.place(x=482, y=590)

    combo_init = ctk.CTkComboBox(
        values= calles_list()
    )
    combo_init.place(x=272, y=640)

    combo_final = ctk.CTkComboBox(
        values= calles_list()
    )
    combo_final.place(x=482, y=640)

    label_map = tk.LabelFrame(root)
    label_map.pack(pady=20)
    map_widget = tkmapv.TkinterMapView(label_map, width=1000, height=500, corner_radius=3)
    map_widget.pack()

    #map_widget.set_position()
    map_widget.set_address('Plaza 2 de Mayo, Lima , Peru')
    map_widget.set_zoom(20)

    root.mainloop()


if __name__ == "__main__":
    main()

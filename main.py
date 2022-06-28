import tkinter as tk
import tkintermapview as tkmapv
import plotly.graph_objects as go
from src.data import calles_list
import customtkinter as ctk


def main() -> None:
    ctk.set_appearance_mode("System")

    root = ctk.CTk()
    root.geometry("900x700")
    root.title("Tkinter MapView")
    root.resizable(False, False)
    main_title = ctk.CTkLabel(text="Tkinter MapView", text_font=("Arial", 30))
    main_title.pack()

    init_g_label = ctk.CTkLabel(text="Inicio", text_font=("Arial", 20))
    init_g_label.place(x=172, y=590)

    final_g_label = ctk.CTkLabel(text="Destino", text_font=("Arial", 20))
    final_g_label.place(x=382, y=590)

    def combobox_callback(choice):
        print("combobox drop clicked:", choice)

    combo_init = ctk.CTkComboBox(
        values=calles_list(),
        command=combobox_callback
    )
    combo_init.place(x=172, y=640)

    combo_final = ctk.CTkComboBox(
        values=calles_list(),
        command=combobox_callback
    )
    combo_final.place(x=382, y=640)

    label_map = tk.LabelFrame(root)
    label_map.pack(pady=20)
    map_widget = tkmapv.TkinterMapView(label_map, width=1000, height=500, corner_radius=3)
    map_widget.pack(fill="both", expand=True)

    def add_marker_event(coords):
        print("Add marker:", coords)
        new_marker = map_widget.set_marker(coords[0], coords[1], text="new marker")

    map_widget.add_right_click_menu_command(label="Add Marker",
                                            command=add_marker_event,
                                            pass_coords=True)

    def left_click_event(coordinates_tuple):
        print("Left click event with coordinates:", coordinates_tuple)

    map_widget.add_left_click_map_command(left_click_event)

    def polygon_click(polygon):
        print(f"Polygon clicked: {polygon.name}")

    switzerland_marker = map_widget.set_position(-12.0573852, -77.0161867, marker=True)
    map_widget.set_zoom(8)

    polygon_1 = map_widget.set_polygon([(-12.0602391, -77.0411635), (-12.0593158, -77.0311213), (-12.0573852, -77.0161867)],
                                       # fill_color=None,
                                       # outline_color="red",
                                       #border_width=9,
                                       command=polygon_click,
                                       name="Lima")

    # return map_widget.set_position(19.4, -99.13)

    # map_widget.set_address('Plaza 2 de Mayo, Lima , Peru')
    map_widget.set_zoom(20)

    btn_generate = ctk.CTkButton(text="Generar", text_font=("Arial", 20))
    btn_generate.place(x=600, y=610)

    root.mainloop()


if __name__ == "__main__":
    main()

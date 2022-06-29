import tkinter as tk
import tkintermapview as tkmapv
import plotly.graph_objects as go
from src.data import calles_list
from find_path import find_path
import customtkinter as ctk


def generar_caminos(hora, a, b, map_widget):
    # Llamar funcion con dos caminos retornas lista de id de calles
    (roads, paths) = find_path(hora, int(a), int(b))
    
    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black']
    #print path 
    
    if roads is None:
        return None
    
    for road in roads:
        crr_road = list(paths[paths['id'] == road[0]]['combined'].values[0])
        path_1 = map_widget.set_path(crr_road,
                                       color= colors[hora % len(colors)],
                                       #border_width=9,
                                       name="Lima")
        
        
    marker = map_widget.set_position(list(paths.combined.values[0])[0][0], list(paths.combined.values[0])[0][1])

    
    # buscar camino en df de calles e intersecciones
    
    # modifico el mapa lista de duplas de latitudes y longitudes

    pass

def btn_detele_path(map_widget):

    pass
    

def main() -> None:
    ctk.set_appearance_mode("System")

    root = ctk.CTk()
    root.geometry("900x700")
    root.title("Tkinter MapView")
    root.resizable(False, False)
    main_title = ctk.CTkLabel(text="Tkinter MapView", text_font=("Arial", 30))
    main_title.pack()

    init_g_label = ctk.CTkLabel(text="Hora", text_font=("Arial", 20))
    init_g_label.place(x=12, y=590)

    init_g_label = ctk.CTkLabel(text="Inicio", text_font=("Arial", 20))
    init_g_label.place(x=198, y=590)

    final_g_label = ctk.CTkLabel(text="Destino", text_font=("Arial", 20))
    final_g_label.place(x=392, y=590)

    def combobox_callback(choice):
        print("combobox drop clicked:", choice)

    combo_hrs = ctk.CTkComboBox(
        values= list(map(str, range(24))),
        command=combobox_callback
    )
    combo_hrs.place(x=12, y=640)

    combo_init = ctk.CTkComboBox(
        values=calles_list(),
        command=combobox_callback
    )
    combo_init.place(x=198, y=640)

    combo_final = ctk.CTkComboBox(
        values=calles_list(),
        command=combobox_callback
    )
    combo_final.place(x=392, y=640)

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

    marker = map_widget.set_position(-12.0573852, -77.0161867)

    # return map_widget.set_position(19.4, -99.13)

    # map_widget.set_address('Plaza 2 de Mayo, Lima , Peru')
    map_widget.set_zoom(14)

    btn_generate = ctk.CTkButton(
        text="Generar", 
        text_font=("Arial", 20),
        command=lambda: generar_caminos(int(combo_hrs.get()), combo_final.get(), combo_init.get(), map_widget)
    )

    btn_delete = ctk.CTkButton(
        text="Eliminar",
        text_font=("Arial", 20),
        command=btn_detele_path(map_widget)
    )


    btn_delete.place(x=650, y=648)
    btn_generate.place(x=650, y=580)
    

    root.mainloop()


if __name__ == "__main__":
    main()

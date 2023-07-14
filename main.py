import flet as ft
import os
import project_cust_38.Cust_Functions as F
from dataclasses import dataclass, field
import project_cust_38.Cust_SQLite as CSQ

# set Flet path to an empty string to serve at the root URL (e.g., https://lizards.ai/)
# or a folder/path to serve beneath the root (e.g., https://lizards.ai/ui/path
DEFAULT_FLET_PATH = ''  # or 'ui/path'
DEFAULT_FLET_PORT = 80
DEFAULT_FLET_HOST = '192.168.50.230'

db_kplan:str = F.bdcfg('DB_kplan')
DICT_PODRAZDEL = F.raskrit_dict(CSQ.zapros(db_kplan,"""SELECT * FROM podrazdel""",rez_dict=True),'Имя')

@dataclass()
class _Data_vars():
    DICT_PODRAZDEL:dict = field(default_factory=lambda: DICT_PODRAZDEL)

def main(page: ft.Page):
    page.dvars = _Data_vars()
    list_podr = [[_,page.dvars.DICT_PODRAZDEL[_]['Порядок']] for _ in page.dvars.DICT_PODRAZDEL.keys()]
    list_podr = sorted(list_podr, key=lambda x: x[1])
    list_podr = [_[0] for _ in list_podr]
    destinations = [ft.NavigationRailDestination(
                icon=page.dvars.DICT_PODRAZDEL[podr]['icon_flet'].split(';')[0],
        selected_icon=page.dvars.DICT_PODRAZDEL[podr]['icon_flet'].split(';')[1], label=podr.replace('пл_','')
            ) for podr in list_podr]
    #ft.icons.POINT_OF_SALE_ROUNDED
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        #extended=True,
        min_width=40,
        min_extended_width=40,
        #leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=destinations,
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )

    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=2),
                ft.Column([ ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
    )

if __name__ == "__main__":
    flet_path = os.getenv("FLET_PATH", DEFAULT_FLET_PATH)
    flet_port = int(os.getenv("FLET_PORT", DEFAULT_FLET_PORT))
    print(f'http://{DEFAULT_FLET_HOST}:{flet_port}')
    ft.app(name=flet_path, target=main, view=None, port=flet_port, host=DEFAULT_FLET_HOST)
    #ft.app(name=flet_path, target=main)

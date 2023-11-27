import flet as ft
from components import ModeButton, iconButton
from flet import TextAlign
from flet import RoundedRectangleBorder

def main(page: ft.Page):
    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True
    page.window_width = 750
    page.window_height = 140
    page.bgcolor = '#E9E9E9'
    # page.window_title_bar_buttons_hidden = True   
    top_bar = ft.Container(
        content = ft.Row(
            [
                ft.Container(padding=10), #place holder
                ft.Icon()
            ]
        ) 
        )
    
    BT_add_note = ModeButton(f"bt_addnote.svg",f"bt_addnote_selected.svg")
    BT_add_task = ModeButton(f"bt_addtask.svg",f"bt_addtask_selected.svg")
    BT_ask = ModeButton(f"bt_ask.svg",f"bt_ask_selected.svg")
    Icon_tofu = iconButton(f"tofu_icon.png")
    Bar_major = ft.Row(
            [
                Icon_tofu, ft.Container(padding=5),
                BT_add_note, BT_add_task, BT_ask, ft.VerticalDivider(thickness=2),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=8,
            opacity=1,
            expand=True,
        )
    
    test_button1 = ft.ElevatedButton(
        icon="help",
        text=r"/help",
        height=35,
        style = ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                padding=10
            )
        )
    test_button2 = ft.ElevatedButton(
        text=r"/review",
        height=35,
        style = ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                padding=10
            )
        )
    
    Bar_secondary = ft.Row(
            [
                test_button1,test_button2
            ],
            alignment=ft.MainAxisAlignment.END,
            spacing=10,
            opacity=1,
            expand=True,
        )
    
    Row_mode = ft.Row(
        [Bar_major, Bar_secondary],
        expand=False,
        height=40,
    )
    
    Tf_input =  ft.TextField(
        bgcolor=ft.colors.WHITE,
        border=ft.InputBorder.OUTLINE,
        border_color=ft.colors.BLUE_GREY_300,
        border_radius=10,
        border_width=1,
        multiline=True,
        dense=True,
        text_size=15,
        expand=True,
    )
    
    baseContainer = ft.Container(
        content=ft.Column([Row_mode,Tf_input],spacing=5),
        padding=ft.padding.symmetric(0, 5),
        # scale=0.93,
        expand=True
        )

    page.add(baseContainer)

ft.app(target=main)
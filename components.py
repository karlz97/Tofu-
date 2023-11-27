import flet as ft
class ModeButton(ft.UserControl):
    def __init__(self, icon_res:str, selected_icon_res:str):
        super().__init__()
        self.icon = icon_res
        self.selected_icon = selected_icon_res
        self.selected = False
        
    def build(self):
        view = ft.Container(
            content=ft.Image(src=self.icon, width=45, height=40,),
            width=40,
            height=35,
            border_radius=10,
            on_hover=self.shadow_hover,
            on_click=self.clickEffect,
            ink = True,)
        return view
    
    def shadow_hover(self, e: ft.ControlEvent):
        e.control.shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=2,
            offset=ft.Offset(0, 2),
            color=ft.colors.BLUE_GREY_300,
        ) if e.data == "true" else None
        e.control.update()

    def clickEffect(self, e: ft.ControlEvent):
        self.selected = not self.selected
        if not self.selected:
            e.control.content = ft.Image(src=self.icon, fit=ft.ImageFit.FILL,)
            e.control.update()
        else:
            e.control.content = ft.Image(src=self.selected_icon, width=60, height=60, fit=ft.ImageFit.COVER,)
            e.control.update()
            
class iconButton(ft.UserControl):
    def __init__(self, icon_res:str):
        super().__init__()
        self.icon = icon_res
        self.selected = False
        
    def build(self):
        view = ft.Container(
            content=ft.Image(src=self.icon, width=45, height=40,),
            width=100,
            height=35,
            border_radius=10,
            # on_hover=self.shadow_hover,
            # on_click=self.clickEffect,
            ink = True,)
        return view
            
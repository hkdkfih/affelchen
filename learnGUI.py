import flet as ft

def main(page: ft.Page):
    hf = ft.HapticFeedback()
    page.overlay.append(hf)
    ftctext = ft.Text("test1", theme_style=ft.TextThemeStyle.HEADLINE_LARGE)
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    def ftc_onclick(e):
        hf.heavy_impact()
        
        ftctext = ft.Text("test2", theme_style=ft.TextThemeStyle.HEADLINE_LARGE)
            
        page.update()
    ftc = ft.Container(
        content=ftctext,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.INDIGO_300,
        width=250,
        height=400,
        border_radius=10,
        ink=True,
        on_click=ftc_onclick
    )
    inputb = ft.FloatingActionButton(
        icon=ft.icons.INPUT_ROUNDED, on_click=lambda _: hf.medium_impact())
    binput = ft.TextField(label="input")
    row = ft.Row([binput, inputb],spacing=5)
    page.add(ftc,row)
    page.update()

ft.app(target=main)
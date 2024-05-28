import flet as ft
import load
opts = load.load("book_listl")
#opts = {"Red":"Red", "Green":"Green", "Blue":"Blue", "Yellow":"Yellow"}
def main(page: ft.Page):
    def button_clicked(e):
        t.value = f"Dropdown value is:  {dd.value}"
        page.update()

    t = ft.Text()
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    dd = ft.Dropdown(
        width=500,
        options=[
            
        ],
    )
    for i in range(len(opts)):
        print(opts[i])
        dd.options.append(ft.dropdown.Option(opts[i]))
    page.add(dd, b, t)

ft.app(target=main)
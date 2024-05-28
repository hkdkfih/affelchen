import flet as ft

def view(view: ft.View):
    view.add(ft.ElevatedButton(text="Learn"))
    view.add(ft.ElevatedButton(text="Score"))
    view.update()
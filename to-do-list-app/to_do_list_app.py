import flet as ft

def main(page: ft.Page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        page.update()

    new_task = ft.TextField(hint_text="What needs to be done?", expand=True)
    tasks_view = ft.Column()
    view = ft.Column(
        width = 600,
        controls = [
            ft.Row(
                controls = [
                    new_task,
                    ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked),
                ],    
                
            ),
        ],  
    )

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)

ft.app(main)
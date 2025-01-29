import flet as ft

class TodoApp(ft.Column):
    # application's root control is a Column containing all other controls
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(hint_text="What needs to be done?", expand=True)
        self.tasks_view = ft.Column()
        self.width = 600
        self.controls = [
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(
                        icon=ft.Icons.ADD, on_click=self.add_clicked
                    ),
                ],
            ),
            self.tasks_view,
        ]

    def add_clicked(self, e):
        self.tasks_view.controls.append(ft.Checkbox(label=self.new_task.value))
        self.new_task.value = ""
        self.update()

def main(page: ft.Page):
    page.title = "To-Do List"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    # initialize app instance
    todo = TodoApp()

    # add app root control to page
    page.add(todo)

    # example of having two lists one after another
    # app1 = TodoApp()
    # app2 = TodoApp()
    # 
    # page.add(app1, app2)

ft.app(main)


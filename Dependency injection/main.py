from window import Window
from textfile import TextFile
from database import Database

storage = Database()
w = Window(storage)
w.write_text("Greeting from Berlin")
w.show_window()

w.save_text()

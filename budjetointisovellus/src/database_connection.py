import os
import os.path
import sqlite3

# poistaa tietokannan alussa (kätevä moduulin testailussa)
if os.path.exists("courses.db"):
    os.remove("courses.db")

db = sqlite3.connect("courses.db")
db.isolation_level = None
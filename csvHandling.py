import pandas
import tkinter
import os

class Csv:
    def __init__(self, filename: str):
        self.filename = filename
    
    def read(self) -> pandas.DataFrame:
        data = pandas.read_csv(self.filename)
        tkinter.messagebox.showinfo("Success", "CSV file imported successfully")
        return data
    
    def readingTime(self) -> int:
        time: int
        name, ext = os.path.splitext(self.filename)
        name, time = name.rsplit('-', 1)
        return time
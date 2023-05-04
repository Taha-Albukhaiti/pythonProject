import os
import urllib.request
import datetime
import tkinter as tk
#import pygame
"""
---  Dieses Programm nimmt Audio in der Format MP3 auf. Es sollen in der GUI lediglich
---  die URL, der Name der Aufnahme, die Dauer und die Blockgröße eingegeben. 
---  Dann drückt man auf dem Button Aufnehmen und es wird aufgenommen:)
---  URL-Beispiel: http://stream.antenne1.de/a1stg/livestream2.mp3 

---  Ich habe pygame kommentiert, da ich es in dem Semesterprojekt gebrauchen könnte. 
---  Nichtsdestotrotz kann man in diesem Programm die aufgenommene Audiodatei in der GUI
---  abspielen, wenn man einfach die Kommentare entfernt.

---  Autor Taha Al-Bukhaiti
"""

class Audiorekorder_GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Audiorekorder")

        url_label = tk.Label(self.root, text="URL des Streams:")
        url_label.pack()
        self.url_entry = tk.Entry(self.root, width=50)
        self.url_entry.pack()

        filename_label = tk.Label(self.root, text="Name der Aufnahme:")
        filename_label.pack()
        self.filename_entry = tk.Entry(self.root, width=50)
        self.filename_entry.pack()

        duration_label = tk.Label(self.root, text="Dauer der Aufnahme (in Sekunden):")
        duration_label.pack()
        self.duration_entry = tk.Entry(self.root, width=50)
        self.duration_entry.pack()

        blocksize_label = tk.Label(self.root, text="Blockgröße beim Lesen/Schreiben:")
        blocksize_label.pack()
        self.blocksize_entry = tk.Entry(self.root, width=50)
        self.blocksize_entry.pack()

        record_button = tk.Button(self.root, text="Aufnehmen",
                                  command=self.record, width=20, height=1)
        record_button.pack()

        self.output_file_label = tk.Label(self.root, text="")
        self.output_file_label.pack()

       # play_button = tk.Button(self.root, text="Abspielen",
       #                        command=self.play, width=20, height=1)
       # play_button.pack()

        self.output_label = tk.Label(self.root, text="")
        self.output_label.pack()

       # Pygame initialisieren
       # pygame.init()

    def run(self):
        self.root.mainloop()

    def record(self):
        stream = self.url_entry.get()
        filename = self.filename_entry.get()
        if not filename.endswith(".mp3"):
            filename += ".mp3"
        duration = int(self.duration_entry.get())
        blocksize = int(self.blocksize_entry.get())

        start_time = datetime.datetime.now()

        with open(filename, "wb") as m:
            while (datetime.datetime.now() - start_time).seconds < duration:
                m.write(urllib.request.urlopen(stream).read(blocksize))

        self.output_label.configure(text=f"Aufnahme beendet. Datei gespeichert unter: {os.path.abspath(filename)}")
        #self.output_file_label.get()
        #self.filename = filename

"""
    def play(self):
        pygame.mixer.music.load(self.filename)
        pygame.mixer.music.play()
"""

if __name__ == '__main__':
    app = Audiorekorder_GUI()
    app.run()

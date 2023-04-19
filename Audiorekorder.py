import urllib.request
import datetime
import argparse

# ---- Beispiel für Ausführung über Terminal ----
# python3 Audiorekorder.py http://stream.antenne1.de/a1stg/livestream2.mp3 --filename=audio.mp3 --duration=20 --blocksize=2000

# Die Klasse ArgumentParser aus der Bibliothek argparse erstellt die Cli Interface
# und die erfordlichen Einstellung für die Parametrisierung
parser = argparse.ArgumentParser(description="Audiorekorder")
parser.add_argument("url", help="URL des Streams")
parser.add_argument(
    "--filename", help="Name der Aufnahme", default="audio.mp3")
parser.add_argument(
    "--duration", help="Dauer der Aufnahme in Sekunden", type=int, default=10)
parser.add_argument(
    "--blocksize", help="Blockgröße beim Lesen/Schreiben", type=int, default=1000)

args = parser.parse_args()

stream = args.url
start_time = datetime.datetime.now()

with open(args.filename, "wb") as m:
    while (datetime.datetime.now() - start_time).seconds < args.duration:
        m.write(urllib.request.urlopen(stream).read(args.blocksize))
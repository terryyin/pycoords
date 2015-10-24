'''docstring'''

from __future__ import print_function
import csv
from pycoords_lib.coords_view import CoordsView, ScaledCoords
from pycoords_lib.ui import App

VERSION = "0.1.1"


def usage():
    print("Usage:")
    print("    pycoords <csv file path name>")


def main(argv):
    if len(argv) != 2:
        return usage()
    with open(argv[1]) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        coords = [[float(r[0]), float(r[1])] for r in reader]
    app = App("Coords Editor")
    canvas = app.create_canvas()
    coords = ScaledCoords(coords, canvas.get_width(), canvas.get_height())
    CoordsView(canvas, coords).show()
    app.mainloop()
    for row in coords.coords:
        print(", ".join(str(i) for i in row))

'''docstring'''

from __future__ import print_function
import csv
from pycoords_lib.coords_view import CoordsView, ScaledCoords
from pycoords_lib.ui import App


def main(argv):
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


if __name__ == "__main__":
    import sys
    main(sys.argv)

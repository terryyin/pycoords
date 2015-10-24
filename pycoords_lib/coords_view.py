'''The view of the app'''


class ScaledCoords(object):
    DOT_RADIUS = 12

    def __init__(self, coords, width, height):
        self.coords = coords
        xmin = min(x[0] for x in coords)
        xmax = max(coords, key=lambda x: x[0])[0]
        ymin = min(coords, key=lambda x: x[1])[1]
        ymax = max(coords, key=lambda x: x[1])[1]
        self.width = width
        self.height = height
        self.scale = self.get_max_scale(xmin, xmax, ymin, ymax)
        self.center_x = (xmin + xmax) / 2
        self.center_y = (ymin + ymax) / 2

    def move_center(self, dx, dy):
        rdx, rdy = self._view_to_real(dx, dy)
        self.center_x -= rdx
        self.center_y -= rdy

    def move_item(self, index, dx, dy):
        rdx, rdy = self._view_to_real(dx, dy)
        self.coords[index][0] += rdx
        self.coords[index][1] += rdy

    def remove_item(self, index):
        del self.coords[index]

    def point_do(self, x, y, callback):
        def indot(i):
            oldx, oldy = self.scaled(i)
            distance = ((oldx - x) ** 2 + (oldy - y) ** 2)
            return distance <= self.DOT_RADIUS ** 2
        under = [i for i in range(len(self.coords)) if indot(i)]
        if under:
            callback(under[-1])
            return True

    def get_max_scale(self, xmin, xmax, ymin, ymax):
        def convert(i, j):
            return float(i - 2 * self.DOT_RADIUS) / j
        return min(
            convert(self.width, xmax - xmin),
            convert(self.height, ymax - ymin))

    def scaled(self, index):
        real_x, real_y = self.coords[index]
        return (
            (real_x-self.center_x+self.width/2/self.scale)*self.scale,
            (real_y-self.center_y+self.height/2/self.scale)*self.scale)

    def each(self, callback):
        for i in range(len(self.coords)):
            callback(i)

    def add(self, x, y):
        self.coords.append([
            x/self.scale+self.center_x-self.width/2/self.scale,
            y/self.scale+self.center_y-self.height/2/self.scale])
        return len(self.coords) - 1

    def _view_to_real(self, dx, dy):
        return dx / self.scale, dy / self.scale


class CoordsView(object):

    def __init__(self, canvas, coords):
        self.canvas = canvas
        canvas.set_event_receiver(self)
        self._items = {}
        self.coords = coords

    def show(self):
        self.canvas.destroy_all()
        self._items = {}
        self.coords.each(self.put)

    def move(self, x, y, dx, dy):
        def move_item(coord):
            self.coords.move_item(coord, dx, dy)
            self.put(coord)
        if not self.coords.point_do(x, y, move_item):
            self.coords.move_center(dx, dy)
            self.show()

    def remove(self, x, y):
        def remove_item(coord):
            self.coords.remove_item(coord)
            self.show()
        self.coords.point_do(x, y, remove_item)

    def zoom_in(self):
        self.coords.scale *= 1.5
        self.show()

    def zoom_out(self):
        self.coords.scale /= 1.5
        self.show()

    def add(self, x, y):
        self.put(self.coords.add(x, y))

    def put(self, coord):
        for i in self._items.get(coord, []):
            self.canvas.destroy(i)
        x, y = self.coords.scaled(coord)
        self._items[coord] = (
            self.canvas.create_circle(
                x, y, self.coords.DOT_RADIUS, fill="blue"),
            self.canvas.create_text(x, y, fill="white", text=str(coord)))

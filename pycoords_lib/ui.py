'''the ui elements'''

from Tkinter import Tk, Frame, YES, BOTH, Canvas


class Dragger(object):
    def __init__(self):
        self.x = self.y = None
        self.dragging = False

    def start(self, x, y):
        self.x = x
        self.y = y
        self.dragging = True

    def drag_to(self, x, y, callback):
        if self.dragging:
            dx, dy = x - self.x, y - self.y
            if not dx == dy == 0:
                callback(self.x, self.y, dx, dy)
        self.dragging = False


class CoordsCanvas(object):
    def __init__(self, parent, **kwargs):
        self._canvas = Canvas(parent, **kwargs)
        self._canvas.pack(fill=BOTH, expand=YES)
        self._canvas.bind("<Double-Button-1>", self.on_double_click)
        self._canvas.bind("<Shift-Button-1>", self.on_shift_button_click)
        self._canvas.bind("<Control-Button-1>", self.on_ctrl_button_click)
        self._canvas.bind("<Alt-Button-1>", self.on_alt_button_click)
        self._canvas.bind("<Option-Button-1>", self.on_alt_button_click)
        self._canvas.bind("<Double-Button-1>", self.on_double_click)
        self._canvas.bind("<ButtonPress-1>", self.on_button_press)
        self._canvas.bind("<ButtonRelease-1>", self.on_button_release)
        self._event_receiver = None
        self._dragger = Dragger()

    def on_double_click(self, _):
        if hasattr(self._event_receiver, 'zoom_in'):
            self._event_receiver.zoom_in()

    def on_shift_button_click(self, _):
        if hasattr(self._event_receiver, 'zoom_out'):
            self._event_receiver.zoom_out()

    def on_ctrl_button_click(self, event):
        if hasattr(self._event_receiver, 'add'):
            self._event_receiver.add(event.x, event.y)

    def on_alt_button_click(self, event):
        if hasattr(self._event_receiver, 'remove'):
            self._event_receiver.remove(event.x, event.y)

    def on_button_press(self, event):
        self._dragger.start(event.x, event.y)

    def on_button_release(self, event):
        if hasattr(self._event_receiver, 'move'):
            self._dragger.drag_to(
                event.x, event.y,
                self._event_receiver.move)

    def create_circle(self, x, y, r, **kwargs):
        return self._canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)

    def create_text(self, x, y, **kwargs):
        return self._canvas.create_text(x, y, **kwargs)

    def get_width(self):
        return self._canvas.winfo_reqwidth()

    def get_height(self):
        return self._canvas.winfo_reqheight()

    def set_event_receiver(self, receiver):
        self._event_receiver = receiver

    def destroy(self, item):
        self._canvas.delete(item)

    def destroy_all(self):
        self._canvas.delete("all")


class App(object):
    def __init__(self, title):
        self.root = Tk()
        self.root.title(title)
        self.frame = Frame(self.root, width=500, height=500)
        self.frame.pack(fill=BOTH, expand=YES)

    def create_canvas(self):
        return CoordsCanvas(
            self.frame, width=500, height=500,
            bg="white", highlightthickness=0)

    def mainloop(self):
        self.root.mainloop()

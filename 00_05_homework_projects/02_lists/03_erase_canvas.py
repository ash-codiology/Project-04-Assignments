import tkinter as tk

CELL_SIZE = 30
ERASER_SIZE = 3

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=500, height=500)
        self.canvas.pack()
        
        self.cells = []
        self.create_grid()
        self.create_eraser()
        
        self.eraser_on = False

        self.canvas.bind("<B1-Motion>", self.drag_eraser)
        self.canvas.bind("<ButtonRelease-1>", self.stop_eraser)

    def create_grid(self):
        for y in range(0, 500, CELL_SIZE):
            row = []
            for x in range(0, 500, CELL_SIZE):
                rect = self.canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill="blue", outline="blue")
                row.append(rect)
            self.cells.append(row)

    def create_eraser(self):
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE * CELL_SIZE, ERASER_SIZE * CELL_SIZE, fill="white", outline="white")
        
    def drag_eraser(self, event):
        x, y = event.x, event.y
        self.canvas.coords(self.eraser, x - ERASER_SIZE * CELL_SIZE / 2, y - ERASER_SIZE * CELL_SIZE / 2,
                           x + ERASER_SIZE * CELL_SIZE / 2, y + ERASER_SIZE * CELL_SIZE / 2)
        self.erase_cells(x, y)

    def stop_eraser(self, event):
        self.eraser_on = False

    def erase_cells(self, x, y):
        min_x = (x - ERASER_SIZE * CELL_SIZE / 2) // CELL_SIZE
        max_x = (x + ERASER_SIZE * CELL_SIZE / 2) // CELL_SIZE
        min_y = (y - ERASER_SIZE * CELL_SIZE / 2) // CELL_SIZE
        max_y = (y + ERASER_SIZE * CELL_SIZE / 2) // CELL_SIZE

        for i in range(int(min_x), int(max_x)):
            for j in range(int(min_y), int(max_y)):
                if 0 <= i < len(self.cells) and 0 <= j < len(self.cells[i]):
                    self.canvas.itemconfig(self.cells[i][j], fill="white")


root = tk.Tk()
app = EraserApp(root)
root.mainloop()
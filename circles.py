from tkinter import *
import random
import time
import math

SIZE = 800

COLORS = ["#FFFFFF",
          "#E9F0FC",
          "#D4E1F8",
          "#BED2F5",
          "#A9C2F2",
          "#93B3EE",
          "#7EA4EB",
          "#6895E8",
          "#5386E4",
          "#316EDF",
          "#1F5BCA",
          "#1A4CA8",
          "#153D87",
          "#102E65",
          "#0A1E43"]


class Circle:
    circles = []

    def __init__(self):
        self.x = 0
        self.y = 0
        self.radius = 0
        self.grow = True
        self.place()

    def check(self, pos_x, pos_y):
        for i in Circle.circles:
            if i.x == pos_x and i.y == pos_y:
                return False
            elif (i.x - pos_x)**2 + (i.y - pos_y)**2 <= i.radius**2:
                return False
        return True

    def place(self):
        pos_x = random.randint(1, SIZE)
        pos_y = random.randint(1, SIZE)
        while not self.check(pos_x, pos_y):
            pos_x = random.randint(1, SIZE)
            pos_y = random.randint(1, SIZE)
        self.x = pos_x
        self.y = pos_y

        self.c = canvas.create_oval(
            self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, outline="white")

    def check_for_collision(self):
        for i in Circle.circles:
            if i.x != self.x or i.y != self.y:
                if (i.x - self.x)**2 + (i.y - self.y)**2 - 100 <= (i.radius + self.radius)**2:
                    return True
        return False

    def enlarge(self):
        if self.grow:
            self.radius += 1
            canvas.delete(self.c)
            self.c = canvas.create_oval(
                self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, outline="white")
            if self.check_for_collision():
                self.grow = False
            self.colorize()

    def colorize(self):
        index = self.radius / find_max_radius()
        index *= len(COLORS)-1
        index = math.floor(index)
        index = len(COLORS)-index-1
        canvas.itemconfig(
            self.c, outline=COLORS[index], fill=COLORS[index])


def create_window():
    global window
    window = Tk()
    window.geometry(f"{SIZE}x{SIZE}")
    window.resizable(height=False, width=False)
    window.config(bg="black")
    window.title("Circles")

    global canvas
    canvas = Canvas(width=SIZE, height=SIZE,
                    bg="black", highlightthickness=0)
    canvas.pack()


def find_max_radius():
    max = 0
    for i in Circle.circles:
        if i.radius > max:
            max = i.radius
    return max


def main():
    create_window()

    while True:
        Circle.circles.append(Circle())
        for i in Circle.circles:
            i.enlarge()
        window.update()
        time.sleep(0.001)

    window.mainloop()


if __name__ == "__main__":
    main()

import tkinter as tk
import time, keyboard, random

class cUi:
    def c():
        mShown = bool(True)
        bgW = tk.Tk()
        bgW.overrideredirect(True)
        bgW.attributes('-alpha', 0.7)  # Opacity (0.0 - 1.0)
        bgW.configure(bg='black')  # Background color
        screen_width = bgW.winfo_screenwidth()
        screen_height = bgW.winfo_screenheight()
        bgW.geometry(f"{screen_width}x{screen_height}+0+0")

        # Create a canvas
        canvas = tk.Canvas(bgW, width=screen_width, height=screen_height, bg='black', highlightthickness=0)
        canvas.pack()

        # Number of lines and their length
        num_lines = 100
        line_length = 150
        line_width = 1

        # Generate random connected points
        points = [(random.randint(0, screen_width), random.randint(0, screen_height)) for _ in range(num_lines)]
        velocities = [(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(num_lines)]

        while (True):
            time.sleep(0.02)
            if keyboard.is_pressed('insert'):
                mShown = not mShown
                if mShown == bool(True):
                    eValue = 0.1
                    while eValue < 0.7:
                        time.sleep(0.02)
                        bgW.attributes('-alpha', eValue)
                        eValue += 0.1
                        bgW.update()
                elif mShown == bool(False):
                    eValue = 0.7
                    while eValue > 0.0:
                        time.sleep(0.02)
                        bgW.attributes('-alpha', eValue)
                        eValue -= 0.1
                        bgW.update()
            # Clear the canvas
            canvas.delete('all')

            # Update point positions
            for i in range(num_lines):
                x, y = points[i]
                vx, vy = velocities[i]

                x += vx
                y += vy

                # Wrap the points around the screen
                x = x % screen_width
                y = y % screen_height

                points[i] = (x, y)

            # Draw lines connecting the points
            for i in range(num_lines):
                for j in range(i + 1, num_lines):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
                    if distance <= line_length:
                        canvas.create_line(x1, y1, x2, y2, fill='white', width=line_width)
            bgW.update()
cUi.c()

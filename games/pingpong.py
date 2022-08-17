# pingpong.py
# author: Tristen Miller(trkmille@ucsc.edu)
# inputs: user input to control one paddle
# outputs: a gui to play the game
# lets user bounce a ball around

# rebounding ball
from tkinter import *
from random import choice

gui = Tk()
canvas = Canvas(gui)
wall = canvas.create_rectangle(200, 10, 100, 0, fill='blue')


def gameOver(width, height):
    canvas.delete('all')
    text1 = canvas.create_text(width/2, height/2, text="GAME OVER!",
                               fill='red', font=("Times New Roman", 24))
    text2 = canvas.create_text(
        width/2, (height/2)+20, text="Would you like to play again?")
    button1 = Button(canvas, text="Yes",
                     command=replay, anchor=W, bg='springGreen')
    button1.configure(
        width=2, activebackground="#33B5E5", relief=FLAT)
    button1_window = canvas.create_window(
        (width/2)-10, (height/2)+50, anchor=E, window=button1)
    button2 = Button(canvas, text='No',
                     command=leave, anchor=W, bg='red')
    button2.configure(
        width=2, activebackground='#33b5e5', relief=FLAT)
    button2_window = canvas.create_window(
        width/2, (height/2)+50, anchor=W, window=button2)


def animation():
    global canvas
    global rect
    global dx
    global dy
    try:
        width = int(canvas.cget('width'))
        height = int(canvas.cget('height'))
        x1_b, y1_b, x2_b, y2_b = canvas.coords(ball)
        x1_w, y1_w, x2_w, y2_w = canvas.coords(wall)
        if y1_b <= y2_w:
            center = (x1_b+x2_b)//2
            if center < x2_w and center > x1_w:
                dy = -1.05*dy
                dx = 1.05 * dx
            else:
                gameOver(width, height)

        if x2_b > width or x1_b < 0:
            dx = - dx
        if y2_b > height or y1_b < 0:
            dy = - dy
        canvas.move(ball, dx, dy)
        canvas.after(10, animation)
    except ValueError:
        pass  # hush console errors. These are expected when game over happens


def leave():
    print("Have a nice day!")
    gui.destroy()


def replay():
    global canvas
    global ball
    global wall
    global dx, dy
    # Put a little variety into the start of the game
    allow = [-1, 1]
    dx = choice(allow)
    dy = choice(allow)

    canvas.delete('all')
    wall = canvas.create_rectangle(200, 10, 100, 0, fill='blue')
    ball = canvas.create_oval(100, 100, 125, 125, fill="red")
    canvas.pack()
    animation()


def moveRight(event):
    w, x, y, z = canvas.coords(wall)
    if y <= float(canvas.cget('width')):
        canvas.move(wall, 2, 0)


def moveLeft(event):
    w, x, y, z = canvas.coords(wall)
    if w > 0:
        canvas.move(wall, -2, 0)


# main program
dx, dy = 1, 1
gui.bind('<Right>', moveRight)
gui.bind('<Left>', moveLeft)
replay()
mainloop()

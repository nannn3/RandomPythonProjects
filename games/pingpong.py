# pingpong.py
# author: Tristen Miller(trkmille@ucsc.edu)
# inputs: user input to control one paddle
# outputs: a gui to play the game
# lets user bounce a ball around


from tkinter import *
from random import choice
import pdb


class Ball:
    def __init__(self, canvas, color, dx=1, dy=1):
        self.canvas = canvas
        self.id = canvas.create_oval(100, 100, 125, 125, fill=color)
        self.x1, self.y1, self.x2, self.y2 = canvas.coords(self.id)
        self.dx = dx
        self.dy = dy

    def get_x1(self):
        return int(self.x1)

    def set_x1(self, val):
        self.x1 = val

    def get_x2(self):
        return int(self.x2)

    def set_x2(self, val):
        self.x2 = val

    def get_y1(self):
        return int(self.y1)

    def set_y1(self, val):
        self.y1 = val

    def get_y2(self):
        return int(self.y2)

    def set_y2(self, val):
        self.y2 = val

    def get_dx(self):
        return float(self.dx)

    def set_dx(self, val):
        self.dx = float(val)

    def get_dy(self):
        return float(self.dy)

    def set_dy(self, val):
        self.dy = float(val)

    def move(self):
        self.canvas.move(self.id, self.dx, self.dy)
        self.x1, self.y1, self.x2, self.y2 = canvas.coords(self.id)

    def get_center(self):
        return (self.x2+self.x1)/2


class Paddle:
    def __init__(self, x1, y1, x2, y2, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def move(self, dx):
        self.canvas.move(self.id, dx, 0)
        self.x1, self.y1, self.x2, self.y2 = canvas.coords(self.id)

    def get_x1(self):
        return int(self.x1)

    def get_x2(self):
        return int(self.x2)

    def get_y1(self):
        return int(self.y1)

    def get_y2(self):
        return int(self.y2)


def game_start(plyr: int):
    global ball
    global top_paddle
    canvas.delete("all")
    width = int(canvas.cget('width'))
    height = int(canvas.cget('height'))
    if plyr == 2:
        global bottom_paddle
        bottom_paddle = Paddle(0, height, 100, height-10, canvas, 'green')
    top_paddle = Paddle(0, 0, 100, 10, canvas, 'blue')
    ball = Ball(canvas, 'red')
    canvas.pack()
    animation()


def game_setup():
    c_width = int(canvas.cget('width'))
    c_height = int(canvas.cget('height'))
    canvas.delete('all')

    # Tkinter buttons don't allow arguments in function calls, so we have to use
    # local functions to wrap it

    def p1():
        global player
        player = 1
        game_start(1)

    def p2():
        global player
        player = 2
        game_start(2)

    button1P = Button(canvas, text="1 Paddle", bg='grey', command=p1, anchor=W)
    button1P.configure(
        width=(c_width//2), activebackground='#33B5E5', relief=FLAT)
    button1P_window = canvas.create_window(
        c_width/4, (c_height/2)-(c_height/10), anchor=W, window=button1P)

    button2P = Button(canvas, text="2 Paddles",
                      bg='grey', command=p2, anchor=W)
    button2P.configure(
        width=c_width//2, activebackground='#33B5E5', relief=FLAT)
    button2P_window = canvas.create_window(
        c_width/4, (c_height/2)+(c_height/10), anchor=W, window=button2P)
    canvas.pack()


def game_over():
    # Displays game over screen and allows user to replay
    width = int(canvas.cget("width"))
    height = int(canvas.cget('height'))
    canvas.delete('all')
    text1 = canvas.create_text(width/2, height/2, text="GAME OVER!",
                               fill='red', font=("Times New Roman", 24))
    text2 = canvas.create_text(
        width/2, (height/2)+20, text="Would you like to play again?")
    button1 = Button(canvas, text="Yes",
                     command=game_setup, anchor=W, bg='springGreen')
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


def leave():
    # called from game_over()
    print("Have a nice day!")
    gui.destroy()


def animation():
    # TODO: Make the bottom paddle move,implement collisions for it, keep track of points
    global ball
    global top_paddle

    if ball.get_y1() < top_paddle.get_y2():
        if collide(ball, top_paddle):
            ball.dy *= -1.1
        else:
            game_over()
            return
    # note to self, y1 is the top, y2 is the bottom of the ball
    if ball.x2 > int(canvas.cget('width')) or ball.x1 < 0:
        ball.dx *= -1
    if ball.y2 > int(canvas.cget('height')) or ball.y1 < 0:
        ball.dy *= -1
    ball.move()
    canvas.pack()
    canvas.after(10, animation)


def collide(ball, paddle):
    # called from animation()
    if ball.get_center() >= paddle.get_x1() and ball.get_center() <= paddle.get_x2():
        return True
    else:
        return False


def moveRight(event):
    if top_paddle.get_x2() <= int(canvas.cget('width')):
        top_paddle.move(2)


def moveLeft(event):
    if top_paddle.get_x1() > 0:
        top_paddle.move(-2)


if __name__ == "__main__":
    # main program
    gui = Tk()
    # pdb.set_trace()
    canvas = Canvas(gui)
    dx, dy = 1, 1
    game_setup()
    gui.bind('<Right>', moveRight)
    gui.bind('<Left>', moveLeft)
    mainloop()

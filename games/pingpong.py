# pingpong.py
# author: Tristen Miller(trkmille@ucsc.edu)
# inputs: user input to control one paddle
# outputs: a gui to play the game
# lets user bounce a ball around


from tkinter import *


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


class Board:
    def __init__(self):
        self.ball = None
        self.p1 = None
        self.p2 = None
        self.winner = None

    def get_ball(self):
        return self.ball

    def get_p1(self):
        return self.p1

    def get_p2(self):
        return self.p2

    def set_ball(self, ball):
        self.ball = ball

    def set_p1(self, paddle):
        self.p1 = paddle

    def set_p2(self, paddle):
        self.p2 = paddle

    def get_winner(self):
        return self.winner

    def set_winner(self, winner):
        self.winner = winner


board = Board()


def game_start(plyr: int):
    canvas.delete("all")
    height = int(canvas.cget('height'))
    top_paddle = Paddle(0, 0, 100, 10, canvas, 'blue')
    ball = Ball(canvas, 'red')
    if plyr == 2:
        bottom_paddle = Paddle(0, height, 100, height-10, canvas, 'green')
    else:
        bottom_paddle = None
    board.set_ball(ball)
    board.set_p1(top_paddle)
    board.set_p2(bottom_paddle)
    canvas.pack()
    animation()


def game_setup():
    c_width = int(canvas.cget('width'))
    c_height = int(canvas.cget('height'))
    canvas.delete('all')

    # Tkinter buttons don't allow arguments in function calls, so we have to use
    # local functions to wrap it

    def p1():
        game_start(1)
    # end p1

    def p2():
        game_start(2)
    # end p2
    button1P = Button(canvas, text="1 Paddle", bg='grey',
                      command=p1, anchor=CENTER)
    button1P.configure(
        width=(c_width//4), activebackground='#33B5E5', relief=FLAT)
    button1P_window = canvas.create_window(
        c_width/4, (c_height/2)-(c_height/10), anchor=W, width=c_width//2, window=button1P)

    button2P = Button(canvas, text="2 Paddles",
                      bg='grey', command=p2, anchor=CENTER)
    button2P.configure(
        width=c_width//2, activebackground='#33B5E5', relief=FLAT)
    button2P_window = canvas.create_window(
        c_width/4, (c_height/2)+(c_height/10), anchor=W, width=c_width//2, window=button2P)
    canvas.pack()


def game_over():
    # Displays game over screen and allows user to replay
    def leave():
        # called to end the program
        print("Have a nice day!")
        gui.destroy()

    width = int(canvas.cget("width"))
    height = int(canvas.cget('height'))
    canvas.delete('all')

    text1 = canvas.create_text(width/2, height/2, text="GAME OVER!",
                               fill='red', font=("Times New Roman", 24))
    if board.get_winner() == 'Player':
        text2 = canvas.create_text(
            width/2, (height/2)+30, text="You Won!", fill='green', font=("Times New Roman", 20))
    else:
        text2 = canvas.create_text(width/2, (height/2)+30, text="You lost!",
                                   fill='red', font=("Times New Roman", 20))
    text3 = canvas.create_text(
        width/2, (height/2)+50, text="Would you like to play again?")
    # Yes button V
    button1 = Button(canvas, text="Yes",
                     command=game_setup, anchor=W, bg='springGreen')
    button1.configure(
        width=2, activebackground="#33B5E5", relief=FLAT)
    button1_window = canvas.create_window(
        (width/2)-10, (height/2)+70, anchor=E, window=button1)
    # No button V
    button2 = Button(canvas, text='No',
                     command=leave, anchor=W, bg='red')
    button2.configure(
        width=2, activebackground='#33b5e5', relief=FLAT)
    button2_window = canvas.create_window(
        width/2, (height/2)+70, anchor=W, window=button2)


def wall_ai(ball, paddle):
    # basic ai, might make more complex later
    if ball.get_center() < paddle.get_x1():
        paddle.move(-2)
    elif ball.get_center() > paddle.get_x2():
        paddle.move(2)


def animation(*args):
    # TODO: Keep track of points
    ball = board.get_ball()
    top_paddle = board.get_p1()
    bottom_paddle = board.get_p2()
    if bottom_paddle:
        wall_ai(ball, bottom_paddle)
        if ball.get_y2() > bottom_paddle.get_y1():
            if collide(ball, bottom_paddle):
                ball.set_dy(ball.get_dy()*-1.1)
            else:
                board.set_winner("Player")
                game_over()
                return

    if ball.get_y1() < top_paddle.get_y2():
        if collide(ball, top_paddle):
            ball.set_dy(ball.get_dy()*-1.1)
        else:
            board.set_winner("Ai")
            game_over()
            return
    # note that x1 is the left side, x2 is right, y1 is top, and y2 is bottom
    if ball.get_x2() > int(canvas.cget('width')) or ball.get_x1() < 0:
        ball.set_dx(ball.get_dx() * -1)
    if ball.get_y2() > int(canvas.cget('height')) or ball.get_y1() < 0:
        ball.set_dy(ball.get_dy() * -1)
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
    try:
        if board.get_p1().get_x2() <= int(canvas.cget('width')):
            board.get_p1().move(2)
    except ValueError:  # Hush console errors that occur when at the game over screen
        pass


def moveLeft(event):
    try:
        if board.get_p1().get_x1() > 0:
            board.get_p1().move(-2)
    except ValueError:
        pass


if __name__ == "__main__":
    # main program
    gui = Tk()
    canvas = Canvas(gui)
    game_setup()
    gui.bind('<Right>', moveRight)
    gui.bind('<Left>', moveLeft)
    mainloop()

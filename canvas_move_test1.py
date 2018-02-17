from Tkinter import *
import random
import sys

sys.setrecursionlimit(500)

root = Tk()
circles_container = []
test_param1 = 200
canvas_height = 400
canvas_width = 600
right_keyup = True
left_keyup = True
up_keyup = True
down_keyup = True

# changes for feature/implement_awesomeness
# more awesome changes

def draw_circle(canv):
    global circles_container, test_param1
    new_circle_class = CircleClass(canv, root)
    circles_container.append(new_circle_class)

class CircleClass():
    def __init__(self, canvas, root):
        self.radius = 30
        self.position = [0, 1]
        self.position[0] = random.randrange(100, 300)
        self.position[1] = random.randrange(100, 300)
        self.increment = 0
        self.loop_count = 0
        draw_ball(self, canvas)
        """ Apply gravity effects to the balls """
        # while (self.position[1] + self.radius < canvas_height - 5):
        #    self.gravity_effect(root, canvas, 0.00001)
        # if (int(self.position[1]) + self.radius <
        #    canvas_height) and (int(self.position[1] + self.radius > 
        #    (canvas_height-5))):
        #    while (self.position[1] + self.radius > 200):
        #        self.gravity_effect(root, canvas, -0.00001)
        
    def update(self, canvas):
        pass
        
        
    def gravity_effect(self, root, canvas, increment_value):
        self.increment += increment_value
        self.position[1] += increment_value
        canvas.move(self.oval1, 0, self.increment)
        self.position[1] = canvas.coords(self.oval1)[1]
        #print (int(self.position[1]) + self.radius)
        canvas.update()
        
def draw_ball(ball, canvas):
    ball.oval1 = canvas.create_oval(ball.position[0], ball.position[1], 
                                    ball.position[0] + ball.radius, 
                                    ball.position[1] + ball.radius, 
                                    width = 4, outline='white', 
                                    fill='black')
    #root.after(1000, self.draw_ball(canvas))
        
#def move_ball(ball_to_move, canvas):
#    dist = 0
#    while (ball_to_move.position[0] < canvas_width):
#        root.canvas.move(ball_to_move.oval1, dist, 0)
#        dist += 0.000001
#        root.update()
            
def move_right_keyup(canvas):
    global right_keyup
    right_keyup = True
    # print "right key up"
    
def move_left_keyup(canvas):
    global left_keyup
    left_keyup = True
    # print "left key up"
    
def move_up_keyup(canvas):
    global up_keyup
    up_keyup = True
    # print "up key up"
    
def move_down_keyup(canvas):
    global down_keyup
    down_keyup = True
    # print "down key up"

def move_right(canvas):
    global test_param1, circles_container, right_keyup
    right_keyup = False
    for i in circles_container:
        dist = 0
        while (right_keyup == False):
            root.canvas.move(i.oval1, dist, 0)
            dist += 0.00001
            root.update()

def move_left(canvas):
    global circles_container, left_keyup
    left_keyup = False
    for i in circles_container:
        dist = 0
        while (left_keyup == False):
            root.canvas.move(i.oval1, dist, 0)
            dist -= 0.000001
            root.update()

def move_up(canvas):
    global circles_container
    for i in circles_container:
        dist = 0
        while (up_keyup == False):
            root.canvas.move(i.oval1, 0, dist)
            dist -= 0.000001
            root.update()

def move_down(canvas):
    global circles_container
    for i in circles_container:
        dist = 0
        while (down_keyup == False):
            root.canvas.move(i.oval1, 0, dist)
            dist += 0.000001
            root.update()


root.canvas = Canvas(bg = "black", height = canvas_height, 
                     width = canvas_width)
                     
""" The key press continuously calls the function again and again as long as 
the key is kept depressed. In order to avoid this, some kind of timer 
would have to be used. This can be tested by adding a draw_circle method 
for the KeyRelease event for any of the keys below. Multiple circles would 
be drawn as long as the key is depressed, proving that the draw function is 
being called repeatedly. """
root.canvas.bind("<KeyPress-Right>", move_right)
root.canvas.bind("<KeyPress-Left>", move_left)
root.canvas.bind("<KeyPress-Up>", move_up)
root.canvas.bind("<KeyPress-Down>", move_down)

root.canvas.bind("<KeyRelease-Right>", move_right_keyup)
root.canvas.bind("<KeyRelease-Left>", move_left_keyup)
root.canvas.bind("<KeyRelease-Up>", move_up_keyup)
root.canvas.bind("<KeyRelease-Down>", move_down_keyup)

""" Notice how the lambda function is using 'x' here, in contrast to the
usage in the lines below. """
root.canvas.bind("<KeyPress-space>", lambda x: draw_circle(root.canvas))
root.canvas.focus_set()
root.canvas.pack()

""" lambda defines a one line mini function. Without it, the command would 
execute as soon as the dialog opens. """
draw_circle_button = Button(command = lambda: draw_circle(root.canvas), text = 
                            "Circle", height = 1, width = 10, pady = 10)
draw_circle_button.pack()

""" Positioning the window in the center of the screen """
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#root.geometry("%dx%d+%d+%d" % (500, 350, screen_width/4, screen_height/4))

root.mainloop(0)

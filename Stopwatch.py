# template for "Stopwatch: The Game"

import simplegui

# define global variables
tenths_of_seconds = 0
number_of_plays = 0
number_won = 0
stopwatch_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
# A = minutes
# B = tens place of seconds
# C = units place of seconds
# D = tenths_of_seconds

def format(n):
    A = n/600
    B = (n%600)/100
    C = ((n%600) - B*100)/10
    D = (n%600) - B*100 - C*10
    return str(A)+":"+str(B)+str(C)+"."+str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()
    global stopwatch_running
    stopwatch_running = True
    
def stop_handler():
    global number_of_plays, number_won, stopwatch_running
    timer.stop()
    if(stopwatch_running == True):
        stopwatch_running = False
        number_of_plays += 1
        if(tenths_of_seconds%10 == 0):
            number_won += 1
    
def reset_handler():
    global tenths_of_seconds, number_of_plays, number_won, stopwatch_running
    tenths_of_seconds = 0
    number_of_plays = 0
    number_won = 0
    stopwatch_running = False
    timer.stop()
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global tenths_of_seconds
    tenths_of_seconds  += 1
    
# define draw handler
def draw(canvas):
    canvas.draw_text(format(tenths_of_seconds), [100,120], 44, "White")
    canvas.draw_text("/" + str(number_of_plays), [270,20], 30, "Red")
    canvas.draw_text(str(number_won), [255,20], 30, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch!", 300, 200)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start_handler, 100)
frame.add_button("Stop", stop_handler, 100)
frame.add_button("Reset", reset_handler, 100)

# start frame
frame.start()

# Please remember to review the grading rubric

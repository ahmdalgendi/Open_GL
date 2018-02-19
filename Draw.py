from INIT import *

def draw():
    body_w = .7
    body_h= .6
    body_x=-0.4
    body_y = - 0.2
    glClearColor(139/255,90/255 , 43/255, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    ##---------------------------------------################### legs
    add_rectangle(body_x + .14, body_y - .3, body_w / 7, body_h / 1.2, 'red')

    add_rectangle(body_x + .5, body_y - .3, body_w / 7, body_h / 1.2, 'red')
    ##################################################################3
    add_rectangle(body_x+.07,body_y , body_w*.9,body_h,'black')
    #head
    head_rad = 0.2
    add_circle(body_x+.4, body_y+head_rad+.6,head_rad ,'green')
    #mouth
    add_circle(body_x+.4, body_y+head_rad+.6,head_rad/1.3 ,'black')
    add_circle(body_x+.4, body_y+head_rad+.67,head_rad/1.3 ,'green')
    add_circle(body_x+.4, body_y+head_rad+.6,head_rad/2 ,'red')
    #eyes_right
    add_circle(body_x+.52, body_y+head_rad+.7,head_rad/5 ,'black')
    add_circle(body_x+.52, body_y+head_rad+.7,head_rad/11 ,'white')
    add_circle(body_x+.52, body_y+head_rad+.7,head_rad/15 ,'black')
    #left eye
    add_circle(body_x+.3, body_y+head_rad+.7,head_rad/5 ,'black')
    add_circle(body_x+.3, body_y+head_rad+.7,head_rad/11 ,'white')
    add_circle(body_x+.3, body_y+head_rad+.7,head_rad/15 ,'black')
    #sensors
    add_rectangle(body_x+.28,body_y+.95, body_w/25,body_h/4,'green')
    add_circle(body_x+.299, body_y+1.12, head_rad/6.5,'red')
    add_circle(body_x+.299, body_y+1.12, head_rad/9,'black')
    ####


    add_rectangle(body_x+.47,body_y+.95, body_w/25,body_h/4,'green')
    add_circle(body_x+.47+.011, body_y+1.12, head_rad/6.5,'red')
    add_circle(body_x+.47+.011, body_y+1.12, head_rad/9,'black')
    ## heart
    add_circle(body_x+.27,body_y+.44,head_rad/2,'red')
    add_circle(body_x+.32,body_y+.2,head_rad/2.8,'red')
    add_circle(body_x+.5,body_y+.4,head_rad/3,'red')
    ## shoulders
    add_circle(body_x+.10, body_y+.65, head_rad/2,'back')
    add_circle(body_x+.0760+body_w*.9, body_y+.65, head_rad/2,'back')
    ######## hand
    add_rectangle(body_x-.4,body_y+.37 , body_w *.7,body_h *.3,'black')
    add_rectangle(body_x - .45, body_y + .44, body_w * .7, body_h * .1, 'blue')

    glFlush()



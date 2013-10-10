import math
import pygame

def mandlebrot(x_0, ci, cj, x_range, y_range, depth):
    i = float(-x_range) #i = Re{x}
    di = -i/depth
    j = float(-y_range) #j = Im{x}
    dj = -j/depth
    #check grid of points
    while j < y_range:
        i = float(-x_range)
        while i < x_range:
            if mandlebrot_point_in(i,j,c_real,c_img):
                #draw_point(i,j)
                print("IN: (%3f, %3f)" % (i, j))
            i += di
            #pygame.display.update()
        j += dj

#TO DO      
def draw_point(x,y):
    point = pygame.Rect(x,y,1,1)
    pygame.draw.rect(surface, black, point)

#toggle max depth and magnitude limit for cut-off
max_depth = 5
upper_limit = 2
def mandlebrot_point_in(x, y, c_real, c_img, depth = max_depth):
    if depth > 0:
        if x**2 + y**2 >= upper_limit:
            return False
        #using x_n+1 = x_n^2 + c with complex values
        #(a+ib)^2 + c= a^2 + 2iab - b^2 + c = a^2 - b^2 + c_real + i(2ab+c_img)
        #TO DO:  Use complex library to simplify this
        return mandlebrot_point_in(x**2 - y**2 + c_real, 2*x*y + c_img, c_real,
                                   c_img, depth-1)
    return True

##pygame.init()

screen_height = 600
screen_width = 800

##black = pygame.Color(0,0,0,255)
##surface = pygame.Surface((height,width))
##
##window = pygame.display.set_mode((width, height))
y_range = 2
x_range = 2
x_0 = 0
c_real = 0.3
c_img = 0.1
mandlebrot(x_0, c_real, c_img, x_range, y_range, 100)

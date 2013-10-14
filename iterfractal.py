import math
import pygame

def julia(x_0, ci, cj, x_range, y_range, di, dj, depth, file):
    i = float(-x_range) #i = Re{x}
    j = float(-y_range) #j = Im{x}
    #check grid of points
    while j < y_range:
        i = float(-x_range)
        while i < x_range:
            if julia_point_in(i, j, c_real, c_img, depth):
                file.write("%5f\t%5f\n" % (i, j))
            i += di
        j += dj

#TO DO      
def draw_point(x,y):
    point = pygame.Rect(x,y,1,1)
    pygame.draw.rect(surface, white, point)

def julia_point_in(x, y, c_real, c_img, depth = 5):
    if depth > 0:
        if x**2 + y**2 >= upper_limit:
            return False
        #using x_n+1 = x_n^2 + c with complex values
        #(a+ib)^2 + c= a^2 + 2iab - b^2 + c = a^2 - b^2 + c_real + i(2ab+c_img)
        return julia_point_in(x**2 - y**2 + c_real, 2*x*y + c_img, c_real,
                                   c_img, depth-1)
    return True

def mandlebrot(real_range, img_range, dc_real, dc_img, depth, file):
    c_real = float(-real_range) #i = Re{x}
    c_img = float(-img_range) #j = Im{x}
    #check grid of points
    while c_img < img_range:
        c_real = float(-real_range)
        while c_real < real_range:
            if julia_point_in(0, 0, c_real, c_img, depth):
                file.write("%5f\t%5f\n" % (c_real, c_img))
            c_real += dc_real
        c_img += dc_img

# File Saving Settings
julia_f = open('julia.dat', 'w')
mandlebrot_f = open('mandlebrot.dat', 'w')

# Fractal Detail Settings
x_range = 2
dx = 0.002
y_range = 2
dy = 0.002
depth = 25
upper_limit = 5

#Julia Set Settings
x_0 = 0
c_real = -.8
c_img = .156
#julia(x_0, c_real, c_img, x_range, y_range, dx, dy, depth, julia_f)

#Mandlebrot Set
mandlebrot(x_range, y_range, dx, dy, depth, mandlebrot_f)

julia_f.close()
mandlebrot_f.close()

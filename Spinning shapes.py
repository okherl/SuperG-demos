#created by aryan pokhrel
#uploaded on 29/dec/2024
#just used to demonstarte a little bit of what Super_G can do

from Super_G_v1_2 import *

def up(p):
    pyramid.move(0, -5, 0)
    cube.move(0, -5, 0)

def down(p):
    pyramid.move(0, 5, 0)
    cube.move(0, 5, 0)

def left(p):
    pyramid.move(-5, 0, 0)
    cube.move(-5, 0, 0)

def right(p):
    pyramid.move(5, 0, 0)
    cube.move(5, 0, 0)

def d(p):
    pyramid.spin_xz(5)
    cube.spin_xz(5)

def a(p):
    pyramid.spin_xz(-5)
    cube.spin_xz(-5)

def w(p):
    pyramid.spin_yz(5)
    cube.spin_yz(5)

def s(p):
    pyramid.spin_yz(-5)
    cube.spin_yz(-5)

def q(p):
    pyramid.spin_xy(5)
    cube.spin_xy(5)

def e(p):
    pyramid.spin_xy(-5)
    cube.spin_xy(-5)


main_window = window(title = "Spinning shapes")
main_window.display()

#cube
cube_pt_list = [

    [[300, 300, 0], [300, 400, 0], [400, 400, 0], [400, 300, 0]],#back
    [[400, 400, 0], [400, 400, 100], [400, 300, 100], [400, 300, 0]],#right
    [[300, 400, 0], [400, 400, 0], [400, 400, 100], [300, 400, 100]],#bottom
    [[300, 300, 0], [300, 300, 100], [300, 400, 100], [300, 400, 0]],#left
    [[300, 300, 0], [300, 400, 0], [300, 400, 100], [300, 300, 100]],#top
    [[300, 300, 100], [300, 400, 100], [400, 400, 100], [400, 300, 100]]#front

]

cube_list = []

for x in cube_pt_list:
    cube_list.append(poly3d(main_window, x))

cube = shape3d(cube_list)
cube.display()

#the pyramid
pyramid_list_pt = [

    [[200, 200, 0],[100, 300, 0],[200, 300, 0]],
    [[200, 200, 0],[200, 200, 100],[100, 300, 0]],
    [[100, 300, 0],[200, 200, 100],[200, 300, 0]],
    [[200, 300, 0],[200, 200, 100],[200, 200, 0]]

]

pyramid_list = []

for x in pyramid_list_pt:
    pyramid_list.append(poly3d(main_window, x))

pyramid = shape3d(pyramid_list)
pyramid.display()


main_window.keyboard_trigger('Up', up)
main_window.keyboard_trigger('Down', down)
main_window.keyboard_trigger('Left', left)
main_window.keyboard_trigger('Right', right)

main_window.keyboard_trigger("d", d)
main_window.keyboard_trigger('a', a)

main_window.keyboard_trigger('w', w)
main_window.keyboard_trigger('s', s)

main_window.keyboard_trigger('q', q)
main_window.keyboard_trigger('e', e)

text(main_window, x = 10, y = 10, text = "Press up, down, left right, a, d, s, w, q, e for something to happen").display()

main_window.keep_running()
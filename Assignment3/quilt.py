"""
File: quilt.py
--------------
ADD YOUR DESCRIPTION HERE
"""


import sys
import tkinter


def draw_bars(canvas, x, y, width, height, num_lines):
    """
    ADD YOUR COMMENT
    """
    canvas.create_rectangle(x, y, x + width, y + height, outline='lightblue')
    dist = width / (num_lines - 1)
    for i in range(num_lines):
        canvas.create_line(x, y, x, y + height)
        x += dist


def draw_eye(canvas, x, y, width, height, num_lines):
    """
    ADD YOUR COMMENT
    """
    canvas.create_rectangle(x, y, x + width, y + height, outline='lightblue')
    canvas.create_oval(x, y, x + width, y + height, fill='yellow', outline='yellow')
    dist = width / (num_lines - 1)
    start_x = x + width // 2
    start_y = y + height // 2
    for i in range(num_lines):
        canvas.create_line(start_x, start_y, x, (y + height))
        x += dist


def draw_bowtie(canvas, x, y, width, height, num_lines):
    """
    ADD YOUR COMMENT
    """
    canvas.create_rectangle(x, y, x + width, y + height, outline='lightblue')
    dist = height / (num_lines - 1)
    dy = y + height
    for i in range(num_lines):
        canvas.create_line(x, y, (x + width), dy, fill='red')
        y += dist
        dy -= dist


def draw_quilt(canvas, width, height, n):
    """
    Given a canvas which has the dimensions given by the parameters
    width and height, draw a whole quilt on it.  The quilt should
    be comprised of a n-by-n grid of patches (where n is parameter
    that is passed into this function).
    """
    sub_width = width // n
    sub_height = height // n
    x = 0
    y = 0
    for row in range(n):
        for col in range(n):
            choice = (row + col) % 3
            if choice == 0:
                draw_bars(canvas, x, y, sub_width, sub_height, n)
            elif choice == 1:
                draw_bowtie(canvas, x, y, sub_width, sub_height, n)
            elif choice == 2:
                draw_eye(canvas, x, y, sub_width, sub_height, n)
            y += sub_height
        y = 0
        x += sub_width


######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# main() code is complete and should not be modified.
# There are 5 command lines that work here,
# with width/height/n being positive integers.
#  -bars width height num_lines
#  -eye width height num_lines
#  -bowtie width height num_lines
#  -quilt width height n
# e.g. run like this in the terminal:
#  py quilt.py -bars 600 400 10


# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas of the
    of the given int size, ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width + 10, height=height + 10)
    top.title('quilt')
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # add this so (0, 0) works correctly
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    return canvas


def main():
    # Standard first line of main to get args
    args = sys.argv[1:]

    if len(args) != 4:
        print('usage: (one of -bars, -eye, -bowtie, -quilt) width height n')
        return

    # Parse width/height/n from command line, giving a helpful
    # error message if it fails.
    try :
        width = int(args[1])
        height = int(args[2])
        n = int(args[3])
    except Exception as e:
        print("Error parsing int width/height/n from command line:" + ' '.join(args))
        return

    # Tricky: we do all the drawing in a try, so that if it takes an exception,
    # we can still do the mainloop() at the end. If we do not do this, an exception
    # causes no graphics output to appear which makes debugging hard.
    try:
        if args[0] == '-bars':
            canvas = make_canvas(width * 2, height * 2)
            # Can change to fast_draw=False .. drawing plays out more slowly
            draw_bars(canvas, 0, 0, width, height, n)
            draw_bars(canvas, width, height, width, height, n)

        if args[0] == '-eye':
            canvas = make_canvas(width * 2, height * 2)
            draw_eye(canvas, 0, 0, width, height, n)
            draw_eye(canvas, width, height, width, height, n)

        if args[0] == '-bowtie':
            canvas = make_canvas(width * 2, height * 2)
            draw_bowtie(canvas, 0, 0, width, height, n)
            draw_bowtie(canvas, width, height, width, height, n)

        if args[0] == '-quilt':
            canvas = make_canvas(width, height)
            draw_quilt(canvas, width, height, n)

    # Print out exception from draw
    except Exception as e:
        print(e)

    """
    Calls the tkinter.mainloop(), typically last line of main().
    This version checks that there is a window on screen first,
    doing nothing if there is no window.
    """
    if tkinter._default_root:
        tkinter._default_root.update()
        tkinter.mainloop()


if __name__ == '__main__':
    main()

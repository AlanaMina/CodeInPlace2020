"""
File: babygraphics.py
---------------------
Add your comments here
"""

import tkinter
import babynames
import babygraphicsgui as gui


# Provided constants to load and draw the baby data
FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (float): The x coordinate of the vertical line associated
                              with the specified year.
    >>> round(get_x_coordinate(1000, 0), 1)
    20.0
    >>> round(get_x_coordinate(1000, 2), 1)
    180.0
    >>> round(get_x_coordinate(1000, 11), 1)
    900.0
    """
    section = (width // (len(YEARS))) - ((width % (len(YEARS))) - 1)
    return float(section * year_index + GRAPH_MARGIN_SIZE)


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas
    width = canvas.winfo_width()    # get the width of the canvas
    height = canvas.winfo_height()  # get the height of the canvas
    canvas.create_line(GRAPH_MARGIN_SIZE, height - GRAPH_MARGIN_SIZE, width - GRAPH_MARGIN_SIZE,
                       height - GRAPH_MARGIN_SIZE, fill='black')  # bottom
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       fill='black')  # top
    for element in YEARS:
        x = get_x_coordinate(WINDOW_WIDTH, YEARS.index(element))
        canvas.create_line(x, GRAPH_MARGIN_SIZE, x, height - GRAPH_MARGIN_SIZE)
        canvas.create_text((x + TEXT_DX), height - GRAPH_MARGIN_SIZE, anchor=tkinter.NW, text=element)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dictionary of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (tkinter Canvas): The canvas on which we are drawing.
        name_data (dictionary): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot
    """
    draw_fixed_lines(canvas)
    for element in lookup_names:
        color = COLORS[lookup_names.index(element)]
        data = name_data[element]  # dictionary
        for year in YEARS:
            if year not in data:
                rank = MAX_RANK
                label = element + " *"
            else:
                rank = data[year]  # value y
                if rank == 1:
                    label = element + " *"
                else:
                    label = element + " " + str(rank)
            x = get_x_coordinate(WINDOW_WIDTH, YEARS.index(year))
            y = GRAPH_MARGIN_SIZE + ((WINDOW_HEIGHT - (2 * GRAPH_MARGIN_SIZE)) / (MAX_RANK - 1)) * rank
            dx = get_x_coordinate(WINDOW_WIDTH, (YEARS.index(year) + 1))
            year += 10
            if year not in data:
                rank = MAX_RANK
            else:
                rank = data[year]  # value y
            dy = GRAPH_MARGIN_SIZE + ((WINDOW_HEIGHT - (2 * GRAPH_MARGIN_SIZE)) / (MAX_RANK - 1)) * rank
            canvas.create_line(x, y, dx, dy, width=LINE_WIDTH, fill=color)
            canvas.create_text((x + TEXT_DX), (y + TEXT_DX), anchor=tkinter.SW, text=label, fill=color)


# main() code is provided for you
def main():
    import sys
    args = sys.argv[1:]
    global WINDOW_WIDTH
    global WINDOW_HEIGHT
    if len(args) == 2:
        WINDOW_WIDTH = int(args[0])
        WINDOW_HEIGHT = int(args[1])

    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Make window
    top = tkinter.Tk()
    top.wm_title('Baby Names Solution')
    canvas = gui.make_gui(top, WINDOW_WIDTH, WINDOW_HEIGHT, name_data, draw_names, babynames.search_names)

    # draw_fixed once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This needs to be called just once
    top.mainloop()


if __name__ == '__main__':
    main()

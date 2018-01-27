import curses

class Window:
    """
    initialize game window
    params: list of parameters
        title_rows: int, number of rows for title
        window_size: (int, int), rows and columns for main window
        status_rows: int, number of rows for displaying status
    stdscr: a curses.initscr() object
    """
    def __init__(self,params,stdscr):
        self.title_rows = params['title_rows']
        self.window_row, self.window_col = params['window_size']
        self.status_rows = params['status_rows']
        
        self.title_start = 0 # starting row of title
        self.window_start = self.title_rows # starting row of window
        self.status_start = self.window_start + self.window_row # starting row of status
        
        self.title = ""
        self.status = [""]*self.status_rows
        self.curkey = 0
        
        """
        initialize window
        """
        self.stdscr = stdscr
        # Don't print what I type on the terminal
        curses.noecho()
        # React to every key press, not just when pressing "enter"
        curses.cbreak()
        # Enable easy key codes
        self.stdscr.keypad(True)
        # Start colors in curses
        curses.start_color()
        curses.init_pair(99, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(98, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(97, curses.COLOR_BLACK, curses.COLOR_WHITE)
        # max width and height
        self.height, self.width = stdscr.getmaxyx()
    
    """
    print title and status
    """
    def show(self):
        # title
        self.stdscr.attron(curses.color_pair(98))
        self.stdscr.attron(curses.A_BOLD)
        self.stdscr.addstr(0,0,self.title)
        self.stdscr.attroff(curses.color_pair(98))
        self.stdscr.attroff(curses.A_BOLD)
        # status
        self.stdscr.attron(curses.color_pair(97))
        for i in range(self.status_rows):
            self.stdscr.addstr(self.status_start+i,0,self.status[i])
            self.stdscr.addstr(self.status_start+i, len(self.status[i]), " " * (self.width - len(self.status[i]) - 1))
        self.stdscr.attroff(curses.color_pair(97))

    
    """
    add string to screen
    (row, col): coordinate where text to be added
    s: string to be added
    color: specify color for print; need the color initiated
    """
    def add(self,row, col, s, color = None):
        if color is None:
            self.stdscr.addstr(row,col,s)
        else:
            self.stdscr.addstr(row,col,s,curses.color_pair(color))
    
    """
    return current key
    """
    def key(self):
        return self.curkey
    
    """
    get new key
    """
    def newKey(self):
        self.curkey = self.stdscr.getch()
        
    """
    set title string
    """
    def set_title(self,s):
        self.title = s
    
    """
    set status string
    """
    def set_status(self,s,i):
        self.status[i] = s
    
    
    """
    refresh screen
    """
    def erase(self):
        self.stdscr.erase()
    
    """
    let Game decide how to print
    """
    def printGame(self,Game):
        Game.print_to_window(self)
    
    
    """
    close window
    """
    def closeWindow(self):
        # reverse all changes
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

# part of the code referred from: https://gist.github.com/claymcleod/b670285f334acd56ad1c
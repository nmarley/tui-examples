import curses

def main(stdscr):
    # Disable cursor and initialize color
    curses.curs_set(0)
    stdscr.clear()

    # Get screen dimensions
    height, width = stdscr.getmaxyx()

    # Create a basic centered window
    message = "Press 'q' to Exit"
    x = width // 2 - len(message) // 2
    y = height // 2
    stdscr.addstr(y, x, message)

    # Refresh to display the content
    stdscr.refresh()

    # Wait for user input to exit
    while True:
        key = stdscr.getch()
        if key == ord('q'):  # Exit on 'q' key press
            break

if __name__ == "__main__":
    curses.wrapper(main)

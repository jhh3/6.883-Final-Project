import random


class MindReader(object):
    def __init__(self):
        self.prediction = self.flip()
        self.computer_score = self.player_score = 0
        self.losing_streak = 0

        # history
        self.history = [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]
        self.lw2 = self.lw1 = 0

    def flip(self):
        if random.random() > 0.5:
            return 1
        else:
            return 0

    def score(self):
        return "Computer {}, Player {}".format(self.computer_score, self.player_score)

    def take_turn(self, player_choice):
        if player_choice == self.prediction:
            self.computer_score += 1
            self.losing_streak = 0
        else:
            self.player_score += 1
            self.losing_streak += 1

        tmp = int(self.history[self.lw2][self.lw1][0] == player_choice)
        self.history[self.lw2][self.lw1][1] = tmp
        self.history[self.lw2][self.lw1][0] = player_choice
        self.lw2 = self.lw1
        self.lw1 = player_choice

        if self.history[self.lw2][self.lw1][1] == 1 and self.losing_streak < 2:
            self.prediction = self.history[self.lw2][self.lw1][0]
        else:
            self.prediction = self.flip()

        print self.prediction

if __name__ == "__main__":
    import curses
    mr_machine = MindReader()
    stdscr = curses.initscr()
    curses.cbreak()
    curses.curs_set(0)
    stdscr.keypad(1)

    stdscr.refresh()

    key = ''
    while key != ord('q'):
        stdscr.refresh()
        stdscr.addstr(0, 0, "Left = 0, Right = 1. Hit 'q' to quit.")
        key = stdscr.getch()
        if key == curses.KEY_LEFT:
            pressed = "0"
            mr_machine.take_turn(0)
        elif key == curses.KEY_RIGHT:
            pressed = "1"
            mr_machine.take_turn(1)
        else:
            continue

        stdscr.addstr(2, 10, "Last entered %s" % pressed)
        stdscr.addstr(4, 10, mr_machine.score())
        stdscr.clrtoeol()
        stdscr.refresh()

    curses.endwin()

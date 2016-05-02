import random


class SEER(object):
    def __init__(self):
        self.prediction = self.flip()
        self.last_play = 0
        self.last_last_play = 0
        self.state = [[[0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0]]]
        self.player_score = 0
        self.computer_score = 0
        self.last_prediction = 0
        self.last_prediction = 0

    def flip(self):
        if random.random() > 0.5:
            return 1
        else:
            return 0

    def follow_advice_3to1(self):
        if random.random() > 0.75:
            return 1
        else:
            return 0

    def score(self):
        return "Computer {}, Player {}".format(self.computer_score, self.player_score)

    def take_turn(self, player_input):
        cur_state = self.state[self.last_play][self.last_last_play]
        print cur_state
        if player_input == self.prediction:
            self.computer_score += 1
            if self.prediction == cur_state[2]:
                self.state[self.last_play][self.last_last_play][3] = min(3, cur_state[3] + 1)
            else:
                self.state[self.last_play][self.last_last_play][3] = max(-3, cur_state[3] - 1)
        else:
            self.player_score += 1
            if self.prediction == cur_state[2]:
                self.state[self.last_play][self.last_last_play][3] = max(-3, cur_state[3] - 1)
            else:
                self.state[self.last_play][self.last_last_play][3] = min(3, cur_state[3] + 1)
        self.state[self.last_play][self.last_last_play][0] = cur_state[1]
        self.state[self.last_play][self.last_last_play][1] = int(player_input == self.prediction)
        self.last_last_play = self.last_play
        self.last_play = player_input

        # Make next prediction
        advice = self.state[self.last_play][self.last_last_play]
        print advice
        lost_streak = advice[0] + advice[1]
        self.last_prediction = self.prediction
        if lost_streak == 0:
            self.prediction = self.flip()
        else:
            if advice[3] > 0:
                self.prediction = advice[2]
            elif advice[3] == 0:
                self.prediction = self.flip()
            else:
                self.prediction = abs(advice[2] - 1)
            if lost_streak == 1:
                if not self.follow_advice_3to1():
                    self.prediction = abs(self.prediction - 1)

if __name__ == "__main__":
    import curses
    seer_bot = SEER()
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
            seer_bot.take_turn(0)
        elif key == curses.KEY_RIGHT:
            pressed = "1"
            seer_bot.take_turn(1)
        else:
            continue

        stdscr.addstr(2, 10, "Last entered %s" % pressed)
        stdscr.addstr(4, 10, seer_bot.score())
        stdscr.clrtoeol()
        stdscr.refresh()

    curses.endwin()

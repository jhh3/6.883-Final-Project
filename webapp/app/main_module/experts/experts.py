import random
import math


class ExpertsCombo(object):
    def __init__(self, experts):
        self.computer_score = self.player_score = 0
        self.experts = experts
        self.weights = [0.5] * len(experts)

        self.prediction = self.get_prediction()

    def get_prediction(self):
        prob = 0
        for i, expert in enumerate(self.experts):
            prob += self.weights[i] * expert.prediction
        prob = prob / sum(self.weights)
        return random.random() < prob

    def take_turn(self, player_input):
        if self.prediction == player_input:
            self.computer_score += 1
        else:
            self.player_score += 1

        # Experts take turn
        for expert in self.experts:
            expert.take_turn(player_input)

        # Update weights
        exp_pieces = [math.exp(-expert.player_score) for expert in self.experts]
        denom = sum(exp_pieces)
        self.weights = [x / denom for x in exp_pieces]

        # Make next prediction
        self.prediction = self.get_prediction()

    def score(self):
        return "Computer {}, Player {}".format(self.computer_score, self.player_score)

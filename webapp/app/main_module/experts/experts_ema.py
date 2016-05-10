import random


class ExpertsEMA(object):
    def __init__(self, experts, alpha):
        self.computer_score = self.player_score = 0
        self.experts = experts
        self.weights = [0.5] * len(experts)
        self.alpha = alpha

        self.prediction = self.get_prediction()

    def get_prediction(self):
        prob = 0
        for i, expert in enumerate(self.experts):
            prob += self.weights[i] * expert.prediction
        prob = prob / sum(self.weights)
        return random.random() < prob

    def take_turn(self, player_input):
        experts_results = [int(expert.prediction == player_input) for expert in self.experts]
        if self.prediction == player_input:
            self.computer_score += 1
        else:
            self.player_score += 1

        # Update weights
        for i, result in enumerate(experts_results):
            self.weights[i] = self.alpha * result + (1 - self.alpha) * self.weights[i]

        # Experts take turn
        for expert in self.experts:
            expert.take_turn(player_input)

        # Make next prediction
        self.prediction = self.get_prediction()

    def score(self):
        return "Computer {}, Player {}".format(self.computer_score, self.player_score)

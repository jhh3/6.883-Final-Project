from mind_reading_machine.mind_reader import MindReader
from seer.seer import SEER
from experts.experts import ExpertsCombo
from experts.experts_ema import ExpertsEMA
import numpy as np
import matplotlib.pyplot as plt

# Read in data
john_data_path = "../data/john.data"
with open(john_data_path, 'r') as f:
    data = [int(c) for c in f.read().replace('\n', '')]

# Run trials to compute average bot performance
# Record bot score / total runs in results
rounds = 10
shannon_results_john = []
hagel_results_john = []
expert_results_john = []
expert_ema_results_john = []

for r in xrange(rounds):
    # Performance of bots
    shannon_bot = MindReader()
    hagel_bot = SEER()
    expert_bot = ExpertsCombo([MindReader(), SEER()])
    expert_ema_bot = ExpertsEMA([MindReader(), SEER()], 0.9)
    for human_guess in data:
        shannon_bot.take_turn(human_guess)
        hagel_bot.take_turn(human_guess)
        expert_bot.take_turn(human_guess)
        expert_ema_bot.take_turn(human_guess)
    shannon_results_john.append(shannon_bot.computer_score / (1.0 + len(data)))
    hagel_results_john.append(hagel_bot.computer_score / (1.0 + len(data)))
    expert_results_john.append(expert_bot.computer_score / (1.0 + len(data)))
    expert_ema_results_john.append(expert_ema_bot.computer_score / (1.0 + len(data)))

means_john = []
means_john.append(np.mean(shannon_results_john))
means_john.append(np.mean(hagel_results_john))
means_john.append(np.mean(expert_results_john))
means_john.append(np.mean(expert_ema_results_john))
stds_john = []
stds_john.append(2 * np.std(shannon_results_john))
stds_john.append(2 * np.std(hagel_results_john))
stds_john.append(2 * np.std(expert_results_john))
stds_john.append(2 * np.std(expert_ema_results_john))


# Plot bar graph of bot performance
nbots = 4
ind = np.arange(nbots)
bar_width = 0.5

fig, ax = plt.subplots()

rect_john = ax.bar(ind, means_john,
                   bar_width,
                   color='MediumSlateBlue',
                   yerr=stds_john,
                   error_kw={'ecolor': 'Tomato',
                             'linewidth': 2})

axes = plt.gca()
axes.set_ylim([0, 1.1])
axes.set_xlim([-bar_width, nbots - 1 + 2 * bar_width])

ax.set_ylabel('Score (computer score / total predictions)')
ax.set_title('Bot sequence prediction scores')
ax.set_xticks(ind + bar_width / 2)
ax.set_xticklabels(('Shannon', 'Hagelbarger', 'Experts', 'Experts (EMA)'))

ax.legend((rect_john[0], ), ('John\'s Data', ))


def auto_label(rects):
    """Label bars"""
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height, "%.2f" %
                height, ha='center', va='bottom')

auto_label(rect_john)

plt.show()

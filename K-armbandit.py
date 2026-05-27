import numpy as np
import sys
import time
import csv
import matplotlib.pyplot as plt

rng = np.random.default_rng()
class Bandit():
    def __init__(self, name):
        self.name = name
        self.successes = 0
        self.trials = 0
        self.estimate = 0

    def update(self, reward):
        self.trials += 1
        self.successes += reward
        self.estimate += (reward - self.estimate) / self.trials
class KArmedBandit():

    def __init__(self, data, labels, epsilon, threshold):
        self.data = data
        self.labels = labels
        self.epsilon = epsilon
        self.threshold = threshold
        self.bandits = [Bandit(label) for label in labels]

    def select_arm(self):
        if rng.random() < self.epsilon:
            return rng.integers(0, len(self.bandits))
        else:
            estimates = [b.estimate for b in self.bandits]
            return np.argmax(estimates)

    def train(self, train_data):
        for row in train_data:
            arm = self.select_arm()
            value = float(row[arm])
            reward = 1 if value < self.threshold else 0
            self.bandits[arm].update(reward)

    def best_arm(self):
        estimates = [b.estimate for b in self.bandits]
        return np.argmax(estimates)

    def test(self, test_data, best_arm):
        successes = 0
        history = []

        for i, row in enumerate(test_data):
            value = float(row[best_arm])
            reward = 1 if value < self.threshold else 0
            successes += reward
            history.append(successes / (i+1))

        return successes / len(test_data), history

def load_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    labels = data[0]
    rows = data[1:]
    return labels, rows


def split_data(data, train_percent):
    n = len(data)
    split = int(n * train_percent / 100)
    return data[:split], data[split:]

def print_results(labels, bandits, best_idx, success_rate, epsilon, train_percent, threshold):

    print("Omidi, Romina, AXXXXXXXX solution:")
    print("epsilon:", epsilon)
    print("Training data percentage:", train_percent, "%")
    print("Success threshold:", threshold)
    print()

    print("Success probabilities:")
    for i, b in enumerate(bandits):
        print(f"P({labels[i]}) = {round(b.estimate, 4)}")

    print()
    print(f"Bandit [{labels[best_idx]}] was chosen to be played for the rest of data set.")
    print(f"{labels[best_idx]} Success percentage:", round(success_rate, 4))

def plot_results(history, epsilon, train_percent):

    x = list(range(1, len(history)+1))

    plt.figure()
    plt.plot(x, history, label=f"e={epsilon}, train={train_percent}")

    plt.xlabel("Time (rows)")
    plt.ylabel("Cumulative Success Rate")
    plt.title("Bandit Performance")
    plt.legend()
    plt.grid(True)

    filename = f"plot_e{epsilon}_t{train_percent}.png"
    plt.savefig(filename, dpi=200, bbox_inches="tight")
    plt.close()

    print("Plot saved:", filename)


def main():

    if len(sys.argv) != 5:
        print("ERROR: Not enough or too many input arguments.")
        sys.exit()

    filename = sys.argv[1]
    epsilon = float(sys.argv[2])
    train_percent = int(sys.argv[3])
    threshold = float(sys.argv[4])

    # Validate
    if epsilon < 0 or epsilon > 1:
        epsilon = 0.3

    if train_percent < 0 or train_percent > 50:
        train_percent = 50

    labels, data = load_csv(filename)
    train_data, test_data = split_data(data, train_percent)

    t1 = time.time()

    bandit = KArmedBandit(data, labels, epsilon, threshold)
    bandit.train(train_data)

    best_idx = bandit.best_arm()
    success_rate, history = bandit.test(test_data, best_idx)

    t2 = time.time()

    print_results(labels, bandit.bandits, best_idx,
                  success_rate, epsilon, train_percent, threshold)

    print("Execution time:", round(t2 - t1, 4), "seconds")

    plot_results(history, epsilon, train_percent)


if __name__ == "__main__":
    main()

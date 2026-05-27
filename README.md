# CS581 Programming Assignment 03: K-Armed Bandit

This project implements and evaluates an **epsilon-greedy K-Armed Bandit algorithm** using time-series data from a CSV file. The algorithm learns the estimated probability of success for each available bandit during a training phase, then selects the best-performing bandit to use for the remaining test data.

## Project Overview

The multi-armed bandit problem is a classic machine learning problem where a decision-maker must choose between multiple actions, called **arms** or **bandits**, while learning which action gives the best reward over time.

In this project, each column in the input CSV file represents one bandit. For the provided example dataset, each bandit represents a WiFi channel, and each row contains a signal-strength value in dBm. A channel is considered successful when its value is below a given threshold, meaning the channel is not occupied and can be used without causing interference.

## Objective

The main objective is to:

- Implement the epsilon-greedy K-Armed Bandit algorithm
- Estimate the probability of success for each bandit
- Select the best bandit after training
- Evaluate the chosen bandit on the remaining test data
- Compare performance across different epsilon and training-percentage values

## Algorithm

This project uses the **epsilon-greedy** approach:

- With probability `epsilon`, the algorithm explores by choosing a random bandit.
- With probability `1 - epsilon`, the algorithm exploits by choosing the bandit with the highest estimated success probability.

This balances exploration of different bandits with exploitation of the best-known bandit.

## Input File

The program accepts a CSV file as input.

Requirements:

- The first row must contain column labels.
- Each column represents one bandit.
- Each row after the header contains time-series values.
- The program should work with different numbers of rows and columns.
- The input file must be in the same folder as the Python code.

Example input format:

```csv
Channel1,Channel2,Channel3,...,ChannelN
-91,-88,-94,...,-90
-89,-92,-95,...,-87
...
```

## Command-Line Usage

Run the program using:

```bash
python cs581_P03_A20569321.py FILENAME EPSILON TRAIN_PERCENT THRESHOLD
```

Example:

```bash
python cs581_P03_A20569321.py input.csv 0.3 30 -90
```

## Arguments

| Argument | Description |
|---|---|
| `FILENAME` | Name of the input CSV file |
| `EPSILON` | Exploration probability for epsilon-greedy learning |
| `TRAIN_PERCENT` | Percentage of the dataset used for training |
| `THRESHOLD` | Success threshold |

### Parameter Rules

- `EPSILON` must be a real number in `[0, 1]`.
  - If an invalid value is provided, it is set to `0.3`.
- `TRAIN_PERCENT` must be an integer in `[0, 50]`.
  - If an invalid value is provided, it is set to `50`.
- `THRESHOLD` is used to determine success.
  - For WiFi channel data, a value such as `-90` can be used.
  - This value should not be hardcoded.

If the number of command-line arguments is incorrect, the program prints:

```text
ERROR: Not enough or too many input arguments.
```

## Success Definition

For each bandit value:

```text
success = value < threshold
failure = value >= threshold
```

For the WiFi example, success means the selected channel is unoccupied and can be used without interference.

## Program Output

The program prints the results in the following format:

```text
Omidi, Romina, A20569321 solution:
epsilon: 0.3
Training data percentage: 30 %
Success threshold: -90
Success probabilities:
P(LABEL1) = ...
P(LABEL2) = ...
...
Bandit [LABELX] was chosen to be played for the rest of data set.
LABELX Success percentage: ...
```

## Experimental Setup

The algorithm was tested using multiple combinations of:

- `epsilon`: `0.1` to `0.9`
- training percentage: `10`, `20`, `30`, `40`, and `50`

Each parameter combination was run three times to account for randomness in the epsilon-greedy algorithm.

The success threshold was kept fixed during the experiments.

## Results Summary

The algorithm achieved very high success rates across most parameter settings. Most final success rates were close to `1.0`, showing that the epsilon-greedy method was effective at identifying a strong bandit.

Key observations:

- Small training percentages, especially `10%`, sometimes produced less stable results.
- Larger training percentages, especially `40%` and `50%`, produced more consistent success rates.
- Very low epsilon values sometimes underperformed because the algorithm did not explore enough.
- Medium epsilon values, especially around `0.3` to `0.6`, gave strong and stable results.
- High epsilon values also performed well, but they did not significantly improve over medium epsilon values.

## Best Parameter Range

The best performance was usually achieved with:

```text
epsilon: 0.3 to 0.6
training percentage: 40% to 50%
```

These settings provided a good balance between exploration and exploitation while giving the algorithm enough training data to estimate bandit success probabilities accurately.

## Plots

The report includes cumulative success-rate plots for selected parameter settings:

- `epsilon = 0.3`, `train = 50`
- `epsilon = 0.5`, `train = 50`
- `epsilon = 0.8`, `train = 50`

The plots show how the cumulative success rate changes over time after the training phase.

## Conclusion

The epsilon-greedy K-Armed Bandit algorithm performed well on the provided time-series dataset. In most cases, it successfully identified a high-performing bandit and achieved a final success rate close to `1.0`.

The results show that both exploration and training size matter. Too little exploration or too little training can lead to unstable performance, while moderate exploration with enough training data gives the most reliable results.

## Repository Structure

```text
.
├── cs581_P03_A20569321.py      # Main Python implementation
├── input.csv                   # Input dataset
├── README.md                   # Project documentation
└── results/                    # Optional folder for plots and experiment outputs
```

## Technologies Used

- Python
- CSV file processing
- Randomized epsilon-greedy learning
- Matplotlib for plotting cumulative success rate

## Author

**Romina Omidi**  
CS 581 Spring 2026  
Illinois Institute of Technology


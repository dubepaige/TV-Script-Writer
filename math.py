from scipy.stats import binomtest

# Example: human got 12 correct out of 20 trials
num_correct = 11
num_trials = 20

# chance level = 50%
result = binomtest(num_correct, num_trials, p=0.5, alternative='two-sided')

print("p-value:", result.pvalue)
if result.pvalue < 0.05:
    print("Significantly above chance: model is distinguishable")
else:
    print("Not significantly above chance: model passes indistinguishability test")

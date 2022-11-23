import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def min_max_normalization(arr):
    min_value = arr.min()
    max_value = arr.max()

    return (arr - min_value) / (max_value - min_value)

def plot_data(x, y, title, output_path):
    plt.figure()
    plt.plot(x, y)
    plt.title(title)
    plt.savefig(output_path)

raw_data = pd.read_csv("railway.csv")

lengths = np.array(raw_data["Length"], dtype=int)
passengers = np.array(raw_data["Passenger"], dtype=int)

normalized_lengths = min_max_normalization(lengths)
normalized_passengers = min_max_normalization(passengers)

plot_data(lengths, passengers, "RAW", "railway_raw.png")
plot_data(normalized_lengths, normalized_passengers, "NORMALIZED", "railway_normalized.png")
print(lengths)
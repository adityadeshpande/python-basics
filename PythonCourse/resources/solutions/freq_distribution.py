import numpy as np
import pandas as pd

scores = [
    79, 88, 75, 60, 93, 71, 59, 85, 42, 17,
    84, 75, 82, 68, 90, 62, 88, 76, 31, 5,
    65, 75, 87, 74, 62, 95, 78, 63, 48, 23,
    78, 82, 75, 91, 77, 69, 74, 68, 9, 36,
    67, 73, 81, 72, 63, 76, 75, 85, 27, 44,
    80, 73, 57, 88, 78, 62, 76, 53, 12, 39,
    62, 67, 97, 78, 85, 76, 65, 71, 3, 49,
    78, 89, 61, 75, 95, 60, 79, 83, 18, 45
]

# Define bins (0-100 with step of 5)
bins = np.arange(0, 105, 5)  
labels = [f"{i}-{i+4}" for i in bins[:-1]]  

# Compute frequency distribution
freq, _ = np.histogram(scores, bins=bins)

# Create DataFrame
df = pd.DataFrame({"Range": labels, "Frequency": freq})

# Compute Cumulative and Normalized Frequency
df["Cumulative Frequency"] = df["Frequency"].cumsum()
df["Normalized Frequency"] = df["Frequency"] / len(scores)

# Display the table
print(df)

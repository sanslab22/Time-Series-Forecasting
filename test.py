import kagglehub
import pandas as pd
import os

# Download latest version
dir_path = kagglehub.dataset_download("asaniczka/median-and-avg-hourly-wages-in-the-usa-1973-2022")

print("\nPath to dataset folder:", dir_path, "\n")
print("Files in directory:", os.listdir(dir_path), "\n")

path = os.path.join(dir_path, "median_average_wages.csv")


# Load csv
df = pd.read_csv(path)

print(f'Num of rows: {df.shape[0]}')
print(f'Num of cols: {df.shape[1]}\n')





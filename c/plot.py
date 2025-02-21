import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("timing.txt")
n_values = sorted(df["n"].unique())
plt.figure(figsize=(10, 6))
for n in n_values:
    df_n = df[df["n"] == n]
    plt.plot(df_n["m"], df_n["time"], marker="o", label=f"n = {n}")
plt.xlabel("Number of rows (m)")
plt.ylabel("Time taken (seconds)")
plt.title("Time vs. Number of Rows")
plt.xscale("log")
plt.legend()
plt.grid(True, which="both", ls="--")
plt.tight_layout()
plt.savefig("timing.png")

import math
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    path = Path("datasaurus_all.csv")
    if not path.exists():
        raise FileNotFoundError(path)

    df = pd.read_csv(path)
    print("Available columns:", df.columns.tolist())
    dino = df[df["shape"] == "dino"].copy()
    summary = {
        "count": len(dino),
        "x_mean": dino["x"].mean(),
        "y_mean": dino["y"].mean(),
        "x_std": dino["x"].std(),
        "y_std": dino["y"].std(),
        "x_min": dino["x"].min(),
        "x_max": dino["x"].max(),
        "y_min": dino["y"].min(),
        "y_max": dino["y"].max(),
    }

    print("Dino shape summary:")
    for key, value in summary.items():
        if isinstance(value, float):
            value = round(value, 3)
        print(f"  {key}: {value}")

    fig, ax = plt.subplots(constrained_layout=True)
    ax.scatter(
        dino["x"],
        dino["y"],
        s=36,
        c="#0f172a",
        edgecolor="#dbeafe",
        linewidth=0.8,
        alpha=0.9,
    )
    ax.set_title("Datasaurus Dino", fontsize=16, weight="semibold")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_aspect("equal")
    ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.5)
    fig.savefig("dino_scatter.png", dpi=200)
    print("Saved scatter plot to dino_scatter.png")


if __name__ == "__main__":
    main()

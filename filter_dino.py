from pathlib import Path

import pandas as pd


def main() -> None:
    df = pd.read_csv("datasaurus_all.csv")
    dino = df[df["shape"] == "dino"]
    dino.to_csv("datasaurus_dino.csv", index=False)
    print(f"Saved {len(dino)} rows to datasaurus_dino.csv")


if __name__ == "__main__":
    main()

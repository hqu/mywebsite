import json
from pathlib import Path

import pandas as pd


def main() -> None:
    path = Path("datasaurus_dino.csv")
    df = pd.read_csv(path)
    data = df.to_dict(orient="records")
    out_path = Path("dino_data.json")
    out_path.write_text(json.dumps(data))
    print(f"wrote {out_path}")


def echo_json_string() -> None:
    path = Path("dino_data.json")
    encoded = json.dumps(path.read_text())
    print(encoded)


if __name__ == "__main__":
    main()
    echo_json_string()

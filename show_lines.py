from pathlib import Path


def main() -> None:
    text = Path("index.html").read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(text, start=1):
        print(f"{i}: {line}")


if __name__ == "__main__":
    main()

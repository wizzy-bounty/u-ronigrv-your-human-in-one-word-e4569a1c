import os


WORD = "escalator"


def write_entry(output_dir: str) -> None:
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as entry_file:
        entry_file.write(WORD)


def main() -> None:
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()

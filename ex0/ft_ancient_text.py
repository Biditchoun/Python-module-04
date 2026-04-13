import sys


def open_file(name: str) -> None:
    print(f"Accessing file '{name}'")
    try:
        file = open(name)
    except Exception as err:
        print(f"Error opening file '{name}': {err}\n")
        return
    print(f"---\n\n{file.read()}---")
    file.close
    print(f"File '{name}' closed.")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>\n")
    else:
        open_file(sys.argv[1])

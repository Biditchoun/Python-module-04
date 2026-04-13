import sys


def open_file(name: str) -> str:
    print(f"Accessing file '{name}'")
    try:
        file = open(name)
    except Exception as err:
        sys.stderr.write(f"[STDERR] Error opening file '{name}': {err}\n")
        return ""
    rt = file.read()
    print(f"---\n\n{rt}---")
    file.close
    print(f"File '{name}' closed.\n")
    return rt


def files_training(av: list) -> None:
    print("=== Cyber Archives Recovery ===")
    if len(av) == 1:
        sys.stderr.write("[STDERR]Usage: ft_ancient_text.py <file>\n")
        return
    content = open_file(sys.argv[1])
    if content == "":
        return
    content = content.replace("\n", "#\n")
    content = content.replace("#\n#\n", "#\n\n")
    print("Transform data:")
    print(f"---\n\n{content}---")
    print("Enter new file name (or empty): ", end="")
    name = sys.stdin.readline()
    name = name.replace("\n", "")
    if name == "":
        print("Not saving data")
        return
    print(f"Saving data to '{name}'")
    try:
        file = open(name, "w")
    except Exception as err:
        sys.stderr.write(f"[STDERR] Error opening file '{name}': {err}\n")
        print("Not saving data")
        return
    file.write(content)
    print(f"Data saved in file '{name}'.")


if __name__ == "__main__":
    files_training(sys.argv)

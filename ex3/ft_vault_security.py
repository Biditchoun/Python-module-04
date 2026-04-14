def secure_archive(name: str, access: str = "r", to_write: str = "") -> tuple:
    try:
        file = open(name, access)
    except Exception as err:
        return (False, f"{err}")
    with file:
        if access == "r":
            return (True, file.read())
        file.write(to_write)
        return (True, "Content successfully written to file")


def with_training() -> None:
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    rt = secure_archive("/not/existing/file")
    print(rt)
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    rt = secure_archive("passwd")
    print(rt)
    print("\nUsing 'secure_archive' to read from a regular file:")
    rt = secure_archive("ancient_fragment.txt")
    print(rt)
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    rt = secure_archive("new_fragment.txt", "w", rt[1])
    print(rt)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    with_training()

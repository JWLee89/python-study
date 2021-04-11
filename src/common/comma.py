def list_comma() -> None:
    a_list = ["Michael " "Jackson", "John", "Brown"]
    print(f"What is wrong with the following? {a_list}")
    print(f"Python performed string concatenation because we forgot a comma")
    a_list_better = [
        "Michael",
        "Jackson",   # Easier to spot missing comma and easier to read diffs on GitHub
        "John",
        "Brown"
    ]
    print(a_list_better)


if __name__ == "__main__":
    list_comma()

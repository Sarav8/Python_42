import sys

def ft_command_quest():
    print("=== Command Quest ===")
    total = len(sys.argv)
    if (total <= 1):
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {total - 1}")
    i = 1
    while i < total:
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1
    print(f"Total arguments: {total}")

if __name__ == "__main__":
    ft_command_quest()


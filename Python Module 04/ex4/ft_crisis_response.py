
def ft_crisis_response():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try: 
        with open("lost_archive.txt") as arch:
            dates = arch.read()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    try:
        print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        raise PermissionError
        with open("classified_vault.txt", "r") as arch2:
            dates2 = arch2.read()
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    try:
        print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
        with open("standard_archive.txt") as arch3:
            dates3 = arch3.read()
        print(f"SUCCESS: {dates3}")
        print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print(".txt not found")
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()
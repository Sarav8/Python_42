def ft_ancient_fragment():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        arch = open("ancient_fragment.txt", "r")
        dates = arch.read()
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(dates)
        arch.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    ft_ancient_fragment()

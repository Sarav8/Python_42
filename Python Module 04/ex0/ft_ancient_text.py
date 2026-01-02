import os

def ft_ancient_fragment():
    
    arch = open("ancient_fragment.txt", "r")
    dates = arch.read()
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt")
    print("Connection established...\n")
    print("RECOVERED DATA:")
    print(dates)
    print("\nData recovery complete. Storage unit disconnected.")


if __name__== "__main__":
    ft_ancient_fragment()

def ft_vault_security():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    try:
        print("\nSECURE EXTRACTION:")
        with open("classified_data.txt", "r") as arch:
            dates = arch.read()
        print(dates)
    except FileNotFoundError:
        print("Error: .txt not found")
    print("\nSECURE PRESERVATION:")
    try:
        with open("security_protocols.txt", "w") as arch2:
            arch2.write("{[}CLASSIFIED{]} New security protocols archived\n")
        print("{[}CLASSIFIED{]} New security protocols archived")
        print("Vault automatically sealed upon completion\n")
    except PermissionError:
        print("Error")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    ft_vault_security()

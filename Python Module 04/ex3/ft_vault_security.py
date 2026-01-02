

def ft_vault_security():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    try:
        print("\nSECURE EXTRACTION:")
        with open("classified_data.txt") as arch:
            dates = arch.read()
        print(dates)
    except FileNotFoundError:
        print(".txt not found")
    print("\nSECURE PRESERVATION:")
    try:
        with open("security_protocols.txt") as arch2:
            dates2 = arch2.read()
        print(dates2)
    except FileNotFoundError:
        print(".txt not found")
    print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")
    
if __name__ =="__main__":
    ft_vault_security()
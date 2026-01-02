import os

def ft_archive_creation():

    with open("new_discovery.txt", "w") as arch:
        arch.write("{[}ENTRY 001{]} New quantum algorithm discovered\n")
        arch.write("{[}ENTRY 002{]} Efficiency increased by 347 %\n")
        arch.write("{[}ENTRY 003{]} Archived by Data Archivist trainee")
    try:
        with open("new_discovery.txt", "r") as arch:
            dates = arch.read()
        print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
        print("Initializing new storage unit: new_discovery.txt")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        print(dates)
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    print("\nData inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")

if __name__ == "__main__":
    ft_archive_creation()

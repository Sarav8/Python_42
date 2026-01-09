import sys


def ft_stream_management():
    sys.stdout.write("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n\n")

    sys.stdout.write("Input Stream active. Enter archivist ID: ")
    sys.stdout.flush()
    archivist_id = sys.stdin.readline().strip()

    sys.stdout.write("Input Stream active. Enter status report: ")
    sys.stdout.flush()
    status = sys.stdin.readline().strip()

    sys.stdout.write(
        f"\n{{[}}STANDARD{{]}} Archive status from {archivist_id}: {status}\n"
        )
    sys.stderr.write(
        "{[}ALERT{]} System diagnostic: Communication channels verified\n"
        )
    sys.stdout.write("{[}STANDARD{]} Data transmission complete\n")

    sys.stdout.write("\nThree-channel communication test successful.\n")


if __name__ == "__main__":
    ft_stream_management()

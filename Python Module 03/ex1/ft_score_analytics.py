import sys


def ft_score_analytics():
    print("=== Player Score Analytics ===")
    total = len(sys.argv)
    if total < 2:
        print(
            f"No scores provided. Usage: "
            f"python3 {sys.argv[0]} <score1> <score2> ..."
        )
    else:
        num_list = []
        i = 1
        while i < total:
            try:
                num = int(sys.argv[i])
                num_list.append(num)
            except ValueError:
                print("Error: score must be integer")
                return
            i += 1
        print(f"Scores processed: {num_list}")
        print(f"Total players: {total - 1}")
        print(f"Total score: {sum(num_list)}")
        print(f"Average score: {sum(num_list) / len(num_list)}")
        print(f"High score: {max(num_list)}")
        print(f"Low score: {min(num_list)}")
        print(f"Score range: {max(num_list) - min(num_list)}")


if __name__ == "__main__":
    ft_score_analytics()

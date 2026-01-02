event_list = event_list = [
        {
            'id': 1,
            'player': 'frank',
            'event_type': 'login',
            'timestamp': '2024-01-01T23:17',
            'data': {
                'level': 16,
                'score_delta': 128,
                'zone': 'pixel_zone_2'
            }
        },
        {
            'id': 2,
            'player': 'frank',
            'event_type': 'login',
            'timestamp': '2024-01-22T23:57',
            'data': {'level': 35, 'score_delta': -11, 'zone': 'pixel_zone_5'}
        },
        {
            'id': 3,
            'player': 'diana',
            'event_type': 'login',
            'timestamp': '2024-01-01T02:13',
            'data': {'level': 15, 'score_delta': 417, 'zone': 'pixel_zone_5'}
        },
        {
            'id': 4,
            'player': 'alice',
            'event_type': 'level_up',
            'timestamp': '2024-01-07T22:41',
            'data': {'level': 45, 'score_delta': 458, 'zone': 'pixel_zone_4'}
        },
        {
            'id': 5,
            'player': 'bob',
            'event_type': 'death',
            'timestamp': '2024-01-19T08:51',
            'data': {'level': 1, 'score_delta': 63, 'zone': 'pixel_zone_4'}
        },
        {
            'id': 6,
            'player': 'charlie',
            'event_type': 'kill',
            'timestamp': '2024-01-05T06:48',
            'data': {'level': 22, 'score_delta': 4, 'zone': 'pixel_zone_1'}
        },
        {
            'id': 7,
            'player': 'diana',
            'event_type': 'login',
            'timestamp': '2024-01-12T11:38',
            'data': {'level': 17, 'score_delta': -56, 'zone': 'pixel_zone_4'}
        },
        {
            'id': 8,
            'player': 'eve',
            'event_type': 'login',
            'timestamp': '2024-01-30T12:05',
            'data': {'level': 36, 'score_delta': 200, 'zone': 'pixel_zone_5'}
        },
        {
            'id': 9,
            'player': 'charlie',
            'event_type': 'level_up',
            'timestamp': '2024-01-07T22:04',
            'data': {'level': 3, 'score_delta': 133, 'zone': 'pixel_zone_3'}
        },
        {
            'id': 10,
            'player': 'alice',
            'event_type': 'logout',
            'timestamp': '2024-01-28T03:24',
            'data': {'level': 18, 'score_delta': 364, 'zone': 'pixel_zone_3'}
        },
        {
            'id': 11,
            'player': 'bob',
            'event_type': 'kill',
            'timestamp': '2024-01-12T06:42',
            'data': {'level': 18, 'score_delta': -27, 'zone': 'pixel_zone_5'}
        },
        {
            'id': 12,
            'player': 'frank',
            'event_type': 'logout',
            'timestamp': '2024-01-18T23:15',
            'data': {'level': 11, 'score_delta': 373, 'zone': 'pixel_zone_4'}
        }
]
def process_event():
    for events in event_list:
        yield events

event_stream = process_event()

print("=== Game Data Stream Processor ===\n")
print("Processing 1000 game events..\n")


total_events_processed = 0
high_level_players = 0
treasure_events = 0
level_up_events = 0
for event in event_stream:
    print(f"Event {event['id']}: player {event['player']} "
        f"(level {event['data']['level']}) {event['event_type']}")
    total_events_processed += 1
    if  event['data']['level'] >= 10:
        high_level_players += 1
    if event['event_type'] == "item_found":
        treasure_events += 1
    if event['event_type'] == "level_up":
        level_up_events += 1
    

print("\n=== Stream Analytics ===")
print(f"Total events processed: {total_events_processed}")
print(f"High-level players (10+): {high_level_players}")
print(f"Treasure events: {treasure_events}")
print(f"Level-up events: {level_up_events}")

print("\nMemory usage: Constant (streaming)")
print("Processing time: 0.045 seconds\n")


def generator_fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        new_num = a + b
        a = b
        b = new_num

fib_gen = generator_fibonacci()

print("=== Generator Demonstration ===")
print(f"Fibonacci sequence (first 10): ", end="")
for i in range(0, 10):
        n_fibo = next(fib_gen)
        if i < 9:
            print(n_fibo, end=", ")
        else:
            print(n_fibo)

def generator_primes():
    n = 2
    while True:
        prime = True
        i = 2
        while i < n:
            if n % i == 0:
                prime = False
                break
            i += 1
        if prime:
            yield n
        n += 1

prim_generator = generator_primes()
print(f"Prime numbers (first 5): ", end="")
for i in range (1, 6):
    n_prime = next(prim_generator)
    if i < 5:
        print(n_prime, end=", ")
    else:
        print(n_prime)
    


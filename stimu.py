import math
import time
import random

def is_prime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    limit = int(math.sqrt(x)) + 1
    for i in range(3, limit, 2):
        if x % i == 0:
            return False

    return True

def find_primes_in_time_limit(time_limit):
    start_time = time.time()
    prime_numbers = []
    while time.time() - start_time < time_limit:
        # Generate random values for 'a' and 'i'
        a = random.uniform(0.1, 10.0)  # Adjust the range as needed
        i = random.randint(1, 1000)

        # Calculate x(i/a)
        result = i / a
        if is_prime(int(result)):
            prime_numbers.append(int(result))

    random.shuffle(prime_numbers)  # Shuffle the prime numbers
    return prime_numbers

if __name__ == "__main__":
    time_limit = 60  # 1 minute time limit
    prime_numbers = find_primes_in_time_limit(time_limit)

    # Write prime numbers to prime.log
    with open('prime.log', 'w') as log_file:
        log_file.write(f"Prime numbers found, shuffled, and checked in {time_limit} seconds:\n")
        log_file.write(f"{prime_numbers}\n")
        log_file.write(f"Total prime numbers found: {len(prime_numbers)}\n")

    print("Prime numbers written to prime.log")

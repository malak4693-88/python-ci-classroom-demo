
import time
from price_calculator import calculate_total

def main():
    start = time.perf_counter()
    checksum = 0.0

    for i in range(50_000_000):
        result = calculate_total(
            unit_price=100.0,
            quantity=(i % 10) + 1,
            discount_percent=10.0
        )
        checksum += result

    elapsed = time.perf_counter() - start

    print(f"Checksum: {checksum:.2f}")
    print(f"Execution time: {elapsed:.3f} seconds")


if __name__ == "__main__":
    main()

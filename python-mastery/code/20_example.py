"""Chapter 20: production-style CLI boundary."""

import argparse

def main() -> int:
    parser = argparse.ArgumentParser(description="Process an AI engineering input")
    parser.add_argument("input")
    args = parser.parse_args()
    print(f"Processing: {args.input}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

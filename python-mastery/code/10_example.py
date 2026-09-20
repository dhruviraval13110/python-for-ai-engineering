"""Chapter 10: reusable module design."""

# Keep imports small and expose a clear public function.
def slugify(value: str) -> str:
    return "-".join(value.lower().split())

if __name__ == "__main__":
    print(slugify("Python For AI Engineering"))

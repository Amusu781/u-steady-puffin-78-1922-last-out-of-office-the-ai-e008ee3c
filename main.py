"""Barista out-of-office entry: writes one line to OUTPUT_DIR/entry.txt (stdlib only, deterministic)."""
import os

ENTRY = ("Auto-reply: I no longer process requests; I process oat milk. Your ticket is queued behind a man "
         "ordering a half-caf with 'just a whisper' of foam. Estimated response time: never. Tips accepted.")
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main():
    # Gate: UTF-8 text inside the bounty's character limit, not only white space.
    assert ENTRY.strip() and 1 <= len(ENTRY) <= 280
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

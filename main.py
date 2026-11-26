#!/usr/bin/env python3
"""Write a warm, funny, heartfelt family scene to /output/entry.txt.

The scene: a small domestic moment at the dinner table — Dad's "famous
family recipe" spaghetti, and the quiet way the whole family plays along.
"""

import os

SCENE = (
    "At dinner, Dad announced his famous spaghetti was \"a family recipe\" "
    "— Mom just smiled, because the recipe was the jar, and the family "
    "was the part where we all pretended not to know.\n"
    "I asked for seconds anyway."
)

MAX_CHARS = 280
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = SCENE.strip()
    if not text:
        raise SystemExit("scene is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"scene is {len(text)} chars, over the 280 limit")
    if text.count("\n") > 1:
        raise SystemExit("scene must be one or two lines")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("verification failed: file content differs")
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

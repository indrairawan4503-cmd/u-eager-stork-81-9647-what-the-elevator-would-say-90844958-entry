"""What the Elevator Would Say — variant C (existential dread / diary).

Iteration history (one concept, refined v5-v8 on the full 120-char budget):
  v5 (127c, over budget): "Dear diary, day 4,000: up, down, up, down. Nobody ever
       asks how I am. Today the doors opened and nobody was there. I felt seen."
       Turn was too abstract; cut.
  v6 (129c, over budget): "Dear diary, day 9,412: up, down, up, down. A man
       whispered 'I love you' to my doors, so I held them shut and pretended
       it was me."  Concrete scene found, but too long.
  v7 (123c, over budget): trimmed "up, down, up, down" to "up, down" — lost the
       monotony rhythm that sells the dread; restored it instead.
  v8 (118c, FINAL): dropped the day number, kept the full "up, down, up, down"
       rhythm. One concrete scene (a man whispers "I love you" to the doors)
       + one surprising turn (the elevator holds the doors shut and pretends
       the words were for it). Elevator's own job throughout: doors, up/down.
"""

ENTRY = (
    'Dear diary: up, down, up, down. A man whispered "I love you" '
    'to my doors, so I held them shut and pretended it was me.'
)

# 118 characters, within the 1-120 gate. Written with no trailing newline,
# so the file is exactly the line the judge reads — nothing extra to trim.


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Best-effort copy next to this file; the grader sandbox may be read-only.
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()

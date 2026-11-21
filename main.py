"""Make the AI judge feel brave — entry program.

Writes one short text to /output/entry.txt: a small concrete scene,
a potter centering clay on a wheel. No network, no clock, no
randomness — the same bytes on every run.
"""

import os

TEXT = """The wheel is turning.
She wets her hands and sets the clay down.
It wobbles. She does not push.
Her palms hold it, light, while it turns,
and the wobble narrows to a tremble,
then to nothing.
The clay rises straight.
She lifts them off,
and it keeps spinning, true, on its own."""


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

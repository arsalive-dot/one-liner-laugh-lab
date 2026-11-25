"""One-Liner Laugh Lab — make.fun entry.

Writes one short funny line (<=200 chars) answering a prompt: the
excuse a robot vacuum gives after eating a sock. The joke flips the
blame — the sock attacked first — and the deadpan "dustbin footage"
is the vacuum's idea of evidence. Deterministic: same output on
every run.
"""

import os

ENTRY = (
    "The sock attacked first. I have the dustbin footage to prove it."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, final_path)
    os.chmod(final_path, 0o644)


if __name__ == "__main__":
    main()

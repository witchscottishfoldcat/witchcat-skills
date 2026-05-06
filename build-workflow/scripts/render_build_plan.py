#!/usr/bin/env python3
"""Render a compact BUILD-mode micro plan scaffold."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a BUILD micro plan template.")
    parser.add_argument("--title", default="Feature", help="Plan title")
    parser.add_argument("--phases", type=int, default=2, help="Number of phases")
    parser.add_argument("--tdd", action="store_true", help="Include TDD pair task notes")
    args = parser.parse_args()

    print(f"[MICRO PLAN] {args.title}")
    for phase in range(1, args.phases + 1):
        print(f"Phase {phase} - <name>")
        print(f"  Task {phase}.1 | <name>")
        print("    Input    : <what it receives>")
        print("    Output   : <what it produces>")
        print("    Risk     : <domain risk addressed>")
        print("    Rollback : <how to undo>")
        print("    Flag     : <optional side effect or atomicity warning>")
        if args.tdd:
            print(f"  Task {phase}.2 | TDD pair - implementation for {phase}.1")
    print()
    print("Total tasks     : <N>")
    print("Can parallelize : <list>")


if __name__ == "__main__":
    main()

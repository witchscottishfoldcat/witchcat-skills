#!/usr/bin/env python3
"""Render a findings-first review scaffold."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Render an engineering review template.")
    parser.add_argument("--title", default="Review", help="Review title")
    args = parser.parse_args()

    print(f"Findings - {args.title}")
    print("1. [Severity] <file:line> - <problem and consequence>")
    print("2. [Severity] <file:line> - <problem and consequence>")
    print()
    print("Open questions")
    print("- <assumption or unknown>")
    print()
    print("Residual risk")
    print("- <remaining test gap or environment limitation>")


if __name__ == "__main__":
    main()

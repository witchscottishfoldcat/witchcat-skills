#!/usr/bin/env python3
"""Render a DEBUG workflow report scaffold."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a DEBUG report template.")
    parser.add_argument("--title", default="Bug Investigation", help="Report title")
    args = parser.parse_args()

    print(f"[DEBUG] {args.title}")
    print("1. Reproduce   : <exact steps to trigger the issue>")
    print("2. Trace       : <state transitions leading to failure>")
    print("3. Hypothesis  : <suspected root cause>")
    print("4. Validate    : <how the hypothesis was confirmed>")
    print("5. Fix         : <change made>")
    print("6. Regression  : <test added to prevent recurrence>")


if __name__ == "__main__":
    main()

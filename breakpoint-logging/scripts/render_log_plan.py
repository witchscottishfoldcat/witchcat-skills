#!/usr/bin/env python3
"""Render a breakpoint-style log instrumentation plan."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a log instrumentation plan template.")
    parser.add_argument("--title", default="Log Instrumentation", help="Plan title")
    args = parser.parse_args()

    print(f"[LOG PLAN] {args.title}")
    print("Question        : <what debugging question should the logs answer>")
    print("Entry Points     : <where execution enters the path>")
    print("Branch Points    : <which decisions matter>")
    print("Mutations        : <state changes to log before or after>")
    print("External Calls   : <I/O boundaries to instrument>")
    print("Failure Paths    : <exceptions, retries, timeouts, fallbacks>")
    print("Noise Controls   : <sampling, aggregation, or deliberate omissions>")
    print("Safe Fields      : <ids, counts, statuses to log>")


if __name__ == "__main__":
    main()

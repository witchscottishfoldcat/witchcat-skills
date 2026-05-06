#!/usr/bin/env python3
"""Render an architecture planning scaffold."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Render an ARCH plan template.")
    parser.add_argument("--title", default="Architecture Plan", help="Plan title")
    parser.add_argument("--modules", type=int, default=3, help="Number of module stubs")
    parser.add_argument("--phases", type=int, default=2, help="Number of micro-plan phases")
    args = parser.parse_args()

    print(f"[DOMAIN RISKS] {args.title}")
    print("Invariants       : <list>")
    print("Atomicity        : <list with boundary crossed>")
    print("Concurrency      : <list>")
    print("Side Effects     : <list with compensation strategy>")
    print("Trust Boundaries : <list>")
    print("Observability    : <what would be invisible without instrumentation>")
    print("Performance      : <hot paths, scale limits>")
    print("Top Risks        : <1-3 items max>")
    print()
    print("[ARCHITECTURE PLAN]")
    print("Modules")
    for index in range(1, args.modules + 1):
        print(f"  module-{index} : <responsibility> | does NOT own: <boundary>")
    print("Build Order")
    print("  A -> B -> C")
    print("Assumptions")
    print("  <conditions that, if wrong, invalidate this blueprint>")
    print()
    print("ADR-1")
    print("  Decision : <what>")
    print("  Context  : <why needed>")
    print("  Options  : <alternatives>")
    print("  Chosen   : <selected>")
    print("  Tradeoff : <gained vs sacrificed>")
    print("  Rollback : <revert plan>")
    print()
    print("[MICRO PLAN]")
    for phase in range(1, args.phases + 1):
        print(f"Phase {phase} - <name>")
        print(f"  Task {phase}.1 | <name>")
        print("    Input    : <what it receives>")
        print("    Output   : <what it produces>")
        print("    Risk     : <domain risk addressed>")
        print("    Rollback : <how to undo>")
        print("    Flag     : <optional atomicity or side-effect warning>")
    print()
    print("Total tasks     : <N>")
    print("Can parallelize : <list>")


if __name__ == "__main__":
    main()

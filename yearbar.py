#!/usr/bin/env python3

from datetime import date
import argparse
import shutil


def year_progress():
    today = date.today()
    day_of_year = today.timetuple().tm_yday

    year = today.year
    is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    total_days = 366 if is_leap else 365

    progress = day_of_year / total_days
    return year, day_of_year, total_days, progress


def render_bar(progress, width=30):
    filled = int(width * progress)
    empty = width - filled
    return "█" * filled + "░" * empty


def render_dots(progress, total=20):
    filled = int(total * progress)
    return " ".join(["●"] * filled + ["○"] * (total - filled))


def center(text):
    cols = shutil.get_terminal_size().columns
    return text.center(cols)


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--dots", action="store_true")
    parser.add_argument("--stats", action="store_true")
    parser.add_argument("--zen", action="store_true")
    parser.add_argument("-h", "--help", action="store_true")

    args = parser.parse_args()

    if args.help:
        print(
            "yearbar\n\n"
            "Flags:\n"
            "  --dots    Dot-based progress\n"
            "  --stats   Numerical stats\n"
            "  --zen     Minimal output\n"
        )
        return

    year, day, total, progress = year_progress()

    if args.stats:
        print(f"Year       : {year}")
        print(f"Day        : {day}")
        print(f"Days total : {total}")
        print(f"Days left  : {total - day}")
        print(f"Progress   : {progress:.2%}")
        return

    if args.dots:
        dots = render_dots(progress)
        print(center(dots))
        return

    bar = render_bar(progress)

    if args.zen:
        print(center(bar))
        return

    print(center(str(year)))
    print(center(f"[{bar}] {progress:.1%}"))
    print(center(f"Day {day} / {total}"))


if __name__ == "__main__":
    main()


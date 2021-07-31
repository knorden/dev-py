import csv
import argparse


def count_FINAL(url: str):
    with open(url, "r", encoding="utf-8") as fin_stats:
        count = 0
        for line in fin_stats:
            row = line.split(",")
            count += 1 if 'FINAL' in row else 0
        print(count)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="parses the filepath of a csv.")
    parser.add_argument("--file", help="You need to specify the name of the csv file.")
    args = parser.parse_args()
    filename = args.file

    count_FINAL(filename)

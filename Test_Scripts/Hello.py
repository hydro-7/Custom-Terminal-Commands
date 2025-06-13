import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name1", help="Your name")
parser.add_argument("name2", help="My name")

args = parser.parse_args()

print(f"Hello, {args.name1}!\n ~{args.name2}")

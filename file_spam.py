import os, argparse

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

file_path = args.file

with open(file_path, "r") as file:
    phones = file.read().split("\n")

for phone in phones:
    os.system("start python spamer.py " + phone)
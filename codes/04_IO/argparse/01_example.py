import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('num', help="an integer number", type=int)
args = parser.parse_args()
print(args.num)

import argparse

def create_probset(problems):

    for i in range(len(problems)):
        file_name = "prob_" + str(i+1) + ".cpp"
        print(file_name)
        # print("//  " + problems[i-1] + "\n#include<stdio.h>\n\nint main()\n{\n\n\treturn 0;\n}")
        
        with open(file_name, "w") as f:
            f.write("//  " + problems[i] + "\n#include<stdio.h>\n\nint main()\n{\n\n\treturn 0;\n}")

def get_probs(file_path):
    file = open(file_path, "r")
    problems = file.readlines()
    return problems

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--start", type=int)
args = parser.parse_args()

print(args.start)

start = args.start

file_path = "probset"
problems = get_probs(file_path)
# print(problems)
create_probset(problems)
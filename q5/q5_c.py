import ast
import os
res = 0
listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk('my-python-project'):
    for file in filenames:
        listOfFiles.append(os.path.join(dirpath, file))

for filename in listOfFiles:
    if filename.endswith(".py"):
        with open(filename) as f:
            text = f.read()
            tree = ast.parse(text)
            res += sum(isinstance(exp, ast.FunctionDef) for exp in tree.body)

print(res)
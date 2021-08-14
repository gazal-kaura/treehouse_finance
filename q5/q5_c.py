import ast
import os
res = 0
for filename in os.listdir('my-python-project'):
    if filename.endswith(".py"):
        print(filename)
        with open('my-python-project/' + filename) as f:
            tree = ast.parse(f.read())
            res += sum(isinstance(exp, ast.FunctionDef) for exp in tree.body)

print(res)
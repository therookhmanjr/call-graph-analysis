import ast

class CallVisitor(ast.NodeVisitor):
    def __init__(self):
        self.calls = []

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            self.calls.append(node.func.id)
        self.generic_visit(node)

def analyze_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())

    functions = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            visitor = CallVisitor()
            visitor.visit(node)
            functions[node.name] = visitor.calls

    return functions

if __name__ == "__main__":
    funcs = analyze_file("text_utils.py")
    for func, calls in funcs.items():
        print(f"{func} -> {calls}")

# phase3_parser.py

class DAXEvaluator:
    """Evaluates postfix DAX formulas using stack."""

    def evaluate_postfix(self, expression):
        stack = []
        tokens = expression.split()
        for token in tokens:
            if token.isdigit():
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+': stack.append(a+b)
                elif token == '-': stack.append(a-b)
                elif token == '*': stack.append(a*b)
                elif token == '/': stack.append(a/b)
        return stack[0] if stack else None
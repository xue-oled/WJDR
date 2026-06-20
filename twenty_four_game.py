def calculate_24(nums):
    """
    Given a list of four numbers, returns all possible expressions that evaluate to 24.
    """
    from itertools import permutations, product
    
    # All possible permutations of the input numbers
    perms = list(permutations(nums))
    
    # All possible combinations of arithmetic operations
    operations = list(product(['+', '-', '*', '/'], repeat=3))
    
    results = []
    
    # Try all possible permutations and operation combinations
    for perm in perms:
        for ops in operations:
            # Try different parenthesis combinations
            results.extend(try_all_parentheses(perm, ops))
    
    # Remove duplicate expressions
    return list(set(results))

def try_all_parentheses(numbers, operations):
    """
    Tries all possible parenthesis combinations for a given set of numbers and operations.
    Returns expressions that evaluate to 24.
    """
    results = []
    
    # Unpack numbers
    a, b, c, d = numbers
    
    # Unpack operations
    op1, op2, op3 = operations
    
    # Try different parenthesis combinations
    try:
        # No parentheses (left to right)
        expr = f"{a} {op1} {b} {op2} {c} {op3} {d}"
        if eval_valid(expr) == 24:
            results.append(expr)
            
        # (a op b) op c op d
        expr = f"({a} {op1} {b}) {op2} {c} {op3} {d}"
        if eval_valid(expr) == 24:
            results.append(expr)
            
        # a op (b op c) op d
        expr = f"{a} {op1} ({b} {op2} {c}) {op3} {d}"
        if eval_valid(expr) == 24:
            results.append(expr)
            
        # a op b op (c op d)
        expr = f"{a} {op1} {b} {op2} ({c} {op3} {d})"
        if eval_valid(expr) == 24:
            results.append(expr)
            
        # (a op b) op (c op d)
        expr = f"({a} {op1} {b}) {op2} ({c} {op3} {d})"
        if eval_valid(expr) == 24:
            results.append(expr)
            
        # ((a op b) op c) op d
        expr = f"(({a} {op1} {b}) {op2} {c}) {op3} {d}"
        if eval_valid(expr) == 24:
            results.append(expr)
            
        # (a op (b op c)) op d
        expr = f"({a} {op1} ({b} {op2} {c})) {op3} {d}"
        if eval_valid(expr) == 24:
            results.append(expr)
            
        # a op ((b op c) op d)
        expr = f"{a} {op1} (({b} {op2} {c}) {op3} {d})"
        if eval_valid(expr) == 24:
            results.append(expr)
            
        # a op (b op (c op d))
        expr = f"{a} {op1} ({b} {op2} ({c} {op3} {d}))"
        if eval_valid(expr) == 24:
            results.append(expr)
            
    except:
        # Skip any evaluation errors (like division by zero)
        pass
    
    return results

def eval_valid(expr):
    """
    Evaluates an expression safely, handling division by zero.
    """
    try:
        # Replace spaces with nothing for proper evaluation
        expr = expr.replace(' ', '')
        return eval(expr)
    except ZeroDivisionError:
        return float('inf')

def main():
    print("24点计算器")
    print("请输入4个数字（1-9），由程序找出所有可能的计算方式得到24：")
    
    while True:
        try:
            # Get user input
            numbers = list(map(int, input("请输入: ").split()))
            
            # Validate input
            if len(numbers) != 4:
                print("必须输入4个数字，请重新输入！")
                continue
                
            if any(num < 1 or num > 9 for num in numbers):
                print("数字必须在1-9之间，请重新输入！")
                continue
            
            # Calculate solutions
            solutions = calculate_24(numbers)
            
            if solutions:
                print(f"\n找到 {len(solutions)} 种计算方式得到24:")
                for solution in solutions:
                    print(f" - {solution}")
            else:
                print("\n没有找到可以得到24的计算方式。")
            
            # Ask if user wants to continue
            if input("\n再试一次? (y/n): ").lower() != 'y':
                break
                
        except Exception as e:
            print(f"发生错误: {e}")
            print("请重新输入！")

if __name__ == "__main__":
    main()
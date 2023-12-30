import inspect
import sys


def grab_input():
    '''grab txt file input from stdin'''
    numbers = []
    
    for line in sys.stdin:
        try:
            numbers.append(int(line.strip()))
        except ValueError:
            continue
    return numbers


def print_methods(obj):
    # Split items based on their types
    magic_methods = [x for x in dir(obj) if x.startswith("__") and x.endswith("__")]
    private_methods = [x for x in dir(obj) if x.startswith("_") and not x in magic_methods]
    public_methods = [x for x in dir(obj) if not x.startswith("_")]

    print("\n\033[93mMagic Methods:\033[0m")
    for item in sorted(magic_methods):
        print(f"    {item}")

    print("\n\033[93mPrivate Methods:\033[0m")
    for item in sorted(private_methods):
        print(f"    {item}")

    print("\n\033[93mPublic Methods:\033[0m")
    for item in sorted(public_methods):
        print(f"    {item}")


def cprint(expr, _globals=None, _locals=None):
    """
    Custom print function that prints the name of the variable/expression
    alongside its value.
    
    Parameters:
    - expr: The expression to evaluate.
    - _globals, _locals (dict, optional): Optional dictionaries to specify the namespace 
      for the evaluation. This allows the function to access variables outside of its 
      local scope.
    
    Example:
    x = 10
    cprint(x)
    # Output: x: 10
    """
    # Fetch the line of code that called cprint
    frame = inspect.currentframe().f_back
    # line = frame.f_code.co_filename, frame.f_lineno
    call_line = inspect.getframeinfo(frame).code_context[0].strip()

    # Extract the argument from the line
    arg_str = call_line[call_line.index('(') + 1:-1].strip()

    try:
        value = expr
        # print(f"{arg_str}: {value}")
        print(f"\033[93m{arg_str}\033[0m: \n{value}\n")
    except Exception as e:
        print(f"Error evaluating {arg_str}: {e}")


def cprint_str(expr, globals=None, locals=None):
    """
    Custom print function that prints the name of the variable/expression
    alongside its value.

    Parameters:
    - expr (str): The expression to evaluate as a string.
    - globals, locals (dict, optional): Optional dictionaries to specify the namespace
      for the evaluation. This allows the function to access variables outside of its
      local scope.

    Example:
    x = 10
    cprint_str("x")
    # Output: x: 10
    """
    try:
        # Evaluate the expression
        value = eval(expr, globals, locals)
        print(f"\033[93m{expr}\033[0m: \n{value}\n")
    except Exception as e:
        print(f"Error evaluating {expr}: {e}")


# import torch 

# def count_unique(tensor):
#     # Calculate unique values and their counts
#     unique_values, counts = torch.unique(tensor, return_counts=True)

#     # Convert unique_values to a Python list
#     unique_values = unique_values.tolist()

#     # Convert counts to a Python list
#     counts = counts.tolist()

#     # Print the unique values and their counts
#     for value, count in zip(unique_values, counts):
#         print(f"Value: {value}, Count: {count}")
# 
#     print()

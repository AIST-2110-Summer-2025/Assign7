from i_am_human import format_float

# Make this function work
def get_float(prompt):
    ...


# Make this function work
def get_operator(prompt):
    ...


# Make this function work
def get_result(num1, num2, operator):
    ...


# Look but don't touch...
# Isn't this so much simpler and cleaner?
def main():
    n1 = get_float("Enter number 1: ")
    if n1 is None:
        return          # early return strategy

    n2 = get_float("Enter number 2: ")
    if n2 is None:
        return

    op = get_operator("Enter an operator [ + - x / ^ ]: ")
    if op is None:
        return

    res = get_result(n1, n2, op)

    n1_str = format_float(n1)
    n2_str = format_float(n2)
    if not res:     # if res is None then the result should show ERROR
        res_str = "ERROR"
    else:           # otherwise round and format it to 4 decimal places
        res_str = format_float(res, 4)

    print(f"{n1_str} {op} {n2_str} = {res_str}")


if __name__ == "__main__":
    main()

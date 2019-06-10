import time
import sys
from knum import KNum

def test(file_path, mode = None):
    def mult(expected, xval, yval):
        return KNum(expected), KNum(xval) * KNum(yval)
    def div(expected, xval, yval):
        return KNum(expected), KNum(xval) / KNum(yval)
    def sum(expected, xval, yval):
        return KNum(expected), KNum(xval) + KNum(yval)
    def rest(expected, xval, yval):
        return KNum(expected), KNum(xval) - KNum(yval)

    print("*** Reading Test Cases ***")
    cases = None
    total = 0
    failed = 0
    passed = 0
    with open(file_path, "r") as file:
        lines = file.read()
        cases = lines.split("\n")
    total = len(cases)
    start = time.time()
    for case in cases:
        # Skips comments
        if case.startswith("#"): 
            continue
        (case_num, xval, yval, expected) = (int(n) for n in case.split(";"))
        print(f"\nProcessing case {case_num}: {xval} * {yval}")

        if not mode or mode == 'mult' or mode == '*':
            expected, given = mult(expected, xval, yval)
        elif mode == 'div' or mode == '/':
            expected, given = div(expected, xval, yval)
        elif mode == 'sum' or mode == '+':
            expected, given = sum(expected, xval, yval)
        elif mode == 'rest' or mode == '-':
            expected, given = rest(expected, xval, yval)

        if  given != expected:
            print(f" Result: {given} != Expected: {expected}")
            print(f'*** Case {case_num} failed! ***')
            failed += 1
        else:
            print(f" Result: {given} != Expected: {expected}")
            print(f'*** Case {case_num} passes! ***')
            passed += 1
            
    end = time.time()
    print("\n*** Test Case Result ***")
    print(f"Total cases={total}. Failed={failed} Passed={passed}")
    print(f"Duration:{(end -start):.4f}sec")
    return f"{(end -start):.4f}sec"

if __name__ == "__main__":
    argv = sys.argv
    mode = None
    if len(argv) == 1:
        file = "../test/test_01.csv"
    elif len(argv) == 2:
        file = argv[1]
    else:
        file = argv[1]
        mode = argv[2]

    test(file, mode)

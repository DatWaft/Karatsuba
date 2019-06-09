import time
if __name__ == "__main__":
    print("*** Reading Test Cases ***")
    cases = None
    total = 0
    failed = 0
    passed = 0
    with open("../test/test_01.csv", "r") as file:
        lines = file.read()
        cases = lines.split("\n")
    total = len(cases)
    start = time.time()
    for case in cases:
        # Skips comments
        if case.startswith("#"): 
            continue
        (case_num, xval, yval, expected) = (int(n) for n in case.split(";"))
        print(f"Processing case {case_num}")
        given = xval * yval
        if  given != expected:
            print(f"*** Case {case_num} failed! {given} != {expected} ***")
            failed += 1
        else:
            print(f"*** Case {case_num} passes! ***")
            passed += 1
            
    end = time.time()
    print("\n*** Test Case Result ***")
    print(f"Total cases={total}. Failed={failed} Passed={passed}")
    print(f"Duration:{(end -start):.4f}sec")
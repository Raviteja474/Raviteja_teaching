import time

def run_tests(obj):
    print(f"creatig object : {type(obj)}")
    print("precondition start")
    time.sleep(1)

    TEST_FAIL = False

    setup_result= obj.setUp()
    if not setup_result:
        TEST_FAIL = True
    time.sleep(1)

    obj.run()
    run_result = obj.run()
    if not run_result:
        TEST_FAIL = True
    time.sleep(1)

    tearDown_result =obj.tearDown()
    if not tearDown_result:
        TEST_FAIL = True
    time.sleep(1)

    if TEST_FAIL:
        print(".................Test failed................")
    else:
        print(".................Test passed................")

    print("postcondition start")
    time.sleep(1)


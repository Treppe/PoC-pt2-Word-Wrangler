"""
Lightweight testing class inspired by unittest from Pyunit
https://docs.python.org/2/library/unittest.html
Note that code is designed to be much simpler than unittest
and does NOT replicate unittest functionality
"""
import user47_qdKDMRsIRKKjadc_12 as ww

class TestSuite:
    """
    Create a suite of tests similar to unittest
    """
    def __init__(self):
        """
        Creates a test suite object
        """
        self.total_tests = 0
        self.failures = 0
    
    
    def run_test(self, computed, expected, message = ""):
        """
        Compare computed and expected
        If not equal, print message, computed, expected
        """
        self.total_tests += 1
        if computed != expected:
            msg = message + " Computed: " + str(computed)
            msg += " Expected: " + str(expected)
            print msg
            self.failures += 1
    
    def report_results(self):
        """
        Report back summary of successes and failures
        from run_test()
        """
        msg = "Ran " + str(self.total_tests) + " tests. "
        msg += str(self.failures) + " failures."
        print msg
               

suite = TestSuite()
# def remove_duplicates(list1) test:
test_list = [1, 1, 3, 4, 4, 4, 5]
suite.run_test(ww.remove_duplicates(test_list), [1, 3, 4, 5], 
               "Test 1a: remove_duplicates([1, 1, 3, 4, 4, 4, 5])")
test_list = [1, 2, 3]
suite.run_test(ww.remove_duplicates(test_list), [1, 2, 3], 
               "Test 1b: remove_duplicates([1, 2, 3])")
test_list = []
suite.run_test(ww.remove_duplicates(test_list), [], 
               "Test 1c: remove_duplicates([])")

# def intersect(list1, list2) test:
test_list1 = [1, 2, 3]
test_list2 = [2, 3, 4]
suite.run_test(ww.intersect(test_list1, test_list2),
               [2, 3], "Test 2a: intersect([1,2,3],[2,3,4])")
test_list1 = [1, 2, 2, 3]
test_list2 = [2, 3, 4]
suite.run_test(ww.intersect(test_list1, test_list2),
               [2, 2, 3], "Test 2b: intersect([1,2,2,3],[2,3,4])")
test_list1 = [1, 2]
test_list2 = [3, 4]
suite.run_test(ww.intersect(test_list1, test_list2),
               [], "Test 2c: intersect([1,2],[3,4])")

# def merge(list1, list2) test:
test_list1 = [1, 2, 3]
test_list2 = [2, 3, 4]
suite.run_test(ww.merge(test_list1, test_list2),
               [1, 2, 3, 4], "Test 3a: merge([1,2,3], [2,3,4])")
test_list1 = []
test_list2 = [1, 2]
suite.run_test(ww.merge(test_list1, test_list2),
               [1, 2], "Test 3b: merge([], [1, 2])")
test_list2 = [1, 2, 3]
test_list1 = [2, 3, 4]
suite.run_test(ww.merge(test_list1, test_list2),
               [1, 2, 3, 4], "Test 3a: merge([2,3,4], [1,2,3])")


suite.report_results()
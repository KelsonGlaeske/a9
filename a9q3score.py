# CMPT 145: Node-Based Data Structures
#   Linked List ADT test script
#   This version reports progress through the script!
#
#   The script runs two kinds of tests:
#      - unit tests: test one function at a time
#      - integration tests: test how functions work together

import a9q3 as a9q3


###############################################################################################
# A little tool to help with the reporting of errors and counting, etc.
# It's an ADT defined within this file, with the following operations:
#   - createCounter(reason, lim)
#     create a counter data structure labelled with a reason (string) and an error limit (lim)
#   - expecting(counter, flag, errstring)
#     counts and reports, based on the outcome of a test (flag)
#   - set_limit(counter, lim)
#     cause the counter to stop the script after a given number of errors (lim)
#   - final_report(counter)
#     displays the final results


class ErrorCounter(object):
    def __init__(self, reason, lim=0):
        """
        Create a counter to counter tests.  The counter will
        collect statistics based on calls to function expecting().
        :param reason: a string to describe what's being tested.
        :param lim: how many errors to detect before halting the tests
        :return: None
        """
        self.successes = 0
        self.tests = 0
        self.reason = reason
        self.limit = lim


    def expecting(self, flag, errstring='null'):
        """
        Do the work of counting and reporting.
        If flag is true, the condition being tested is true, meaning no error.
        Report the progress at all times, but give more detail when flag is False.
        The value of this for debugging depends on useful errstring!

        :param counter: the counter to use
        :param flag: A Boolean, the result of a test for an expected correct result
        :param errstring: a string that describes what should have happened
        :return: None
        """
        self.tests += 1
        if flag:
            self.successes += 1
        print("***", self.successes, 'of', self.tests, 'tests passed', end=' ')
        if not flag:
            print('**FAILURE**', self.reason + errstring)
        else:
            print()
        if self.limit > 0 and self.tests - self.successes >= self.limit:
            print("Halting because of too many errors")
            exit(1)


    def set_limit(self, errors):
        """
        Set the counter to terminate testing after a number of errors.
        If errors is 0, there is no limit.
        :param counter: a counter
        :param errors: an integer
        :return: None
        """
        self.limit = errors


    def final_report(self):
        """
        Display the final count for the number of successful tests.
        :param counter: a counter.
        :return: None
        """
        print('Final Count for', self.reason, self.successes, 'of', self.tests, 'tests passed')

###############################################################################################


test_counter = ErrorCounter('Table operations: ')

###############################################################################################

def gen_val(key):
    """Given a key, return a string that can’t be mistaken as the key itself"""
    return 'value_for_'+str(key)


###############################################################################################
reason = 'Table unit test'
print('---Test phase:', reason, '---')
atable = a9q3.Table()

test_counter.expecting(atable.is_empty(), reason + ': brand new Table not empty!')
test_counter.expecting(atable.size() == 0, reason + ': brand new Table non zero size!')


###############################################################################################
reason = 'Table insertion test'
print('---Test phase:', reason, '---')
atable = a9q3.Table()


keys = [5, 3, 7]
for vvv in keys:
    flag = atable.insert(vvv, gen_val(vvv))
    test_counter.expecting( flag, reason + ': insertion of key '+str(vvv)+' failed')

test_counter.expecting(not atable.is_empty(), reason + ': Table with successful insertions is empty!')
test_counter.expecting(atable.size() == 3, reason + ': Table has wrong size!')

###############################################################################################
reason = 'Table membership test'
print('---Test phase:', reason, '---')
atable = a9q3.Table()


keys = [5, 3, 7]
for vvv in keys:
    flag = atable.insert(vvv, gen_val(vvv))

for vv in keys:
    flag, newvalue = atable.retrieve(vv)
    test_counter.expecting( flag, reason + ': member could not find key in non-trivial tree after deletion')
    test_counter.expecting( newvalue == gen_val(vv), reason + ': member could not find value in non-trivial tree after deletion')


###############################################################################################
reason = 'Table update test'
print('---Test phase:', reason, '---')
atable = a9q3.Table()

keys = [5, 3, 7]
for vvv in keys:
    flag = atable.insert(vvv, gen_val(vvv))

for vvv in keys:
    flag = atable.insert(vvv, gen_val(vvv)+'_updated!')
    test_counter.expecting( not flag, reason + ': insertion of key '+str(vvv)+' failed')

test_counter.expecting(not atable.is_empty(), reason + ': Table with successful updates is empty!')
test_counter.expecting(atable.size() == len(keys), reason + ': Table has wrong size!')

for vvv in keys:
    flag, newvalue = atable.retrieve(vvv)
    test_counter.expecting(flag, reason + ': key '+str(vvv)+' not found after update')
    test_counter.expecting(newvalue == gen_val(vvv)+'_updated!', reason + ': value for '+str(vvv)+' not properly update')


###############################################################################################
reason = 'Table deletion test'
print('---Test phase:', reason, '---')
atable = a9q3.Table()

keys = [5, 3, 10]
for v in keys:
    atable = a9q3.Table()
    for vvv in keys:
        flag = atable.insert(vvv, gen_val(vvv))

    flag = atable.delete(v)
    test_counter.expecting( flag, reason + ': deletion of data failed in non-trivial tree')
    flag, newvalue = atable.retrieve(v)
    test_counter.expecting( not flag, reason + ': member found deleted key in non-trivial tree')
    test_counter.expecting( newvalue is None, reason + ': member returned some value in non-trivial tree')
    test_counter.expecting(not atable.is_empty(), reason + ': Table with successful insertions is empty!')
    test_counter.expecting(atable.size() == len(keys)-1, reason + ': Table has wrong size!')
    for vv in keys:
        if v != vv:
            flag, newvalue = atable.retrieve(vv)
            test_counter.expecting( flag, reason + ': member could not find key in non-trivial tree after deletion')
            test_counter.expecting( newvalue == gen_val(vv), reason + ': member could not find value in non-trivial tree after deletion')


###############################################################################################
reason = 'Table total annihilation test'
print('---Test phase:', reason, '---')
atable = a9q3.Table()

keys = [5, 3, 8, 6, 10, 1, 15, 11, 24, -1]
for v in keys:
    flag = atable.insert(v, gen_val(v))

test_counter.expecting(not atable.is_empty(), reason + ': Table with successful insertions is empty!')
test_counter.expecting(atable.size() == len(keys), reason + ': Table has wrong size!')

for v in keys:
    flag = atable.delete(v)
    test_counter.expecting( flag, reason + ': deletion of data failed in non-trivial tree')

test_counter.expecting(atable.is_empty(), reason + ': Table with all keys deleted is not empty')
test_counter.expecting(atable.size() == 0, reason + ': Table has non-zero size!')

test_counter.final_report()

# CMPT 145: Node-Based Data Structures
#   Linked List ADT test script
#   This version reports progress through the script!
#
#   The script runs two kinds of tests:
#      - unit tests: test one function at a time
#      - integration tests: test how functions work together

import a9q2 as a9q2


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
        self.limit = 200


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


test_counter = ErrorCounter('BST primitive operations: ')

###############################################################################################

def gen_val(key):
    """Given a key, return a string that can’t be mistaken as the key itself"""
    return 'value_for_'+str(key)
    
###############################################################################################
reason = 'insert_prim() singleton test'
print('---Test phase:', reason, '---')
atnode = None

key = 'one'
value = gen_val(key)
flag, newtree = a9q2.insert_prim(atnode, key, value)

test_counter.expecting( flag, reason + ': insertion into empty tree failed')
test_counter.expecting( newtree is not None, reason + ': insertion did not create a new tree')
test_counter.expecting( newtree.key == key, reason + ': insertion into empty tree lost key')
test_counter.expecting( newtree.value == value, reason + ': insertion into empty tree lost value')


###############################################################################################
reason = 'member_prim() singleton test'
print('---Test phase:', reason, '---')
atnode = None

key = 'one'
value = gen_val(key)
flag, atnode = a9q2.insert_prim(atnode, key, value)

flag, retvalue = a9q2.member_prim(atnode, key)
test_counter.expecting( flag, reason + ': member failed to find key at root of singleton tree')
test_counter.expecting( retvalue == value, reason + ': member failed to return value at root of singleton tree')

flag, retvalue = a9q2.member_prim(atnode, 'ksjdkdjs')
test_counter.expecting( not flag, reason + ': member found unknown key at root')
test_counter.expecting( retvalue is None, reason + ': member found unknown value at root')


###############################################################################################
reason = 'delete_prim() singleton test'
print('---Test phase:', reason, '---')
atnode = None

key = 'one'
value = gen_val(key)
_, atnode = a9q2.insert_prim(atnode, key, value)

flag, newtree = a9q2.delete_prim(atnode, key)

test_counter.expecting( flag, reason + ': could not delete root of singleton tree ')
test_counter.expecting( newtree is None, reason + ': result of deletion of root of singleton tree is not empty')

###############################################################################################
reason = 'delete_prim() left leaf test'
print('---Test phase:', reason, '---')
atnode = None

key = [5, 3, 7]
for k in key:
    flag, atnode = a9q2.insert_prim(atnode, k, gen_val(k))

flag, newtree = a9q2.delete_prim(atnode, 3)

test_counter.expecting( flag, reason + ': delete left leaf of 2-level tree failed')
test_counter.expecting( newtree.left is None, reason + ': could not delete left leaf of 2-level tree ')
test_counter.expecting( newtree.key == 5, reason + ': delete left leaf modified root of 2-level tree: key ')
test_counter.expecting( newtree.value == gen_val(5), reason + ': delete left leaf modified root of 2-level tree: value ')
test_counter.expecting( newtree.right.key == 7, reason + ': delete left leaf modified right leaf of 2-level tree: key ')
test_counter.expecting( newtree.right.value == gen_val(7), reason + ': delete left leaf modified right leaf of 2-level tree: value ')

###############################################################################################
reason = 'delete_prim() right leaf test'
print('---Test phase:', reason, '---')
atnode = None

keys = [5, 3, 7]
for v in keys:
    flag, atnode = a9q2.insert_prim(atnode, v, gen_val(v))

flag, newtree = a9q2.delete_prim(atnode, 7)

test_counter.expecting( flag, reason + ': delete right leaf of 2-level tree failed')
test_counter.expecting( newtree.right is None, reason + ': could not delete right leaf of 2-level tree ')
test_counter.expecting( newtree.key == 5, reason + ': delete right leaf modified root of 2-level tree: key')
test_counter.expecting( newtree.value == gen_val(5), reason + ': delete right leaf modified root of 2-level tree: value')
test_counter.expecting( newtree.left.key == 3, reason + ': delete right leaf modified left leaf of 2-level tree: key')
test_counter.expecting( newtree.left.value == gen_val(3), reason + ': delete right leaf modified left leaf of 2-level tree: value')

###############################################################################################
reason = 'delete_prim() root test'
print('---Test phase:', reason, '---')
atnode = None

keys = [5, 3, 7]
for v in keys:
    flag, atnode = a9q2.insert_prim(atnode, v, gen_val(v))

flag, newtree = a9q2.delete_prim(atnode, 5)

test_counter.expecting( flag, reason + ': delete root of 2-level tree failed')
test_counter.expecting( newtree.key == 3, reason + ': delete root failed to set root of 2-level tree: key ')
test_counter.expecting( newtree.value == gen_val(3), reason + ': delete root failed to set root of 2-level tree: value ')
test_counter.expecting( newtree.right.key == 7, reason + ': delete root failed to set right leaf of 2-level tree: key ')
test_counter.expecting( newtree.right.value == gen_val(7), reason + ': delete root failed to set right leaf of 2-level tree: value ')
test_counter.expecting( newtree.left is None, reason + ': root failed to set left subtree of 2-level tree ')


###############################################################################################
reason = 'insert_prim() integration test'
print('---Test phase:', reason, '---')
atnode = None

keys = ['one', 'two', 'three', 'four', 'five']
for v in keys:
    flag, atnode = a9q2.insert_prim(atnode, v, gen_val(v))
    test_counter.expecting( flag, reason + ': sequential insertion into tree failed')

test_counter.expecting( atnode.key == 'one', reason + ': insertion into empty tree lost data value at root')
test_counter.expecting( atnode.left.key == 'four', reason + ': insertion into empty tree lost data at left subtree: key')
test_counter.expecting( atnode.left.value == gen_val('four'), reason + ': insertion into empty tree lost data at left subtree: value')
test_counter.expecting( atnode.right.key == 'two', reason + ': insertion into empty tree lost data at right subtree: key')
test_counter.expecting( atnode.right.value == gen_val('two'), reason + ': insertion into empty tree lost data at right subtree: value')
test_counter.expecting( atnode.left.left.key == 'five', reason + ': insertion into empty tree lost data at left subtree: key')
test_counter.expecting( atnode.right.left.value == gen_val('three'), reason + ': insertion into empty tree lost data at right subtree: value')
test_counter.expecting( atnode.left.left.key == 'five', reason + ': insertion into empty tree lost data at left subtree: key')
test_counter.expecting( atnode.right.left.value == gen_val('three'), reason + ': insertion into empty tree lost data at right subtree: value')
test_counter.expecting( atnode.left.right is None, reason + ': insertion into empty tree added data at left subtree')
test_counter.expecting( atnode.right.right is None, reason + ': insertion into empty tree added data at right subtree')


###############################################################################################
reason = 'member_prim() positives test'
print('---Test phase:', reason, '---')
atnode = None

keys = ['one', 'two', 'three', 'four', 'five']
for v in keys:
    flag, atnode = a9q2.insert_prim(atnode, v, gen_val(v))

for v in keys:
    flag, newvalue = a9q2.member_prim(atnode, v)
    test_counter.expecting( flag, reason + ': member failed to find key in non-trivial tree')
    test_counter.expecting( newvalue == gen_val(v), reason + ': member failed to find value in non-trivial tree')

###############################################################################################
reason = 'member_prim() negatives test'
print('---Test phase:', reason, '---')
atnode = None

keys = ['one', 'two', 'three', 'four', 'five']
for v in keys:
    flag, atnode = a9q2.insert_prim(atnode, v, gen_val(v))

for v in ['seven', 'eleven']:
    flag, newvalue = a9q2.member_prim(atnode, v)
    test_counter.expecting( not flag, reason + ': member foudn nonsense in non-trivial tree')
    test_counter.expecting( newvalue is None, reason + ': member found value in non-trivial tree')


###############################################################################################
reason = 'delete_prim() negatives test'
print('---Test phase:', reason, '---')
atnode = None

keys = [5, 3, 1, 8, 10, 7, 2]
for v in keys:
    flag, atnode = a9q2.insert_prim(atnode, v, gen_val(v))

flag, atnode = a9q2.delete_prim(atnode, 99)
test_counter.expecting( not flag, reason + ': deletion of non-data failed in non-trivial tree')

###############################################################################################
reason = 'delete_prim() positives test'
print('---Test phase:', reason, '---')
atnode = None

keys = [5, 3, 1, 8, 10, 7, 2]
for v in keys:
    for vvv in keys:
        flag, atnode = a9q2.insert_prim(atnode, vvv, gen_val(vvv))
    flag, newtree = a9q2.delete_prim(atnode, v)
    test_counter.expecting( flag, reason + ': deletion of data failed in non-trivial tree')
    flag, newvalue = a9q2.member_prim(newtree, v)
    test_counter.expecting( not flag, reason + ': member found deleted key in non-trivial tree')
    test_counter.expecting( newvalue is None, reason + ': member returned value in non-trivial tree')
    for vv in keys:
        if v != vv:
            flag, newvalue = a9q2.member_prim(newtree, vv)
            test_counter.expecting( flag, reason + ': member could not find key in non-trivial tree after deletion')
            test_counter.expecting( newvalue == gen_val(vv), reason + ': member could not find value in non-trivial tree after deletion')

test_counter.final_report()

'''
https://stackoverflow.com/questions/18296755/python-max-function-using-key-and-lambda-expression
s :- covered takes every element of s that isn't in covered and makes a new set out of that
len(s - covered) :- is the number of elements in s that aren't in covered (the number of elements in s - covered)
lambda s: len(s - covered) :- is a function that takes a set and returns the number of elements in that set that
                            aren't in covered
key=lambda s: len(s - covered) :- uses that function as a "key" which is applied to all of the elements of subsets
                                  before comparing them
'''
# set covering problem

def set_cover(universe, subsets):
    """Find a family of subsets that covers the universal set"""
    elements = set(e for s in subsets for e in s)
    # Check the subsets cover the universe
    if elements != universe:
        return None

    covered = set()
    answer = []

    # Greedily add the subsets with the most uncovered points
    while covered != elements:
        subset = max(subsets, key=lambda s: len(s - covered))
        answer.append(subset)
        covered = covered | subset

    return answer


cities = int(input("Enter no of cities : "))
town_pairs = int(input("Enter town pairs: "))
print(cities, '\t', town_pairs)

#for i in range(town_pairs):
 #   user_inpt = input('enter num seperated by , : ')

universe = set(range(1, cities + 1))
# subsets = [set([1, 2, 6, 8]),
#            set([2, 1, 3, 6]),
#            set([3, 2, 4, 5]),
#            set([3, 5, 4, 7]),
#            set([5, 3, 4, 6]),
#            set([6, 1, 2, 5, 7, 8]),
#            set([7, 4, 6]),
#            set([8, 1, 6])]
subsets = [{8, 1, 2, 6},
            {1, 2, 3, 6},
            {2, 3, 4, 5},
            {3, 4, 5, 7},
            {3, 4, 5, 6},
            {1, 2, 5, 6, 7, 8},
            {4, 6, 7},
            {8, 1, 6}]
cover = set_cover(universe, subsets)
print(cover)
print('The minimum no of stations the company has to build are:', len(cover))




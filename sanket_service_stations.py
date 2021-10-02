common = [1, 2, 3, 4, 5, 6, 7, 8]
user_input = {}
common_pair = {}
no_town = int(input("ENTER NUMBER OF TOWNS : "))
no_town_pairs = int(input("ENTER NUMBER OF TOWN PAIRS : "))

i = 0
while i < no_town_pairs:
    n1, n2 = input().split()
    a = int(n1)
    b = int(n2)
    user_input.setdefault(i, [a]).append(b)
    i = i + 1

conv_input = list(user_input.values())
pair = 1
i = 0
while i < no_town_pairs:
    if conv_input[i][0] == pair:
        common_pair.setdefault(pair, [pair]).append(conv_input[i][1])
    elif conv_input[i][1] == pair:
        common_pair.setdefault(pair, [pair]).append(conv_input[i][0])
    if i >= conv_input.__len__() - 1:
        pair = pair + 1
        i = 0
        if pair > no_town:
            break
        continue
    i = i + 1

conv_common_pair = list(common_pair.values())

# new logic starts here


def set_cover(universe, subsets):
    elements = set(e for s in subsets for e in s)
    if elements != universe:
        return None

    covered = set()
    answer = []
    while covered != elements:
        subset = max(subsets, key=lambda s: len(s - covered))
        answer.append(subset)
        covered = covered | subset
    return answer


# main area
list_of_sets = []
for i in conv_common_pair:
    list_of_sets.append(set(i))

print("list of sets", list_of_sets)
universe = set(range(1, no_town + 1))
subsets = list_of_sets

cover = set_cover(universe, subsets)
print('=' * 40)
print(cover)
print('The minimum no of stations the company has to build are:', len(cover))





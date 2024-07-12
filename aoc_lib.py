from math import ceil, floor, gcd, lcm, factorial, log, exp, pi, sin, cos, tan

vowels, VOWELS = 'aeiou', 'AEIOU'
conson, CONSON = 'bcdfghjklmnpqrstvwxyz', 'BCDFGHJKLMNPQRSTVWXYZ'
alphab, ALPHAB = 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits, digits_as_words = '0123456789', ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
remap_cards = {'2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', 'T':'B', 'J':'C', 'Q':'D', 'K':'E', 'A':'F', 'X':'0'}

def rotate_grid(grid, direction="right"):
    if direction == "right":
        return [list(row)[::-1] for row in zip(*grid)]
    elif direction == "left":
        return [row for row in list(zip(*grid))][::-1]
    elif direction == "180":
        return [row[::-1] for row in grid[::-1]]

def flatten(matrix): return [item for row in matrix for item in row]
def flip(matrix, sideways=True): return [row[::-1] for row in matrix] if sideways else [row for row in reversed(matrix)]
def diagonal(matrix, left=True): return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))] if left else [[matrix[len(matrix) - 1 - j][len(matrix) - 1 - i] for j in range(len(matrix))] for i in range(len(matrix))]

def combinations(array, n=2):
    def helper(start, combo):
        if len(combo) == n: return [combo]
        return sum([helper(i + 1, combo + [array[i]]) for i in range(start, len(array) - n + len(combo) + 1)], [])
    return helper(0, [])

def matches(array1, array2): return list(set(array1) & set(array2))
def count_items(array): return {item: array.count(item) for item in array}
def count_and_sort_items(array): return sorted(sorted(list({item: array.count(item) for item in array}.items()), key=lambda x: x[0]), key=lambda x: x[1], reverse=True)
def gcd_list(array): return array[0] if len(array) == 1 else gcd_list([gcd(array[0], array[1])] + array[2:])
def lcm_list(array): return array[0] if len(array) == 1 else lcm_list([lcm(array[0], array[1])] + array[2:])
def average(array, include_zeros=True): return sum([num for num in array if num != 0 or include_zeros]) / max(len([num for num in array if num != 0 or include_zeros]), 1)
def distance(a, b, direct=False): return sum([abs(a[i] - b[i]) ** (1 + direct) for i in range(len(a))]) ** (1 / (1 + direct))
def none(array): return not any(array)
def cardinal(array, num): return [items for items in zip(*[list(array[i:len(array)-num+i+1]) for i in range(num)])]

def product(array, include_zeros=False):
    if 0 in array and include_zeros: return 0
    result, a = 1, [n for n in array if n != 1]
    for n in array: result *= n
    return result

def extremes(array, mode='max'):
    mode = max if mode == 'max' else min
    return {key: mode(item[key] for item in array if key in item) for key in list(set.union(*[set(item.keys()) for item in array]))}

def items_meet_constraints(items, rules): return all(rule not in items or items[rule] <= rules[rule] for rule in rules)
def items_in_matrix(items, matrix, find=True): return [(i, j) for i, row in enumerate(matrix) for j, item in enumerate(row) if (item in items) == find]
def items_in_rows(items, matrix, find=True): return [i for i, row in enumerate(matrix) if (any(item in row for item in items) ^ (not find))]
def items_in_cols(items, matrix, find=True): return [i for i, col in enumerate(rotate(matrix)) if (any(item in col for item in items) ^ (not find))]
def items_in_row(items, row, find=True): return [(i, item) for i, item in enumerate(row) if (item in items) ^ (not find)]

def count_chars(string): return {char: string.count(char) for char in string}
def count_and_sort_chars(string): return sorted(sorted(list({char: string.count(char) for char in string}.items()), key=lambda x: x[0]), key=lambda x: x[1], reverse=True)
def reverse(string): return string[::-1]
def is_palindrome(string): return string == reverse(string)
def list_chars(string): return [list(line) for line in data.split('\n')]

def replace_all_items_in_string(items, string):
    for item1, item2 in items: string = string.replace(item1, item2)
    return string

def char_to_num(char): return ord(char.upper())-64

def n_combinations(n, x): return factorial(n) / (factorial(x) * factorial(n - x))
def num_to_char(num, upper=False): return chr(num + 96 - upper * 32)
def pascal(num): return num * (num + 1) / 2
def is_triangle_num(num): return (num * 8 + 1) ** .5 % 1 == 0
def fibonacci(num): return 0 if num == 0 else 1 if num < 3 else fibonacci(num - 1) + fibonacci(num - 2)
def signum(num): return (num > 0) - (num < 0)

def quadratic(a, b, c): return (- b + (b ** 2 - 4 * a * c) ** .5) / (2 * a), (- b - (b ** 2 - 4 * a * c) ** .5) / (2 * a)

def num_in_range(num, pair): return min(pair) <= num < max(pair)
def natural_power(num): return 0 if num < 1 else 1 << (num - 1)

def range_intersection(range1, range2): # uses 2 pairs of coordinates (even pair not inclusive)
    (x1, x2), (x3, x4) = range1, range2 # get x's
    if x1 == x2 or x3 == x4: return [[], [range1] * (x1 < x2), [range2] * (x3 < x4)] # check for zero-length
    if range1 == range2: return [[range1], [], []] # check for same range
    left_pair, intersection, right_pair = cardinal((min(x1, x3), max(x1, x3), min(x2, x4), max(x2, x4)), 2) # get pairs
    if intersection[0] >= intersection[1]: return [[], [range1], [range2]] # check for no intersection
    ranges = [[intersection], [], []] # get intersecting range
    if x1 < intersection[0]: ranges[1] += [left_pair] # get remainder ranges
    if x2 > intersection[1]: ranges[1] += [right_pair]
    if x3 < intersection[0]: ranges[2] += [left_pair]
    if x4 > intersection[1]: ranges[2] += [right_pair]
    return ranges

def box_intersection(box1, box2): # uses 4 pairs of coordinates (even pairs not inclusive)
    ((x1, y1), (x2, y2)), ((x3, y3), (x4, y4)) = box1, box2 # get x's and y's
    if x1 == x2 or y1 == y2 or x3 == x4 or y3 == y4: return [[], [box1] * (x1 < x2 and y1 < y2), [box2] * (x3 < x4 and y3 < y4)] # check for zero-area
    if box1 == box2: return [[box1], [], []] # check for same box
    ([x_intersection], *x_pairs), ([y_intersection], *y_pairs) = range_intersection((x1, x2), (x3, x4)), range_intersection((y1, y2), (y3, y4)) # get pairs
    if 0 in (len(x_intersection), len(y_intersection)): return [[], [box1], [box2]] # check for no intersection
    boxes = [[((x_intersection[0], y_intersection[0]), (x_intersection[1], y_intersection[1]))], [], []] # get intersecting box
    for i in (0, 1): # get remainder boxes
        x_pair = flatten([x_intersection] + x_pairs[i])
        for y in y_pairs[i]: boxes[i+1] += [((min(x_pair), y[0]), (max(x_pair), y[1]))]
        for x in x_pairs[i]: boxes[i+1] += [((x[0], y_intersection[0]), (x[1], y_intersection[1]))]
    return boxes

def cycle_bits(a, b, c, d, e):
    f = b - c
    g = f - d
    h = a >> g & (1 << d) - 1
    return a >> f << f | (((1 << (e % d)) - 1 & h) << d - (e % d) | h >> (e % d)) << g | (1 << g) - 1 & a

def cycle_items(array, padding, cycle_start, cycle_length, num_right_shifts):
    array = [None for _ in range(padding - len(array))] + array
    num_right_shifts %= cycle_length
    if num_right_shifts > 0:
        array_slice = array[cycle_start:cycle_start + cycle_length][-num_right_shifts:] + array[cycle_start:cycle_start + cycle_length][:-num_right_shifts]
    else:
        num_left_shifts = -num_right_shifts
        array_slice = array[cycle_start:cycle_start + cycle_length][num_left_shifts:] + array[cycle_start:cycle_start + cycle_length][:num_left_shifts]
    return array[:cycle_start] + array_slice + array[cycle_start + cycle_length:]

def walk(steps, origin=(0, 0), stop=False):
    current = origin
    locations = {current: 1}
    while len(steps) > 0:
        step = steps.pop(0)
        current = tuple(a + b for a, b in zip(current, step))
        locations[current] = locations.get(current, 0) + 1
        if current == stop: break
    return locations

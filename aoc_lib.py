from math import ceil, floor, gcd, lcm, factorial, log, exp, pi, sin, cos, tan

vowels, VOWELS = 'aeiou', 'AEIOU'
conson, CONSON = 'bcdfghjklmnpqrstvwxyz', 'BCDFGHJKLMNPQRSTVWXYZ'
alphab, ALPHAB = 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits, digits_as_words = '0123456789', ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
remap_cards = {'2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', 'T':'B', 'J':'C', 'Q':'D', 'K':'E', 'A':'F', 'X':'0'}

def int1(x): return int(x) + 1

def rotate_grid(grid, direction="right"):
    if direction == "right":
        return [list(row)[::-1] for row in zip(*grid)]
    elif direction == "left":
        return [row for row in list(zip(*grid))][::-1]
    elif direction == "180":
        return [row[::-1] for row in grid[::-1]]

def grid_diagonal(grid):
    A = {}
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            A.setdefault(i + j, []).append(value)
    return list(A.values())

def flatten(matrix): return [item for row in matrix for item in row]
def flip(matrix, sideways=True): return [row[::-1] for row in matrix] if sideways else [row for row in reversed(matrix)]
def diagonal(matrix, left=True): return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))] if left else [[matrix[len(matrix) - 1 - j][len(matrix) - 1 - i] for j in range(len(matrix))] for i in range(len(matrix))]

def directions(keys): return dict(zip(keys, [(0, -1), (0, 1), (-1, 0), (1, 0)])) # left, right, up, down

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
def cardinal(x, n): return [x[i:i+n] for i in range(len(x)-n+1)]

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
def items_in_cols(items, matrix, find=True): return [i for i, col in enumerate(rotate_grid(matrix)) if (any(item in col for item in items) ^ (not find))]
def items_in_row(items, row, find=True): return [(i, item) for i, item in enumerate(row) if (item in items) ^ (not find)]

def count_chars(string): return {char: string.count(char) for char in string}
def count_and_sort_chars(string): return sorted(sorted(list({char: string.count(char) for char in string}.items()), key=lambda x: x[0]), key=lambda x: x[1], reverse=True)
def reverse(string): return string[::-1]
def is_palindrome(string): return string == reverse(string)
def list_chars(string): return [list(line) for line in string.split('\n')]

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

def is_subrange_in_range(subrange, in_range):
    (a, b), (c, d) = subrange, in_range
    return c <= a <= b <= d

def range_intersection(range1, range2):
    (a, b), (c, d) = range1, range2
    range_intersections = [[], [], None]
    for subrange in cardinal(sorted({a, b, c, d}), 2):
        A, B = is_subrange_in_range(subrange, range1), is_subrange_in_range(subrange, range2)
        if A and B: range_intersections[2] = subrange
        elif A or B: range_intersections[A+B*2-1].append(subrange)
    return range_intersections

def join_ranges(ranges):
    if ranges:
        flattened = flatten(ranges)
        return min(flattened), max(flattened)

def box_intersection(box1, box2):
    ((x1, y1), (x2, y2)), ((x3, y3), (x4, y4)) = box1, box2
    x_intersections, y_intersections = range_intersection((x1, x2), (x3, x4)), range_intersection((y1, y2), (y3, y4))
    x_intersection, y_intersection = x_intersections[2], y_intersections[2]
    box_intersections = [[], [], None]
    if x_intersection and y_intersection:
        for box in (0, 1):
            if x_range := join_ranges(x_intersections[box] + [x_intersection] * bool(x_intersection)):
                x1, x2 = x_range
                for y1, y2 in y_intersections[box]:
                    box_intersections[box].append(((x1, y1), (x2, y2)))
            if y_intersection:
                y1, y2 = y_intersection
                for x1, x2 in x_intersections[box]:
                    box_intersections[box].append(((x1, y1), (x2, y2)))
        (x1, x2), (y1, y2) = x_intersection, y_intersection
        box_intersections[2] = ((x1, y1), (x2, y2))
    else:
        box_intersections = [[box1], [box2], None]
    return box_intersections

def box_size(box):
    (x1, y1), (x2, y2) = box
    return (x2 - x1) * (y2 - y1)

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

def find_all_indexes(substr, bigstr):
    I, start = [], 0
    while (start := bigstr.find(substr, start + 1)) != -1: I.append(start)
    return I

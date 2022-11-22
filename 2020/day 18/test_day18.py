from day18 import solve, solve_left_right, solve_ordered

def test_part1_1():
    assert solve('1 + (2 * 3) + (4 * (5 + 6))', solve_left_right) == 51

def test_part2_1():
    assert solve('1 + (2 * 3) + (4 * (5 + 6))', solve_ordered) == 51

def test_part2_2():
    assert solve('2 * 3 + (4 * 5)', solve_ordered) == 46

def test_part2_3():
    assert solve('5 + (8 * 3 + 9 + 3 * 4 * 3)', solve_ordered) == 1445

def test_part2_4():
    assert solve('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', solve_ordered) == 669060

def test_part2_5():
    assert solve('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', solve_ordered) == 23340

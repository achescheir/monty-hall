from unittest import mock
from monty_hall import get_prizes, get_opened_doors, swap, play_round
# create mock random.choice, always picks first element
# mock_random = mock.Mock(random.choice, returnvalue=0)
# patch over with mocked choice()  'random.choice', lambda seq:seq[0]
# with(mock.patch('random.choice', mock_choice)) as mock_random:


def mock_choice(a):
    return a[0]


def side_effect_1(arg):
    assert arg == [0, 1, 2]
    return arg[0]

mock_choice_1 = mock.Mock('mock_choice', side_effect=side_effect_1)


@mock.patch('random.choice', mock_choice_1)
def test_get_prizes_1():
    assert get_prizes(1, list(range(3))) == [0]
    assert len(mock_choice_1.mock_calls) == 1


def side_effect_2(arg, default=[[0, 1, 2, 3], [1, 2, 3]]):
    assert arg == default[0]
    default.remove(default[0])
    return arg[0]

mock_choice_2 = mock.Mock('mock_choice', side_effect=side_effect_2)


@mock.patch('random.choice', mock_choice_2)
def test_get_prizes_2():
    assert get_prizes(2, list(range(4))) == [0, 1]
    assert len(mock_choice_2.mock_calls) == 2


def side_effect_3(arg, default=[[2]]):
    assert arg == default[0]
    default.remove(default[0])
    return arg[0]

mock_choice_3 = mock.Mock('mock_choice', side_effect=side_effect_3)


@mock.patch('random.choice', mock_choice_3)
def test_get_opened_doors_3():
    assert get_opened_doors(list(range(3)), 1, [0], 1) == [2]
    assert len(mock_choice_3.mock_calls) == 1


def side_effect_4(arg, default=[[0, 2]]):
    assert arg == default[0]
    default.remove(default[0])
    return arg[0]

mock_choice_4 = mock.Mock('mock_choice', side_effect=side_effect_4)


@mock.patch('random.choice', mock_choice_4)
def test_get_opened_doors_4():
    assert get_opened_doors(list(range(3)), 1, [1], 1) == [0]
    assert len(mock_choice_4.mock_calls) == 1


def side_effect_5(arg, default=[[1]]):
    assert arg == default[0]
    default.remove(default[0])
    return arg[0]

mock_choice_5 = mock.Mock('mock_choice', side_effect=side_effect_5)


@mock.patch('random.choice', mock_choice_5)
def test_get_opened_doors_5():
    assert get_opened_doors(list(range(3)), 2, [0], 1) == [1]
    assert len(mock_choice_5.mock_calls) == 1


def side_effect_6(arg, default=[[2, 3]]):
    assert arg == default[0]
    default.remove(default[0])
    return arg[0]

mock_choice_6 = mock.Mock('mock_choice', side_effect=side_effect_6)


@mock.patch('random.choice', mock_choice_6)
def test_get_opened_doors_6():
    assert get_opened_doors(list(range(4)), 1, [0], 1) == [2]
    assert len(mock_choice_6.mock_calls) == 1


def side_effect_7(arg, default=[[2, 3], [3]]):
    assert arg == default[0]
    default.remove(default[0])
    return arg[0]

mock_choice_7 = mock.Mock('mock_choice', side_effect=side_effect_7)


@mock.patch('random.choice', mock_choice_7)
def test_get_opened_doors_7():
    assert get_opened_doors(list(range(4)), 1, [0], 2) == [2, 3]
    assert len(mock_choice_7.mock_calls) == 2


def side_effect_8(arg, default=[[2, 3]]):
    assert arg == default[0]
    default.remove(default[0])
    return arg[0]

mock_choice_8 = mock.Mock('mock_choice', side_effect=side_effect_8)


@mock.patch('random.choice', mock_choice_8)
def test_get_opened_doors_8():
    assert get_opened_doors(list(range(4)), 1, [0, 1], 1) == [2]
    assert len(mock_choice_8.mock_calls) == 1


def side_effect_9(arg, default=[[3]]):
    assert arg == default[0]
    default.remove(default[0])
    return arg[0]

mock_choice_9 = mock.Mock('mock_choice', side_effect=side_effect_9)


@mock.patch('random.choice', mock_choice_9)
def test_get_opened_doors_9():
    assert get_opened_doors(list(range(4)), 2, [0, 1], 1) == [3]
    assert len(mock_choice_9.mock_calls) == 1


def side_effect_10(arg, default=[[2]]):
    assert arg == default[0]
    default.remove(default[0])
    return arg[0]

mock_choice_10 = mock.Mock('mock_choice', side_effect=side_effect_10)


@mock.patch('random.choice', mock_choice_10)
def test_swap_10():
    assert swap(list(range(3)), 1, [0]) == 2
    assert len(mock_choice_10.mock_calls) == 1


def side_effect_11(arg, default=[[0]]):
    assert arg == default[0]
    default.remove(default[0])
    return arg[0]

mock_choice_11 = mock.Mock('mock_choice', side_effect=side_effect_11)


@mock.patch('random.choice', mock_choice_11)
def test_swap_11():
    assert swap(list(range(3)), 1, [2]) == 0
    assert len(mock_choice_11.mock_calls) == 1


def side_effect_12(arg, default=[[3]]):
    assert arg == default[0]
    default.remove(default[0])
    return arg[0]

mock_choice_12 = mock.Mock('mock_choice', side_effect=side_effect_12)


@mock.patch('random.choice', mock_choice_12)
def test_swap_12():
    assert swap(list(range(4)), 1, [0, 2]) == 3
    assert len(mock_choice_12.mock_calls) == 1


def side_effect_13(arg, default=[[0, 1, 2], [0, 1, 2], [1, 2], [2]]):
    assert arg == default[0]
    default.remove(default[0])
    return arg[0]

mock_choice_13 = mock.Mock('mock_choice', side_effect=side_effect_13)


@mock.patch('random.choice', mock_choice_13)
def test_play_round_13():
    assert not play_round()
    assert len(mock_choice_13.mock_calls) == 4

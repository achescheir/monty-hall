from  unittest import mock
from monty_hall import *

def mock_choice(a):
    return a[0]
#create mock random.choice, always picks first element
# mock_random = mock.Mock(random.choice, returnvalue=0)
#patch over with mocked choice()  'random.choice',lambda seq:seq[0]
@mock.patch('random.choice',mock_choice)
# with(mock.patch('random.choice', mock_choice)) as mock_random:
    def test_get_prizes():
        print(type(mock_random))
        assert get_prizes(1,list(range(3))) == [0]
        assert mock_random.called == True#assert_called_with([0,1,2])
        assert get_prizes(2,list(range(4))) == [0,1]
        #mocked.choice() called with ([0,1,2]) then with ([1,2])

#patch over with mocked choice()
@mock.patch('random.choice',mock_choice)
def test_get_opened_doors():
    assert get_opened_doors(list(range(3)),1,[0],1) == [2]
    #mocked.choice() called once with ([2])
    assert get_opened_doors(list(range(3)),1,[1],1) == [0]
    #mocked.choice() called once with ([0,2])
    assert get_opened_doors(list(range(3)),2,[0],1) == [1]
    #mocked.choice() called once with ([1])
    assert get_opened_doors(list(range(4)),1,[0],1) == [2]
    #mocked.choice() called once with ([2,3])
    assert get_opened_doors(list(range(4)),1,[0],2) == [2,3]
    #mocked.choice() called  with ([2,3]) then with ([3])
    assert get_opened_doors(list(range(4)),1,[0,1],1) == [2]
    #mocked.choice() called once with ([2,3])
    assert get_opened_doors(list(range(4)),2,[0,1],1) == [3]
    #mocked.choice() called once with ([3])

#patch over with mocked choice()
@mock.patch('random.choice',mock_choice)
def test_swap():
    assert swap(list(range(3)),1,[0]) == 2
    #mocked.choice() called once with ([2])
    assert swap(list(range(3)),1,[2]) == 0
    #mocked.choice() called once with ([0])
    assert swap(list(range(4)),1,[0,2]) == 3
    #mocked.choice() called once with ([3])

#path over with mocked choice()
@mock.patch('random.choice',mock_choice)
def test_play_round():
    assert play_round() == False
    #mocked.choice() called with ([0,1,2]) then ([0,1,2]) then ([1,2]) then ([2])

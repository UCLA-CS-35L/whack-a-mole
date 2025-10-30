from algo import coin_change


def test_coin_change_example():
    coins = [1, 2, 5]
    amount = 11
    assert coin_change(coins, amount) == 3

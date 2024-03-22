from Matemathic_Function.src.matemathic_function.hello import hello


def test_hello():
    # Given
    given_str = "Hello friend"
    given_name = "friend"
    # When
    test_str = hello(given_name)
    # then
    assert given_str == test_str

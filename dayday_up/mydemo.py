import pytest

@pytest.fixture
def my_string():
    return "Hello, "

@pytest.fixture
def my_number():
    return 42

@pytest.fixture
def combined_data(my_string, my_number):
    return my_string + str(my_number)

def test_combined_data(combined_data):
    assert combined_data == "Hello, 42"

# 执行测试
if __name__ == "__main__":
    pytest.main()

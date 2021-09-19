import pytest


def test_one(d: "asdf"):
    print("运行测试one")

if __name__ == '__main__':
    pytest.main(["test_demo.py", "-s"])
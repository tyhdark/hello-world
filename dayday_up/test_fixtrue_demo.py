import pytest
from loguru import logger


class TestFixDemo(object):

    @pytest.fixture(scope='class', params=[1, 3, 2])
    def test_my_demo(self, request):
        logger.info("开始")
        return request.param

    def test_one(self, test_my_demo):
        logger.info(f"test_my_demo============{str(test_my_demo)}")
        logger.error(f"test_my_demo============{str(test_my_demo)}")

    def test_two(self, test_my_demo):
        logger.info(f"test_my_demo============{str(test_my_demo)}")

# import pytest
#
# class TestDemo:
#     @pytest.fixture(params=[1, 2, 3])
#     def my_fixture(self, request):
#         return request.param
#
#     def test_using_fixture(self, my_fixture):
#         assert my_fixture > 0
#         print(f"Testing with param: {my_fixture}")

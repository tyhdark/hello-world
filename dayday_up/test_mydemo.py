import logging
import random

import pytest

# 创建一个 fixture 函数，用于设置和清理资源
from loguru import logger

global_variable = 2
is_end = True
user_addr = None


# 想要解决 创建新地址后 A函数执行完所有的parametrize参数后 再创建新地址 去执行B函数里所有的parametrize

class TestDemo(object):

    @pytest.fixture
    def cleanup_my_resources(self):
        global is_end
        global user_addr
        logger.info(f"start global_variable={global_variable}------------")
        if is_end:
            logger.info(f"开始----is_end={is_end}------创建用户--")
            user_addr = str(random.randint(1, 10) * 1000)
            my_addr = user_addr
            is_end = False
        else:
            logger.info(f"开始----is_end={is_end}------使用用户--")
            my_addr = user_addr

        yield my_addr
        if is_end:
            user_addr = None
            logger.error("结束------is_end={is_end}------删除用户--------")

    # 使用 fixture 执行清理操作
    @pytest.mark.parametrize("send_fees", (9999, 100, 100.0, 100.1, 100.49, 100.9, 200, "end"))
    def test_my_teardown(self, cleanup_my_resources, send_fees):
        logger.info("Running test_with_teardown")
        global user_addr
        logger.info(f"我的地址 my_addr==================>{user_addr}")
        if "end" is send_fees:
            global is_end
            is_end = True
            pytest.skip("最后一个跳过-------------》")

        else:
            logger.info(f"send_fees={send_fees},self={self}-------do something------------")

    # 使用 fixture 执行清理操作
    @pytest.mark.parametrize("send_fees", (9999, 100, 100.0, 100.1, 100.49, 100.9, 200, "end"))
    def test_your_teardown(self, cleanup_my_resources, send_fees):
        logger.info("Running test_your_teardown")
        global user_addr
        logger.info(f"你的地址 your_addr==================>{user_addr}")
        if "end" is send_fees:
            global is_end
            is_end = True
            pytest.skip("最后一个跳过-------------》")

        else:
            logger.info(f"send_fees={send_fees},self={self}-------do something------------")

# 运行测试

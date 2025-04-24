import logging
logger = logging.getLogger(__name__)

def test_login(login_page):
    logger.info("info")
    logger.debug("debug")
    assert login_page.title == "Sign in [Jenkins]"


def test_main_page(main_page):
    logger.info("info")
    logger.debug("debug")
    assert main_page.title == "Dashboard [Jenkins]" + '1'


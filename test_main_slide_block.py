import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageobjects.main_page import MainPage


def setup():
    pytest.driver = webdriver.Chrome("./drivers/chromedriver")
    pytest.driver.get(MainPage.default_url)


def teardown():
    pytest.driver.close()


def test_switch_slider():
    # Assign
    test_graph_header = pytest.driver.find_elements_by_xpath(
        MainPage.graph_header_blocks["imperfections"])[0]
    content_status = pytest.driver.find_elements_by_xpath(
        MainPage.graph_content_blocks["imperfections"])[0]
    expected_active_element = MainPage.graph_content_blocks["imperfections"] + \
        "[contains(@style, 'display: block')]"

    # Act
    test_graph_header.click()
    WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, expected_active_element)))

    test_graph_header.click()
    time.sleep(2)  # This animation hard to track through CSS so it's hardcoded

    # Assert
    display_status = content_status.value_of_css_property("display")
    assert display_status != "none"

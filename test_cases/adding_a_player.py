import os
import unittest
import time

from selenium import webdriver

from pages.add_page import AddingPage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en/players/add')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_player(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        time.sleep(15)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.click_on_the_add_player_button()
        time.sleep(5)
        new_player = AddingPage(self.driver)
        new_player.title_of_page()
        new_player.type_in_email("it_qa@gmail.com")
        new_player.type_in_name("Alina")
        new_player.type_in_surname("Nikitina")
        new_player.type_in_main_position("2")
        time.sleep(10)
        new_player.type_in_age("02.05.1996")
        new_player.type_in_phone("25475546")
        time.sleep(10)
        new_player.click_on_the_submit_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()


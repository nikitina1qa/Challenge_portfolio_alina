import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"
    add_player_button_xpath = "//main/div[3]/div[2]/descendant::a/button/span[1]"

    def title_of_page(self):
        time.sleep(4)
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)





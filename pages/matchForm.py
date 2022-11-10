from pages.base_page import BasePage


class MatchForm(BasePage):
    main_page_button_xpath = "(//div/child::span)[1]"
    players_button_xpath = "//*[text()= 'Players']"
    adding_a_match_button_xpath = "//ul[2]//descendant::span"
    matches_button_xpath = "//ul[2]//child::div//following-sibling::div//child::span[text()='Matches']"
    reports_button_xpath = "//ul[2]//child::div//following-sibling::div//child::span[text()='Reports']"
    language_button_xpath = "(//ul[3]//descendant::span)[1]"
    sign_out_button_xpath = "//*[text()='Sign out']"
    my_team_field_xpath = "//input[@name='myTeam']"
    enemy_team_field_xpath = "//input[@name='enemyTeam']"
    date_field_xpath = "//input[@name='date']"


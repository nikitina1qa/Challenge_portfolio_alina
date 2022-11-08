from pages.base_page import BasePage


class MatchForm(BasePage):
    main_page_button_xpath = "(//div/child::span)[1]"
    players_button_xpath = "//*[text()= 'Players']"
    language_button_xpath = "(//div/following-sibling::div/child::span)[4]"
    sign_out_button_xpath = "//*[text()='Sign out']"
    logo_image_xpath = "//div[@title='Logo Scouts Panel']"
    add_player_button_xpath = "//span[contains(text(),'Add player')]"
    scouts_panel_button_xpath = "//div/descendant::span[text()='Dev team contact']"
    last_created_player_button_xpath = "(//h6//following-sibling::a)[1]//child::span[1]"
    last_updated_player_button_xpath = "(//h6/following-sibling::a/descendant::span)[3]"
    last_created_match_button_xpath = "(//h6[text()='Last created match']/following-sibling::a/descendant::span)[1]"
    last_updated_match_button_xpath = "(//h6[text()='Last updated match']/following-sibling::a/descendant::span)[1]"
    last_updated_report_button_xpath = "(//a[contains(@href,'/en')])[last()]/descendant::span[1]"
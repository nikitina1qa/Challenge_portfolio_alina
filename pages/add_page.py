from pages.base_page import BasePage


class AddingPage(BasePage):
    email_field_xpath = "//input[@name='email']"
    name_field_xpath = "//input[@name='name']"
    surname_field_xpath = "//input[@name='surname']"
    main_position_field_xpath = "//input[@name='mainPosition']"
    age_field_xpath = "//input[@name='age']"
    phone_field_xpath = "//input[@name ='phone']"
    submit_button_xpath = "//button[@type ='submit']/child::span[1]"
    adding_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    expected_title = "Add player"
    title_of_box_xpath = "//form/descendant::div/div/span[1]"
    header_of_box = "Add player"

    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_phone(self, phone):
        self.field_send_keys(self.phone_field_xpath, phone)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_field_xpath, main_position)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.adding_url) == self.expected_title

import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait
from data.data import phone_number, card_number, card_code, message_for_driver
from helpers.retrieve_code import retrieve_phone_code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_tariff_icon = (By.XPATH, '//div[@class="tcard-title" and text()= "Comfort"]')
    comfort_tariff_assert = (By.CSS_SELECTOR, '.tariff-cards .tcard.active .tcard-title')
    phone_number_button = (By.XPATH, '//div[@class="np-text" and text()= "Número de teléfono"]')
    phone_number_assert = (By.CSS_SELECTOR, '.np-button.filled .np-text')
    phone_number_field = (By.ID, 'phone')
    phone_submit_button = (By.CSS_SELECTOR, '.button.full')
    phone_code_field = (By.ID, 'code')
    code_submit_button = (By.XPATH, '//button[@class="button full" and text()= "Confirmar"]')
    payment_method_button = (By.XPATH, '//div[@class="pp-text" and text()= "Método de pago"]')
    add_card_button = (By.XPATH, '//div[@class="pp-title" and text()= "Agregar tarjeta"]')
    card_number_field = (By.ID, 'number')
    card_submit_button = (By.XPATH, '//button[@class="button full" and text()= "Agregar"]')
    payment_method_card_title = (By.XPATH, '//div[@class="pp-title" and text()="Tarjeta"]')
    payment_method_close_button = (By.XPATH, '//div[@class="payment-picker open"]'
                                             '//button[@class="close-button section-close"]')
    driver_comment_field = (By.ID, 'comment')
    blanket_and_tissues_switch = (By.XPATH, '//div[@class="tariff-picker shown"]'
                                            '//div[contains(@class, "r-sw-container")][.//div[text()="Manta y pañuelos"]]'
                                            '//span[contains(@class, "slider")]')
    ice_cream_plus_button = (By.XPATH, '//div[@class="tariff-picker shown"]'
                                       '//div[contains(@class, "r-counter-container") and .//div[text()="Helado"]]'
                                       '//div[@class="counter-plus"]')
    ice_cream_count = (By.XPATH, '//div[@class="tariff-picker shown"]'
                                   '//div[contains(@class, "r-counter-container") and .//div[text()="Helado"]]'
                                   '//div[@class="counter-value"]')
    request_taxi_smart_button =(By.CSS_SELECTOR, '.smart-button-wrapper .smart-button')
    search_car_modal = (By.XPATH, '//div[@class="order shown"]'
                                  '//div[@class="order-header-title" and text()="Buscar automóvil"]')
    car_number = (By.CSS_SELECTOR, '.order-number .number')
    driver_card = (By.CSS_SELECTOR, '.order-subbody .order-btn-group')


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def set_from(self, from_address):
        self.wait.until(
            EC.visibility_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
              self.wait.until(
            EC.visibility_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_request_taxi_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.request_taxi_button)
        )
    def click_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_tariff_icon(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.comfort_tariff_icon)
        )

    def click_comfort_tariff_icon(self):
        self.get_comfort_tariff_icon().click()

    def get_comfort_tariff_assert(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.comfort_tariff_assert)
        )

    def get_phone_number_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.phone_number_button)
        )

    def click_phone_number_button(self):
        self.get_phone_number_button().click()

    def set_phone_number(self):
        self.wait.until(
            EC.visibility_of_element_located(self.phone_number_field)
        ).send_keys(phone_number)

    def get_phone_submit_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.phone_submit_button)
        )

    def click_phone_submit_button(self):
        self.get_phone_submit_button().click()

    def set_phone_code_field(self):
        phone_code = retrieve_phone_code(self.driver)
        self.wait.until(
            EC.visibility_of_element_located(self.phone_code_field)
        ).send_keys(phone_code)

    def get_code_submit_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.code_submit_button)
        )

    def click_code_submit_button(self):
        self.get_code_submit_button().click()

    def get_phone_number_assert(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.phone_number_assert)
        ).text

    def get_payment_method_button(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.payment_method_button)
        )

    def click_payment_method_button(self):
        self.get_payment_method_button().click()

    def get_add_card_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.add_card_button)
        )

    def click_add_card_button(self):
        self.get_add_card_button().click()

    def set_card_number_field(self):
        field = self.wait.until(
            EC.element_to_be_clickable(self.card_number_field)
            )
        field.click()
        field.send_keys(card_number + Keys.TAB + card_code + Keys.TAB)

    def get_card_submit_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.card_submit_button)
        )

    def click_card_submit_button(self):
        self.get_card_submit_button().click()

    def get_payment_method_card_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.payment_method_card_title)
        )

    def get_payment_method_close_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.payment_method_close_button)
        )

    def click_payment_method_close_button(self):
        self.get_payment_method_close_button().click()

    def set_driver_comment(self):
        self.wait.until(
            EC.visibility_of_element_located(self.driver_comment_field)
        ).send_keys(message_for_driver)

    def get_driver_comment_assert(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.driver_comment_field)
        ).get_property('value')

    def click_blanket_and_tissues_switch(self):
        switch = self.wait.until(
            EC.presence_of_element_located(self.blanket_and_tissues_switch)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", switch)
        switch.click()

    def get_blanket_and_tissues_switch_assert(self):
        time.sleep(0.5)
        active_color = self.wait.until(
            EC.visibility_of_element_located(self.blanket_and_tissues_switch)
        ).value_of_css_property("background-color")

        return Color.from_string(active_color).hex

    def order_two_ice_creams(self):
        ice_cream = self.wait.until(
            EC.presence_of_element_located(self.ice_cream_plus_button)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ice_cream)
        add_ice_cream = self.wait.until(
            EC.element_to_be_clickable(self.ice_cream_plus_button)
        )
        add_ice_cream.click()
        add_ice_cream.click()

    def get_ice_cream_assert(self):
        return self.wait.until(
            EC.presence_of_element_located(self.ice_cream_count)
        ).text

    def get_request_taxi_smart_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.request_taxi_smart_button)
        )

    def click_request_taxi_smart_button(self):
        self.get_request_taxi_smart_button().click()

    def get_search_car_modal(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.search_car_modal)
        )

    def wait_for_car_search_countdown(self):
        return WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(self.car_number)
        )

    def get_driver_card(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.driver_card)
        )
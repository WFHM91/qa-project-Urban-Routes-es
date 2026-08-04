from data import data
from data.data import address_from, address_to
from pages.urban_routes_page import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service



class TestUrbanRoutes:

    driver = None


    def setup_method(self):
        options = Options()
        options.set_capability("goog:loggingPrefs",{"performance":"ALL"})
        self.driver = webdriver.Chrome(service=Service(), options=options)
        self.driver.get(data.urban_routes_url)
        self.routes_page = UrbanRoutesPage(self.driver)

    def teardown_method(self):
        if self.driver:
            self.driver.quit()

# 1. Configurar la dirección
    def test_set_route(self):
        self.routes_page.set_route(address_from, address_to)

        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

# 2. Seleccionar la tarifa Comfort
    def test_select_comfort_tariff(self):
    # Precondiciones:
        self.routes_page.set_route(address_from, address_to)

    # Test:
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_tariff_icon()
        assert_text = self.routes_page.get_comfort_tariff_assert().text

        assert assert_text == "Comfort"

# 3. Rellenar el número de teléfono
    def test_set_phone_number(self):
    # Precondiciones:
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.set_comfort_tariff()

    # Test:
        self.routes_page.set_phone_number_and_code()
        actual_phone = self.routes_page.get_phone_number_assert()

        assert actual_phone == data.phone_number, f"Esperado {data.phone_number}, pero se obtuvo {actual_phone}"

# 4. Agregar una tarjeta de crédito
    def test_add_credit_card(self):
    # Precondiciones:
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.set_comfort_tariff()
        self.routes_page.set_phone_number_and_code()

    # Test:
        self.routes_page.set_payment_method()

        assert self.routes_page.get_payment_method_card_title().is_displayed(), "La tarjeta de crédito no es visible."

# 5. Escribir un mensaje para el controlador
    def test_set_driver_comment(self):
    # Precondiciones:
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.set_comfort_tariff()
        self.routes_page.set_phone_number_and_code()
        self.routes_page.set_payment_method()
        self.routes_page.click_payment_method_close_button()

    # Test:
        self.routes_page.set_driver_comment()
        comment_text = self.routes_page.get_driver_comment_assert()

        assert comment_text == data.message_for_driver

# 6. Pedir una manta y pañuelos
    def test_order_blanket_and_tissues(self):
    # Precondiciones:
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.set_comfort_tariff()
        self.routes_page.set_phone_number_and_code()
        self.routes_page.set_payment_method()
        self.routes_page.click_payment_method_close_button()

    # Test:
        self.routes_page.click_blanket_and_tissues_switch()
        switch_active = self.routes_page.get_blanket_and_tissues_switch_assert()

        assert switch_active is True

# 7. Pedir 2 helados
    def test_order_two_ice_creams(self):
    # Precondiciones:
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.set_comfort_tariff()
        self.routes_page.set_phone_number_and_code()
        self.routes_page.set_payment_method()
        self.routes_page.click_payment_method_close_button()

    # Test:
        self.routes_page.order_two_ice_creams()
        ice_cream_count = self.routes_page.get_ice_cream_assert()

        assert ice_cream_count == "2"

# 8. Aparece el modal para buscar un taxi
    def test_car_search_modal_is_displayed(self):
    # Precondiciones:
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.set_comfort_tariff()
        self.routes_page.set_phone_number_and_code()
        self.routes_page.set_payment_method()
        self.routes_page.click_payment_method_close_button()

    # Test:
        self.routes_page.click_request_taxi_smart_button()

        assert self.routes_page.get_search_car_modal().is_displayed(), "El modal 'Buscar automóvil' no es visible."

# 9. Esperar a que aparezca la información del conductor en el modal
    def test_wait_driver_card_is_displayed(self):
    # Precondiciones:
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.set_comfort_tariff()
        self.routes_page.set_phone_number_and_code()
        self.routes_page.set_payment_method()
        self.routes_page.click_payment_method_close_button()
        self.routes_page.set_driver_comment()
        self.routes_page.click_request_taxi_smart_button()

    # Test:
        car_number_element = self.routes_page.wait_for_car_search_countdown()

        assert car_number_element.is_displayed(), "El 'número de placa' no es visible."
        assert self.routes_page.get_driver_card().is_displayed(), "La 'información del conductor' no es visible."
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from Infrastructure.Infra.dal.web_driver_extention.web_driver_extension import DriverEX
from Infrastructure.objects.objects_ui.google_images_page_ui import GoogleImagesPageUi


class GoogleSearchImagePageUi:
    def __init__(self, driver: webdriver) -> None:
        self.__driver = driver
        self.__search_images_button = "div[aria-label='{name}']"

    # locators
        self.__search_for_images_text_box = (By.CSS_SELECTOR, "textarea[name='q']")

    def set_image_name(self, name: str):
        DriverEX.send_keys_auto(driver=self.__driver,
                                by=self.__search_for_images_text_box, input_text=name)
        return self

    def click_on_search_images_button(self, name: str) -> GoogleImagesPageUi:
        search_images_button_ext = (By.CSS_SELECTOR, self.__search_images_button.format(name=name.lower()))
        DriverEX.force_click(driver=self.__driver, by=search_images_button_ext)

        return GoogleImagesPageUi(self.__driver)

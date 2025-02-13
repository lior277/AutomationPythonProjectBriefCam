from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import logging


class TestSuitBase:
    logger = logging.getLogger(__name__)

    @staticmethod
    def get_driver() -> webdriver:
        try:
            chrome_options = TestSuitBase.get_web_driver_options()

            # Automatically fetch the correct version of chromedriver
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),  # Automatically gets the right version
                options=chrome_options
            )

            driver.maximize_window()
            return driver
        except Exception as e:
            TestSuitBase.logger.error(f"Failed to create WebDriver: {e}")
            raise

    @staticmethod
    def driver_dispose(driver: webdriver = None):
        if driver is not None:
            try:
                driver.close()
                driver.quit()
            except Exception as e:
                TestSuitBase.logger.error(f"Error disposing driver: {e}")

    @staticmethod
    def get_web_driver_options() -> ChromeOptions:
        options = ChromeOptions()

        # Language and locale settings
        options.add_argument('--lang=en-GB')
        options.add_argument('--accept-language=en-US,en;q=0.9')

        # Security and performance options
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-browser-side-navigation')
        options.add_argument('--enable-features=NetworkService,NetworkServiceInProcess')

        # Optional: Add headless mode for CI/CD or background testing
        # options.add_argument('--headless')

        # Optional: Disable extensions and plugins
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-plugins')

        return options
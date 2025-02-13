import pytest
from Infrastructure.objects.objects_api.episode_page_api import EpisodePageApi
from Infrastructure.objects.objects_ui.google_home_page_ui import GoogleHomePageUi
from Infrastructure.Infra.dal.data_reposetory.data_rep import DataRep

from tests.test_suit_Base import TestSuitBase  # Import TestSuitBase


@pytest.mark.asyncio
class TestVerifyCharacterLocation(TestSuitBase):  # Inherit from TestSuitBase (optional if you need base functionality)

    async def test_verify_characters_location_is_the_same_ui(self):
        # Get the WebDriver directly from TestSuitBase
        driver = TestSuitBase.get_driver()  # This will call the method in TestSuitBase to get the driver

        # Test setup: Use the driver to interact with the page
        episode_page_api = EpisodePageApi()
        character_details = await episode_page_api.randomly_choose_two_characters_pipe_async()

        # character 1
        character_1 = character_details[0]
        character_1_id = character_1.id
        character_1_name = character_1.name
        character_1_location = character_1.location

        driver.get(DataRep.google_home_page_url)

        google_home_page = GoogleHomePageUi(driver)
        google_search_image_page = google_home_page.click_on_images_link()

        google_search_image_page.set_image_name(character_1_name)
        google_images_page = google_search_image_page.click_on_search_images_button(character_1_name)
        google_images_page.click_on_image_by_character_id(character_1_id)
        # google_images_page.capture_image_from_image_details(character_1_name, character_1_id)

        # character 2
        character_2 = character_details[1]
        character_2_id = character_2.id
        character_2_name = character_2.name
        character_2_location = character_2.location
        character_2_image_url = character_2.image

        driver.get(character_2_image_url)
        google_images_page.capture_image(character_2_name, character_2_id)

        if character_1_location != character_2_location:
            print(f"First character location: {character_1_location} for {character_1_name} and "
                  f"second character location: {character_2_location} for {character_2_name}.")
        else:
            print(f"Both characters are from the location: {character_1_location}")

        # Assert that both locations match
        assert character_1_location != character_2_location, \
            f"expected Character 1 location: {character_1_location}, " \
            f"expected Character 2 location: {character_2_location}"

        # Cleanup: Dispose of the WebDriver
        TestSuitBase.driver_dispose(driver=driver)

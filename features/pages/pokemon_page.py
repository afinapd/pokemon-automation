import time

from features.core.reusable_page import ReusablePage
from features.locators.locator import LocatorPokemonPage
from features.locators.locator import Locator

from selenium.webdriver.common.by import By

class PokemonPage(ReusablePage):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = PokemonPage()
        return cls.instance

    def __init__(self):
        super().__init__()

    def clickCTA(self, CTA):
        if CTA == "Pokédex":
            super().perform_action_on_element(LocatorPokemonPage.PokedexCTA, "click")
        elif CTA == "Explore More Pokemon":
            super().perform_action_on_element(LocatorPokemonPage.ExploreMoreCTA, "click")
        else:
            print("not found")

    def acceptCache(self):
        super().element_exists(LocatorPokemonPage.CloseCache)
        super().perform_action_on_element(LocatorPokemonPage.CloseCache, "click")

    def searchPokemon(self, keyword):
        super().perform_action_on_element(LocatorPokemonPage.SearchInput, "clear")
        super().perform_action_on_element(LocatorPokemonPage.SearchInput, "type", keyword)
        super().perform_action_on_element(LocatorPokemonPage.SearchInput, "enter")

    def selectPokemon(self, result):
        super().element_exists(LocatorPokemonPage.ResultImage)
        super().perform_action_on_element(LocatorPokemonPage.ResultImage, "click")

    def verifyPage(self, page):
        super().assert_element_contain_text(page)

    def scrollDownDetail(self):
        super().perform_action_on_element(LocatorPokemonPage.ExploreMoreCTA, "scroll_into_middle")

    def scrollDownToShowAllPokemon(self):
        super().perform_action_on_element(LocatorPokemonPage.LoadMoreCTA, "scroll_into_middle")
        super().perform_action_on_element(LocatorPokemonPage.LoadMoreCTA, "click")

pokemonPage = PokemonPage.get_instance()

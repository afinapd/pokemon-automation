from selenium.webdriver.common.by import By
class Locator:
    def __init__(self, l_type, selector):
        self.l_type = l_type
        self.selector = selector

    def parameterize(self, *args):
        self.selector = self.selector.format(*args)

class LocatorPokemonPage:
    CloseCache = Locator(By.ID, "onetrust-close-btn-container")
    PokedexCTA = Locator(By.CSS_SELECTOR, ".title_pokeball")
    SearchInput = Locator(By.ID, "searchInput")
    ResultImage = Locator(By.CSS_SELECTOR, "figure img")
    TitlePage = Locator(By.XPATH, "//div[4]/section/div[2]/div")
    ExploreMoreCTA = Locator(By.CSS_SELECTOR, ".content-block-half > .button")
    LoadMoreCTA = Locator(By.CSS_SELECTOR, "#loadMore > .button-lightblue")
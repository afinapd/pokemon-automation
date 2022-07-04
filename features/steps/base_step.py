from behave import *

from features.core.base_page import basePage
from features.pages.pokemon_page import pokemonPage


@given('launch chrome browser')
def lauchBrowser(self):
    basePage.get_driver()

@step('open pokemon page')
def openPokemonHomePage(self):
    basePage.navigate("https://www.pokemon.com/us/")
    pokemonPage.acceptCache()

@step('click CTA "{CTA}"')
def clickCTA(self, CTA):
    pokemonPage.clickCTA(CTA)

@step('search Pokemon "{keyword}"')
def searchPokemon(self, keyword):
    pokemonPage.searchPokemon(keyword)

@step('select "{result}"')
def selectPokemon(self, result):
    pokemonPage.selectPokemon(result)

@step('scrolling down to show all detail about "{detail}"')
def showDetailPokemon(self, detail):
    pokemonPage.verifyPage(detail)
    pokemonPage.scrollDownDetail()

@step('scrolling down to show all pokemon')
def scrollPokemon(self):
    pokemonPage.scrollDownToShowAllPokemon()

@step('close browser')
def closeBrowser(self):
    basePage.close_browser()

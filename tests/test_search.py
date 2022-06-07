# These tests cover DuckDuckGo searches

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


def test_basic_duckduckgo_search(browser):
  search_page = DuckDuckGoSearchPage(browser)
  result_page = DuckDuckGoResultPage(browser)
  PHRASE = "mekas"

  # Given the DuckDuckGo home page is displayed
  search_page.load()

  # When the user searches for "mekas"
  search_page.search(PHRASE)

  # Then the search result title contains "mekas"
  assert PHRASE in result_page.title()

  # And the search result query is "mekas"
  assert PHRASE == result_page.search_input_value()

  # And the search result links pertain to "mekas"
  titles = result_page.result_link_titles()
  matches = [t for t in titles if PHRASE.lower() in t.lower()]
  assert len(matches) > 0
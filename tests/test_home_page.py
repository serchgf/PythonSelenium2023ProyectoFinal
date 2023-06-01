from src.page_objects.home_page import HomePage


def test_search(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    home_page.search("Iphone")
    home_page.take_screenshot("test_search")

def test_validate_menu_bar_elements(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    expected_menu_elements = ['Desktops', 'Laptops & Notebooks', 'Components', 'Tablets', 'Software', 'Phones & PDAs',
                              'Cameras', 'MP3 Players']
    actual_menu_elements = home_page.obtain_menu_elements()
    assert expected_menu_elements in actual_menu_elements, f"Elements in menu bar should be: {expected_menu_elements}"
    home_page.take_screenshot("test_validate_menu_bar_elements")
from web import forms


def test_validate_2_words_city_name_success() -> None:
    assert forms.validate_city_name("Zduńska Wola") == "Zdunska-Wola"


def test_validate_1_word_city_name_success() -> None:
    assert forms.validate_city_name("Warszawa") == "Warszawa"


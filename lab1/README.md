# Laboratorium 1

W tym laboratorium zapoznamy się z:
- podstawami testowania oprogramowania
- pakietem `pytest` w języku `python`
- napiszemy swój pierwszy test jednostkowy

## Wiedza teoretyczna
Porozmawiamy więcej na następnych laboratorium, ale już teraz możesz to przeczytać:
1) [Pytest](https://docs.pytest.org/en/7.1.x/)
2) [Whitebox](https://en.wikipedia.org/wiki/White-box_testing)/[BlackBox](https://en.wikipedia.org/wiki/Black-box_testing) testowanie
3) [Unit/Integration/E2E](https://codeahoy.com/2016/07/05/unit-integration-and-end-to-end-tests-finding-the-right-balance/) testy

## Tok działań

Przed rozpoczęciem działań, musimy zainstalować pakiet [pytest](https://docs.pytest.org/en/7.1.x/). W linii poleceń należy wpisać:
```sh
    python3 -m pip install pytest
```

W folderze znajdują się dwa pliki:
- ***calculator.py*** - plik z kodem źródłowym przykładowej biblioteki.
- ***test_calculator.py*** - plik z testami biblioteki


Zadanie:
1) Zobaczyć co znajduje się w plikach `calculator.py` i `test_calculator.py`.
2) Porównać to z przykładem na stronie [pytest](https://docs.pytest.org/en/7.1.x/)
3) wystartować testy za pomocą komendy ```pytest``` w linii poleceń.
4) Pomyłka? Zobacz komentarze w pliku `test_calculator.py` i napraw/zaimplementuj testy.
5) Wywołałeś komendę `pytest` i wszystko działa? Gratuluję, napisałeś(aś) swój pierwszy test jednostkowy.

# Лабораторная работа № 2. Модульные и интеграционные тесты

Простой калькулятор на Python с тестами.

Выполнили: Правиков Д. В., Корнилова Л. Д.

## Файлы

- `calculator.py` — функции калькулятора (сложение, вычитание, умножение,
  деление, степень, корень, факториал, память);
- `main.py` — окно программы на Tkinter;
- `test_calculator.py` — тесты;
- `docs/Отчет_ЛР2.docx` — отчёт;
- `docs/Отчет_ЛР2.pdf` — отчёт в PDF;
- `docs/calculator_window.png` — скриншот окна программы;
- `docs/tests_output.txt` — вывод тестов;

## Запуск программы

```
python main.py
```

## Запуск тестов

```
python -m unittest -v
```

Все 23 теста проходят:

```
Ran 23 tests in 0.001s
OK
```

## Как пересобрать отчёт

```
python tools\make_screenshot.py
python tools\build_report.py
```

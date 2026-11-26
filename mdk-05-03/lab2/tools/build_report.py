"""Сборка простого отчёта по лабораторной работе № 2 (DOCX).

Оформление по ЕГР: Times New Roman 14 пт, полуторный интервал,
абзацный отступ 1,25 см, код — Arial 10 пт, номера страниц внизу справа.
"""

import os

from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import (WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT,
                            WD_TAB_LEADER)
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Mm, Pt, RGBColor

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(BASE, "docs")
OUT = os.path.join(DOCS, "Отчет_ЛР2.docx")

BODY_FONT = "Times New Roman"
CODE_FONT = "Arial"

listing_number = 0


def set_run_font(run, name, size, bold=False):
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = RGBColor(0, 0, 0)
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for attribute in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attribute), name)


def set_style_font(style, name, size, bold=False):
    style.font.name = name
    style.font.size = Pt(size)
    style.font.bold = bold
    style.font.color.rgb = RGBColor(0, 0, 0)
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for attribute in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attribute), name)


def add_body(doc, text, indent=True, align=WD_ALIGN_PARAGRAPH.JUSTIFY,
             space_before=0, keep_next=False):
    paragraph = doc.add_paragraph()
    paragraph.alignment = align
    paragraph.paragraph_format.first_line_indent = Cm(1.25) if indent else Cm(0)
    paragraph.paragraph_format.space_before = Pt(space_before)
    paragraph.paragraph_format.keep_with_next = keep_next
    run = paragraph.add_run(text)
    set_run_font(run, BODY_FONT, 14)
    return paragraph


def add_h1(doc, text):
    paragraph = doc.add_paragraph(style="Heading 1")
    paragraph.paragraph_format.page_break_before = True
    run = paragraph.add_run(text)
    set_run_font(run, BODY_FONT, 14, bold=True)
    return paragraph


def add_h2(doc, text):
    paragraph = doc.add_paragraph(style="Heading 2")
    run = paragraph.add_run(text)
    set_run_font(run, BODY_FONT, 14)
    return paragraph


def add_caption(doc, text, align=WD_ALIGN_PARAGRAPH.LEFT, keep_next=False):
    paragraph = doc.add_paragraph()
    paragraph.alignment = align
    paragraph.paragraph_format.first_line_indent = Cm(0)
    paragraph.paragraph_format.space_before = Pt(6)
    paragraph.paragraph_format.space_after = Pt(3)
    paragraph.paragraph_format.keep_with_next = keep_next
    run = paragraph.add_run(text)
    set_run_font(run, BODY_FONT, 14)
    return paragraph


def add_listing(doc, path, title):
    global listing_number
    listing_number += 1
    add_caption(doc, f"Листинг {listing_number} – {title}", keep_next=True)
    with open(path, encoding="utf-8") as source:
        code = source.read().rstrip("\n")
    paragraph = doc.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
    paragraph.paragraph_format.first_line_indent = Cm(0)
    paragraph.paragraph_format.line_spacing = 1.0
    paragraph.paragraph_format.space_after = Pt(12)
    run = paragraph.add_run(code)
    set_run_font(run, CODE_FONT, 10)


def add_listing_text(doc, text, title):
    global listing_number
    listing_number += 1
    add_caption(doc, f"Листинг {listing_number} – {title}", keep_next=True)
    paragraph = doc.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
    paragraph.paragraph_format.first_line_indent = Cm(0)
    paragraph.paragraph_format.line_spacing = 1.0
    paragraph.paragraph_format.space_after = Pt(12)
    run = paragraph.add_run(text.rstrip("\n"))
    set_run_font(run, CODE_FONT, 10)


def add_figure(doc, filename, caption, width_cm):
    paragraph = doc.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.paragraph_format.first_line_indent = Cm(0)
    paragraph.paragraph_format.space_before = Pt(12)
    paragraph.paragraph_format.space_after = Pt(3)
    paragraph.paragraph_format.keep_with_next = True
    paragraph.add_run().add_picture(os.path.join(DOCS, filename), width=Cm(width_cm))
    add_caption(doc, caption, align=WD_ALIGN_PARAGRAPH.CENTER)


def add_page_number(paragraph):
    run = paragraph.add_run()
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instruction = OxmlElement("w:instrText")
    instruction.set(qn("xml:space"), "preserve")
    instruction.text = " PAGE "
    separate = OxmlElement("w:fldChar")
    separate.set(qn("w:fldCharType"), "separate")
    text = OxmlElement("w:t")
    text.text = "2"
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    for element in (begin, instruction, separate, text, end):
        run._r.append(element)
    set_run_font(run, BODY_FONT, 14)


def add_toc_field(paragraph):
    run = paragraph.add_run()
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    begin.set(qn("w:dirty"), "true")
    instruction = OxmlElement("w:instrText")
    instruction.set(qn("xml:space"), "preserve")
    instruction.text = ' TOC \\o "1-2" \\h \\z \\u '
    separate = OxmlElement("w:fldChar")
    separate.set(qn("w:fldCharType"), "separate")
    text = OxmlElement("w:t")
    text.text = "Содержание"
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    for element in (begin, instruction, separate, text, end):
        run._r.append(element)


def configure_styles(doc):
    normal = doc.styles["Normal"]
    set_style_font(normal, BODY_FONT, 14)
    normal.paragraph_format.line_spacing = 1.5
    normal.paragraph_format.space_before = Pt(0)
    normal.paragraph_format.space_after = Pt(0)
    normal.paragraph_format.first_line_indent = Cm(1.25)
    normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    for name, bold in (("Heading 1", True), ("Heading 2", False)):
        style = doc.styles[name]
        set_style_font(style, BODY_FONT, 14, bold=bold)
        style.paragraph_format.first_line_indent = Cm(1.25)
        style.paragraph_format.line_spacing = 1.5
        style.paragraph_format.space_before = Pt(12)
        style.paragraph_format.space_after = Pt(12)
        style.paragraph_format.keep_with_next = True
        style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT

    for name, indent in (("TOC 1", 0), ("TOC 2", 0.75)):
        try:
            style = doc.styles[name]
        except KeyError:
            style = doc.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
            style.base_style = doc.styles["Normal"]
        set_style_font(style, BODY_FONT, 14)
        style.paragraph_format.first_line_indent = Cm(0)
        style.paragraph_format.left_indent = Cm(indent)
        style.paragraph_format.line_spacing = 1.5
        style.paragraph_format.space_before = Pt(0)
        style.paragraph_format.space_after = Pt(0)
        style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        style.paragraph_format.tab_stops.add_tab_stop(
            Cm(16.5), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS
        )


def build_title_page(doc):
    def centered(text, size, bold=False, space_before=0):
        paragraph = doc.add_paragraph()
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        paragraph.paragraph_format.first_line_indent = Cm(0)
        paragraph.paragraph_format.line_spacing = 1.0
        paragraph.paragraph_format.space_before = Pt(space_before)
        run = paragraph.add_run(text)
        set_run_font(run, BODY_FONT, size, bold=bold)

    def right(text, size, space_before=0):
        paragraph = doc.add_paragraph()
        paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        paragraph.paragraph_format.first_line_indent = Cm(0)
        paragraph.paragraph_format.line_spacing = 1.0
        paragraph.paragraph_format.space_before = Pt(space_before)
        run = paragraph.add_run(text)
        set_run_font(run, BODY_FONT, size)

    centered("Министерство профессионального образования и занятости "
             "населения Приморского края", 16)
    centered("краевое государственное автономное", 16)
    centered("профессиональное образовательное учреждение", 16)
    centered("«Владивостокский судостроительный колледж»", 16)

    centered("ОТЧЕТ", 22, bold=True, space_before=70)
    centered("по лабораторной работе № 2", 16)
    centered("РАЗРАБОТКА МОДУЛЬНЫХ И ИНТЕГРАЦИОННЫХ ТЕСТОВ", 22,
             bold=True, space_before=24)

    right("Выполнили:", 16, space_before=140)
    right("Д. В. Правиков", 16)
    right("Л. Д. Корнилова", 16)

    centered("2026", 16, space_before=170)


def build_report():
    doc = Document()
    configure_styles(doc)

    section = doc.sections[0]
    section.page_width = Mm(210)
    section.page_height = Mm(297)
    section.left_margin = Cm(3)
    section.right_margin = Cm(1.5)
    section.top_margin = Cm(2)
    section.bottom_margin = Cm(2)
    section.different_first_page_header_footer = True

    footer = section.footer
    footer.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
    add_page_number(footer.paragraphs[0])

    build_title_page(doc)

    toc_title = doc.add_paragraph()
    toc_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    toc_title.paragraph_format.first_line_indent = Cm(0)
    toc_title.paragraph_format.page_break_before = True
    toc_title.paragraph_format.space_after = Pt(12)
    set_run_font(toc_title.add_run("Содержание"), BODY_FONT, 14)

    toc = doc.add_paragraph()
    toc.paragraph_format.first_line_indent = Cm(0)
    toc.paragraph_format.line_spacing = 1.5
    add_toc_field(toc)

    add_h1(doc, "1 Цель работы")
    add_body(doc, "Цель работы — сделать калькулятор на Python и проверить "
                  "его тестами.")
    add_body(doc, "Для этого надо было:")
    for item in (
        "– написать программу с кнопками;",
        "– сделать каждую операцию отдельной функцией;",
        "– написать тесты на каждую функцию;",
        "– запустить тесты и убедиться, что всё работает.",
    ):
        add_body(doc, item)

    add_h1(doc, "2 Код программы")
    add_body(doc, "Программа состоит из двух файлов. В файле calculator.py "
                  "находятся функции, которые считают. В файле main.py "
                  "находится окно с кнопками. Тесты лежат в файле "
                  "test_calculator.py.")

    add_h2(doc, "2.1 Функции калькулятора")
    add_body(doc, "Все вычисления сделаны в файле calculator.py. Каждая "
                  "операция — отдельная функция. Функция получает числа и "
                  "возвращает ответ. Если посчитать нельзя, функция "
                  "возвращает слово «Ошибка». Так работает, например, "
                  "деление на ноль.")
    add_body(doc, "Память калькулятора — это переменная memory. Функция "
                  "memory_save() сохраняет число, memory_get() показывает "
                  "его, memory_add() прибавляет число к памяти, а "
                  "memory_clear() очищает память.")
    add_listing(doc, os.path.join(BASE, "calculator.py"),
                "Функции калькулятора (calculator.py)")

    add_h2(doc, "2.2 Окно программы")
    add_body(doc, "Окно сделано с помощью библиотеки Tkinter. В окне есть "
                  "поле, где показывается число, и кнопки. Когда "
                  "пользователь нажимает кнопку, вызывается функция из "
                  "calculator.py, а ответ показывается в поле. Кнопка C "
                  "очищает поле, кнопки MS, MR, M+ и MC работают с памятью. "
                  "Как выглядит окно, показано на рисунке 1.")
    add_listing(doc, os.path.join(BASE, "main.py"),
                "Окно программы (main.py)")
    add_figure(doc, "calculator_window.png",
               "Рисунок 1 – Окно программы", 7.5)
    add_body(doc, "Программа запускается командой python main.py.")

    add_h2(doc, "2.3 Тесты")
    add_body(doc, "Тесты написаны с помощью библиотеки unittest. На каждую "
                  "функцию сделан свой класс, а внутри класса — методы "
                  "test_.... В тесте программа считает пример, а потом "
                  "ответ сравнивается с правильным. Если ответ не такой, "
                  "тест не проходит. Всего получилось 23 теста.")
    add_listing(doc, os.path.join(BASE, "test_calculator.py"),
                "Тесты (test_calculator.py)")

    add_h1(doc, "3 Результаты тестов")
    add_body(doc, "Тесты запускаются командой python -m unittest -v. Вывод "
                  "программы показан в листинге 4.")
    with open(os.path.join(DOCS, "tests_output.txt"), encoding="utf-8") as source:
        console = "> python -m unittest -v\n" + source.read().rstrip("\n")
    add_listing_text(doc, console, "Результат выполнения тестов")
    add_body(doc, "Все 23 теста прошли. В конце написано OK. Значит, все "
                  "функции считают правильно.")

    add_h1(doc, "4 Ответы на контрольные вопросы")
    answers = [
        "1. Модульное тестирование — это проверка отдельных функций "
        "программы.",
        "2. Цель модульного тестирования — найти ошибки в каждой функции.",
        "3. Модульное тестирование делают по принципу «белого ящика», "
        "потому что программист знает, как устроен код.",
        "4. Вокруг модуля создают заглушки для функций, которые он вызывает.",
        "5. На уровне модулей проще всего найти ошибки в условиях, циклах и "
        "переменных.",
        "6. Ошибки в интерфейсах, совместимости и производительности на "
        "уровне модулей обычно не видны.",
        "7. Стратегию тестирования определяет то, какие ошибки чаще "
        "встречаются и где их проще найти.",
        "8. Интеграционное тестирование — это проверка нескольких модулей "
        "вместе.",
        "9. Интеграционное тестирование тоже работает с интерфейсами "
        "модулей и заглушками, поэтому это развитие модульного.",
        "10. Модульное тестирование проверяет один модуль, а интеграционное "
        "— связи между модулями.",
        "11. Интеграционное тестирование делают, когда модули собирают в "
        "одну программу.",
        "12. Модули собирают двумя способами: сразу все (монолитный) или по "
        "одному (инкрементальный, сверху вниз или снизу вверх).",
    ]
    for answer in answers:
        add_body(doc, answer)

    add_h1(doc, "5 Выводы")
    add_body(doc, "В работе сделан калькулятор на Python с кнопками. Все "
                  "операции сделаны отдельными функциями, поэтому каждую "
                  "можно проверить отдельно. На все функции написаны тесты, "
                  "все 23 теста проходят.")
    add_body(doc, "Тесты удобны тем, что если поменять код, можно быстро "
                  "проверить, что ничего не сломалось. Цель работы "
                  "выполнена.")

    add_h1(doc, "Список использованных источников")
    for source in (
        "1 Лутц М. Изучаем Python. – СПб.: Диалектика, 2019.",
        "2 unittest — Unit testing framework. – URL: "
        "https://docs.python.org/3/library/unittest.html (дата обращения: "
        "26.11.2026).",
        "3 tkinter — Python interface to Tcl/Tk. – URL: "
        "https://docs.python.org/3/library/tkinter.html (дата обращения: "
        "26.11.2026).",
    ):
        add_body(doc, source, align=WD_ALIGN_PARAGRAPH.LEFT)

    doc.core_properties.title = "Разработка модульных и интеграционных тестов"
    doc.core_properties.author = "Правиков Д. В., Корнилова Л. Д."
    os.makedirs(DOCS, exist_ok=True)
    doc.save(OUT)
    print(OUT)


if __name__ == "__main__":
    build_report()

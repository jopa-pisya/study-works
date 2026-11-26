"""Снимок окна программы для отчёта."""

import ctypes
import ctypes.wintypes
import os
import sys
import time

ctypes.windll.shcore.SetProcessDpiAwareness(1)

from PIL import ImageGrab  # noqa: E402

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

import main as app  # noqa: E402


def main():
    app.root.update()
    for action in (lambda: app.digit("1"), lambda: app.digit("2"),
                   lambda: app.operation("+"), lambda: app.digit("3"),
                   lambda: app.digit("0"), app.equals, lambda: app.memory("MS")):
        action()
    app.root.update()

    app.root.lift()
    app.root.attributes("-topmost", True)
    app.root.update()
    hwnd = ctypes.windll.user32.FindWindowW(None, "Калькулятор")
    ctypes.windll.user32.SetForegroundWindow(hwnd)
    for _ in range(30):
        app.root.update()
        time.sleep(0.05)

    rect = ctypes.wintypes.RECT()
    ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))
    image = ImageGrab.grab(
        bbox=(rect.left, rect.top, rect.right, rect.bottom), all_screens=True
    )
    width, height = image.size
    image = image.crop((12, 12, width - 14, height - 12))

    target = os.path.join(BASE, "docs", "calculator_window.png")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    image.save(target)
    app.root.destroy()
    print(target)


if __name__ == "__main__":
    main()

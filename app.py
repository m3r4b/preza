import streamlit as st
from reveal_slides import slides

# Настройка страницы Streamlit
st.set_page_config(page_title="Моя презентация", layout="wide")

# Читаем содержимое презентации из Markdown-файла
with open("slides.md", "r", encoding="utf-8") as f:
    slides_content = f.read()

# Отображаем слайды с конфигурацией Reveal.js
slides(
    content=slides_content,
    theme="moon",           # Тема презентации (можно менять)
    height=700,             # Высота окна слайдов
    config={
        "controls": True,       # Показывать стрелки управления
        "progress": True,       # Показывать индикатор прогресса
        "center": True,         # Центрировать содержимое
        "transition": "slide",  # Эффект перехода между слайдами
        "plugins": ["highlight"],  # Подключаем подсветку кода
        "pluginsConfig": {
            "highlight": {
                "theme": "vs"     # Тема подсветки кода (vs — светлая)
            }
        }
    }
)

# Добавляем кастомные стили для кода (можно менять под свой вкус)
st.markdown(
    """
    <style>
    /* Стиль для блоков кода */
    .reveal pre code {
        font-size: 1.2em;
        line-height: 1.5;
        background-color: #f5f5f5;
        padding: 16px 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        font-family: 'Fira Code', Consolas, 'Courier New', monospace;
        white-space: pre-wrap;
        transition: background-color 0.3s ease;
        color: #2d2d2d;
    }

    /* Эффект при наведении мыши */
    .reveal pre code:hover {
        background-color: #e0e0e0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

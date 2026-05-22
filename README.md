# SauceDemo UI Automation

**Первый проект** по автоматизации тестирования на Python.

UI Automation фреймворк для тестирования демо-приложения **SauceDemo** с использованием **Page Object Model (POM)**.

## О проекте

Реализован современный подход к автоматизации тестирования:
- Чистая архитектура **Page Object Model**
- Позитивные и негативные сценарии
- Параметризация тестов
- Allure-отчётность
- Explicit Waits

### Покрытые модули
- Авторизация (успешная + негативные кейсы)
- Работа с корзиной
- Оформление заказа (Checkout)
- Тестирование разных типов пользователей

## Технологический стек

- **Python** 3.11+
- **Selenium** 4.21+
- **Pytest** + pytest-xdist
- **Allure-pytest** — генерация красивых отчётов
- **Webdriver-manager**
- Page Object Model + BasePage

## Как запустить проект

### 1. Клонировать репозиторий
```bash
git clone https://github.com/winsend/saucedemo_automation.git
cd saucedemo_automation
```

### 2. Установить зависимости
```bash
pip install -r requirements.txt
```

### 3. Запуск тестов
```bash
# Обычный запуск
pytest

# Параллельный запуск
pytest -n auto

# Запуск с генерацией Allure отчёта
pytest --alluredir=allure-results -n auto
```
### 4. Просмотр Allure отчёта
```bash
allure serve allure-results
```

Структура проекта
```bash
saucedemo_automation/
├── pages/              # Page Object классы
├── tests/              # Тестовые сценарии
├── utils/              # Локаторы и вспомогательные функции
├── conftest.py         # Fixtures и настройки
├── requirements.txt
└── README.md
```
Автор: Влад Лизогуб
Статус: Учебный проект / Портфолио Junior AQA Engineer
# 📦 Onbon LED Controllers Data Repository

Структурированная база данных о контроллерах LED-дисплеев **Onbon**, собранная с официального сайта **onbon.ru**.

> **Компания:** Onbon — тот же вендор, что в [onbon-parser](https://github.com/valentinpo/onbon-parser) и [onbonbx-parser](https://github.com/valentinpo/onbonbx-parser).
> **Этот репозиторий** — ETL-хранилище и обработка собранных данных.

---

## 📋 Описание

Это **ETL-пайплайн** (Extract, Transform, Load) для сбора и обработки технической информации о контроллерах Onbon. Данные хранятся в формате **JSON** и готовы к использованию в веб-приложениях, каталогах или для аналитики.

## 🎯 Цели

- **Централизация** — объединение разрозненных JSON-файлов в единую базу данных
- **Стандартизация** — очистка данных от технических ошибок (пробелы в ключах, вложенность)
- **Автоматизация** — скрипты для создания структуры папок и расширения карточек товаров
- **Доступность** — данные в удобном машиночитаемом формате

---

## 📁 Структура репозитория

```
onbon-data-repo/
├── 📁 по категориям/           # Группировка JSON по категориям
│   ├── merged_fc.json
│   ├── merged_md.json
│   └── merged_vp.json
├── 📄 add_fields.py            # Добавление полей в карточки
├── 📄 controllers_list.txt     # Список всех контроллеров
├── 📄 create_folders.py        # Создание структуры папок
├── 📄 get_list.py              # Извлечение списка контроллеров
├── 📄 merge.py                 # Объединение JSON-файлов
├── 📄 merged.json              # Объединённый файл
├── 📄 merged_updated.json      # Финальный файл с добавленными полями
├── 📄 requirements.txt         # Зависимости
└── 📄 README.md                # Документация
```

---

## 🚀 Быстрый старт

### Требования

- Python 3.8+
- Стандартные библиотеки: `json`, `os`, `pathlib`

### Установка и запуск

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/valentinpo/Onbon-LED-Controllers-Data-Repository.git
cd Onbon-LED-Controllers-Data-Repository

# 2. Полный цикл обработки
python merge.py           # Шаг 1: Объединение файлов
python add_fields.py      # Шаг 2: Добавление полей
python get_list.py        # Шаг 3: Получение списка
python create_folders.py  # Шаг 4: Создание структуры
```

---

## 💾 Данные

- **`merged.json`** — объединённая база контроллеров
- **`merged_updated.json`** — финальный файл с добавленными полями
- **`по категориям/`** — данные, сгруппированные по категориям
- **`controllers_list.txt`** — полный список контроллеров

---

## 📫 Связанные репозитории

- [onbon-parser](https://github.com/valentinpo/onbon-parser) — парсер сайта **onbon.ru**
- [onbonbx-parser](https://github.com/valentinpo/onbonbx-parser) — парсер сайта **ru.onbonbx.com**
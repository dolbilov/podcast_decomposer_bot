# Podcast Decomposer Bot

> Telegram‑бот, который принимает **голосовые сообщения** (voice) и расшифровывает их в текст.  
> Документация описывает состояние ветки **`dev`** репозитория.

---

## TL;DR

1. Склонируйте репозиторий и переключитесь на `dev`.
2. Создайте файл `.env` и заполните обязательную переменную:
   * `TELEGRAM_BOT_TOKEN`
3. Установите зависимости из `requirements.txt`.
4. Запустите бота командой `python -m podcast_decomposer_bot`.

---

## Быстрый старт

```bash
git clone -b dev https://github.com/dolbilov/podcast_decomposer_bot.git
cd podcast_decomposer_bot

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

pip install -r requirements.txt    # или poetry install

cp .env.example .env               # впишите свои ключи
python -m podcast_decomposer_bot
```

### Docker

```bash
docker build -t podcast-decomposer:dev .
docker run --rm \
  -e TELEGRAM_BOT_TOKEN=... \
  -e OPENAI_API_KEY=... \
  podcast-decomposer:dev
```

---

## Что уже работает

| ✔ | Возможность |
|---|-------------|
| Голосовые в Telegram | Отправьте voice‑сообщение — бот вернёт расшифровку |

*(README перечисляет только функциональность, которая присутствует на текущий момент.)*

---

## Переменные окружения

| Переменная          | Обязательна | Назначение                         |
|---------------------|-------------|------------------------------------|
| `TELEGRAM_BOT_TOKEN`| ✅          | токен вашего Telegram‑бота         |

Пример конфигурации смотрите в файле `.env.example`.

---

## Тесты

```bash
pytest -q
```

---

## Лицензия

MIT © 2025 — [dolbilov](https://github.com/dolbilov)

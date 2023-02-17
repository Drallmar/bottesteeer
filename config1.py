from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    db_host: str       # URL-адрес базы данных
    db_user: str       # Username пользователя базы данных
    db_password: str   # Пароль к базе данных
    database: str      # Название базы данных


@dataclass
class TgBot:
    token: str             # Токен для доступа к телеграм-боту
    admin_ids: list[int]   # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig
Если создать экземпляр класса Config:

config = Config(tg_bot=TgBot(token=BOT_TOKEN,
                             admin_ids=ADMIN_IDS),
                db=DatabaseConfig(db_host=DB_HOST,
                                  db_user=DB_USER,
                                  db_password=DB_PASSWORD,
                                  database=DATABASE))
То, например, получить токен бота можно, будет так:

token = config.tg_bot.token
А пароль к базе данных так:

db_passw = config.db.db_password
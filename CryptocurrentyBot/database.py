import sqlite3
from config import config
from loguru import logger


class Database:
    def __init__(self) -> None:
        self.connect: sqlite3.Connection = sqlite3.connect(config.DATABASE)
        self.cursor: sqlite3.Cursor = self.connect.cursor()

    @logger.catch
    def get_lang(self, user_id: str) -> str:
        """ Получение из бд языка для пользователя """
        if self.check_user(user_id):
            self.cursor.execute("SELECT user_lang FROM users WHERE user_id = ?", (user_id,))
            return self.cursor.fetchone()[0]

    @logger.catch
    def set_lang(self, user_id: str, lang: str) -> None:
        """ Установка в бд языка для пользователя """
        if self.check_user(user_id):
            self.cursor.execute(f"UPDATE users SET user_lang ='{lang}' WHERE user_id='{user_id}'")
        else:
            self.cursor.execute(f"INSERT INTO users (user_id, user_lang) VALUES ('{user_id}', '{lang}')")

        logger.debug(f"Set lang is {lang} for {user_id}")

        self.connect.commit()

    def check_user(self, user_id) -> bool:
        """ Проверка на наличие пользователя в бд """
        self.cursor.execute("SELECT user_lang FROM users WHERE user_id = ?", (user_id,))

        if self.cursor.fetchone() is None:
            return False

        return True


def create_db() -> None:
    """ Функция для создания файла бд """
    connect: sqlite3.Connection = sqlite3.connect(config.DATABASE)
    cursor: sqlite3.Cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER NOT NULL, user_lang TEXT)")
    connect.commit()
    cursor.close()
    connect.close()


if __name__ == '__main__':
    create_db()

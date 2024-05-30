import sqlite3
from config import config
from loguru import logger


class Database:
    def __init__(self) -> None:
        self.connect: sqlite3.Connection = sqlite3.connect(config.TEST_DATABASE)
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

    def get_notify(self) -> list:
        """ Получение всех уведомлений пользователей"""
        self.cursor.execute("SELECT * FROM users")
        data: list = self.cursor.fetchall()
        logger.debug(data)
        return data

    def set_notify(self, user_id, coin, price) -> None:
        """ Установка уведомлений для пользователя """
        self.cursor.execute(f"INSERT INTO users (user_id, user_coin_notify, user_target_price_notify) VALUES ('{user_id}', '{coin}', '{price}')")
        self.connect.commit()

    def del_notify(self, user_id, coin, price) -> None:
        """ Установка уведомления """
        self.cursor.execute("DELETE FROM users WHERE user_id = ? AND user_coin_notify = ? AND user_target_price_notify = ?", (user_id, coin, price,))
        self.connect.commit()


@logger.catch
def create_db() -> None:
    """ Функция для создания файла бд """
    connect: sqlite3.Connection = sqlite3.connect(config.TEST_DATABASE)
    cursor: sqlite3.Cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER NOT NULL, user_lang TEXT, user_coin_notify TEXT, user_target_price_notify TEXT)")
    connect.commit()
    cursor.close()
    connect.close()


if __name__ == '__main__':
    create_db()

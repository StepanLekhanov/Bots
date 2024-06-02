from bot import bot


def main() -> None:
    bot.polling(none_stop=True, interval=0, timeout=0)


if __name__ == '__main__':
    main()

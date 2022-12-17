import os
from modules.color import cprint_upred, cprint_redtext, cprint_text, cprint_yellow, cprint_blue
import configparser
import pwinput

config = configparser.ConfigParser()
configpath = "configtelebot.conf"
def startup():
    """
    Функция запуска и первоначальной настройки программы
    """
    if os.path.exists(configpath):
        cprint_redtext("Бот запущен!")
        from bot import run
        run
    else:
        try:
            cprint_redtext("ПЕРВОНАЧАЛЬНАЯ НАСТРОЙКА ПРОГРАММЫ")
            cprint_redtext("+" * 34)
            cprint_text(
                """[!] Программа запущена впервый раз! 
[!] Необходимо произвести первоначальную настройку!
[!] Данное действие необходимо произвести только один раз, последующие включения будут проходить в 
    штатном режиме

[!] Для прекращения процесса первичной настройки, нажмите [CTRL] + [C]""")
            cprint_redtext("+" * 34)
            cprint_redtext("Настройка взаимодействия с Телеграм \n")
            config.add_section("TOKEN")
            add_token = pwinput.pwinput(prompt='[SET]Введите токен Binance в котором будет работать БОТ- ', mask='*')
            config.set("TOKEN", "BINANCE", add_token)
            except TypeError:
                cprint_redtext("ВВЕДЕН НЕКОРРЕКТНЫЙ ТОКЕН!!!")
            try:
                vk_session.auth(token_only=True)
            except vk_api.AuthError as error_msg:
                print(error_msg)
            set_token_vk = vk_session.token['access_token']
            config.set("TOKEN", "vk_user_token", set_token_vk)

            if os.path.isfile('vk_config.v2.json'):
                os.remove('vk_config.v2.json')
                cprint_redtext("[INFO] Временный файл удален!")
            else:
                cprint_redtext("[INFO] Временный файл не найден!")

            cprint_redtext("Настройка взаимодействия с базой данных")
            config.add_section("DATABASE")
            user_data = input("[SET] Введите имя пользователя базы данных- ")
            config.set("DATABASE", "db_user", user_data)
            password_data = pwinput.pwinput(prompt='[SET] Введите пароль пользователя базы данных- ', mask='*')
            config.set("DATABASE", "db_password", password_data)
            host_data = input("[SET] Введите хост базы данных- ")
            config.set("DATABASE", "db_host", host_data)

            try:
                conn = psycopg2.connect(
                    dbname="vkinder",
                    user=user_data,
                    host=host_data,
                    password=password_data,
                    port="5432",
                    connect_timeout=1)
                conn.close()

                with open(configpath, "w") as config_file:
                    config.write(config_file)

                cprint_text("[INFO] Соединение с базой настроено! Конфигурация записана!")
                cprint_text("[INFO] Начало установки модулей!")
                os.system("pip install -r requirements.txt")
                cprint_text("[FINISH] Настройка завершена! Перезапустите БОТ.")

            except psycopg2.OperationalError:
                cprint_redtext("[ERROR] БАЗА ДАННЫХ НЕДОСТУПНА!!!!")
                raise ValueError('oops!')

        except KeyboardInterrupt:
            cprint_upred("Выполнение настройки завершено по команде пользователя!")

        except ValueError:
            pass


if __name__ == '__main__':
    startup()
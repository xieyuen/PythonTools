from console import data, login

config: dict = {}


def init():
    global config
    config = data.load_config()


def main():
    init()
    while not login.login_status:
        login.main()
    # while True:
    #     pass


if __name__ == "__main__":
    main()

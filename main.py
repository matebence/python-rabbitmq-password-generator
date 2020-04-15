from classes.Generate import Generate


def main():
    config_password = Generate(password="qwerty").rabbitmq_password(encoding="utf-8", rand_salt_number=4)
    print(config_password)


if __name__ == "__main__":
    main()

from app.database.mongo import Mongo


def init() -> None:
    db = Mongo()


def main() -> None:
    init()


if __name__ == "__main__":
    main()

from three_tier import Application
from three_tier import Presentation
from three_tier import Database


def main():
    """
    The main function to initialize and run the three-tier application.

    It creates instances of Application, Presentation, and Database classes, establishes connections between them,
    and starts the main loop of the application.

    :return: None
    """
    app = Application()

    presentation = Presentation()
    presentation.application = app
    app.presentation = presentation

    db = Database()
    app.database = db

    app.run()


if __name__ == '__main__':
    main()

from three_tier import Application
from three_tier import Presentation
from three_tier import Database


def main():

    app = Application()

    presentation = Presentation()
    presentation.application = app
    app.presentation = presentation

    db = Database()
    app.database = db

    app.run()

if __name__ == '__main__':
    main()
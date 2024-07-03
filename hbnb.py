""" Another way to run the app"""
from dotenv import load_env
from src import create_app

load_env()

app = create_app()

if __name__ == "__main__":
    app.run()

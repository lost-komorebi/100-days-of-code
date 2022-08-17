from app import app
from views import home, add


if __name__ == "__main__":
    app.run(debug=True, port=5001)

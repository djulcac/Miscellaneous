from src import init_app

app = init_app(debug=True)

if __name__ == "__main__":
    print('run1',__name__)
    app.run()
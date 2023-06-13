from threading import Timer
import webbrowser
from findJobs import create_app

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

app = create_app()

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=True, use_reloader=False)
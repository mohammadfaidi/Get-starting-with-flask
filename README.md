# Get-starting-with-flask

pip install flask
python -m run 
python -m flask run (Windows),


    pip install flask

You now have a self-contained environment ready for writing Flask code. VS Code activates the environment automatically when you use Terminal: Create New Integrated Terminal. If you open a separate command prompt or terminal, activate the environment by running source env/bin/activate (Linux/macOS) or env\scripts\activate (Windows). You know the environment is activated when the command prompt shows (env) at the beginning.
Create and run a minimal Flask app#

    In VS Code, create a new file in your project folder named app.py using either File > New from the menu, pressing Ctrl+N, or using the new file icon in the Explorer View (shown below).

    Flask tutorial: new file icon in Explorer View

    In app.py, add code to import Flask and create an instance of the Flask object. If you type the code below (instead of using copy-paste), you can observe VS Code's IntelliSense and auto-completions:

    from flask import Flask
    app = Flask(__name__)

    Also in app.py, add a function that returns content, in this case a simple string, and use Flask's app.route decorator to map the URL route / to that function:

    @app.route("/")
    def home():
        return "Hello, Flask!"

        Tip: You can use multiple decorators on the same function, one per line, depending on how many different routes you want to map to the same function.

    Save the app.py file (Ctrl+S).

    In the terminal, run the app by entering python3 -m flask run (macOS/Linux) or python -m flask run (Windows), which runs the Flask development server. The development server looks for app.py by default. When you run Flask, you should see output similar to the following:

    (env) D:\py\\hello_flask>python -m flask run
     * Environment: production
       WARNING: Do not use the development server in a production environment.
       Use a production WSGI server instead.
     * Debug mode: off
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

    If you see an error that the Flask module cannot be found, make sure you've run pip3 install flask (macOS/Linux) or pip install flask (Windows) in your virtual environment as described at the end of the previous section.

    Also, if you want to run the development server on a different IP address or port, use the host and port command-line arguments, as with --host=0.0.0.0 --port=80.

    To open your default browser to the rendered page, Ctrl+click the http://127.0.0.1:5000/ URL in the terminal.

    Flask tutorial: the running app in a browser

    Observe that when you visit a URL like /, a message appears in the debug terminal showing the HTTP request:

    127.0.0.1 - - [11/Jul/2018 08:40:15] "GET / HTTP/1.1" 200 -

    Stop the app by using Ctrl+C in the terminal.

    Tip: If you want to use a different filename than app.py, such as program.py, define an environment variable named FLASK_APP and set its value to your chosen file. Flask's development server then uses the value of FLASK_APP instead of the default file app.py. For more information, see Flask command line interface.

Run the app in the debugger#

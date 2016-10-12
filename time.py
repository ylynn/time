from flask import Flask
app = Flask(__name__)

import time

@app.route("/")
def rtime():
        a = int(time.time())
	return str(a)

if __name__ == "__main__":
	app.run()

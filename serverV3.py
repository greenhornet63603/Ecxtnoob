import threading
from flask import Flask
from database import getserver


# -----------------------
#  Start your bot/server
# -----------------------
def start_bot():
    getserver.connect_v1()


# -----------------------
#  Dummy web server
# -----------------------
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running on Render!"


# -----------------------
#  Start both (bot + web)
# -----------------------
if __name__ == "__main__":
    threading.Thread(target=start_bot).start()
    app.run(host="0.0.0.0", port=10000)

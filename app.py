
from flask import Flask, request, jsonify, render_template
import threading
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pyautogui

app = Flask(__name__)

bot_thread = None
browser = None
@app.route("/")
def home():
    return render_template("index.html")

def start_bot(delay, speed):
    global browser
    browser = webdriver.Chrome()
    browser.get("https://humanbenchmark.com/tests/typing")

    time.sleep(delay - 2)

    page_source = browser.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    spans = soup.find_all('span', class_='incomplete')
    text_to_type = ''.join([span.get_text() for span in spans])

    time.sleep(2)

    pyautogui.write(text_to_type, interval=speed)

@app.route('/start', methods=['POST'])
def start():
    global bot_thread
    delay = int(request.json.get('delay', 0))
    speed = float(request.json.get('botSpeed', 0))
    bot_thread = threading.Thread(target=start_bot, args=(delay, speed))
    bot_thread.start()
    return jsonify({"status": f"Bot started with delay of {delay} seconds and speed {speed}."})

@app.route('/stop', methods=['POST'])
def stop():
    global browser
    if browser:
        browser.quit()
        browser = None
        return jsonify({"status": "Bot stopped."})
    return jsonify({"error": "Bot is not running."})

if __name__ == '__main__':
    app.run(debug=True)
# *-* coding: utf-8 *-*

from flask import Flask

import tasks
app = Flask(__name__)

@app.route('/images', methods=['GET', 'POST'])
def image():
    tasks.image.delay()
    return "image success"

@app.route('/video/', methods=['GET'])
def video():
    tasks.video.delay()
    return "video success"

@app.route('/common/', methods=['GET', 'POST'])
def common():
    tasks.common.delay()
    return "common success"

if __name__ == "__main__":
    app.run(debug=True)

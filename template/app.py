from flask import Flask, render_template, jsonify
import pygame
import random
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game')
def start_game():
    threading.Thread(target=game_loop).start()
    return jsonify({"status": "Game Started"})

if __name__ == "__main__":
    app.run(debug=True)

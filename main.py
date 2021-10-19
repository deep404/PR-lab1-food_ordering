import coloredlogs
import logging
import threading
from flask import Flask
from flask import request
from actors.OrderManager import OrderManager

logging.basicConfig(filename='food_ordering.log', level=logging.DEBUG, format='%(asctime)s:  %(message)s', datefmt="%m/%d/%Y %I:%M:%S %p")
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')

HOST = '0.0.0.0'
FO_PORT = 3000

app = Flask('Food-Ordering-Service')
manager = OrderManager()


@app.route('/register', methods=['POST'])
def register():
    restaurant = request.get_json()
    return manager.register(restaurant)


@app.route('/menu', methods=['GET'])
def get_menu():
    return manager.get_menu()


@app.route('/order', methods=['POST'])
def order():
    data = request.get_json()
    return manager.make_order(data)


@app.route('/rating', methods=['POST'])
def rating():
    data = request.get_json()
    return manager.rating(data)


def main():
    open("food_ordering.log", "w").close()

    threading.Thread(target=lambda: app.run(host=HOST, port=FO_PORT, debug=False, use_reloader=False, threaded=True), daemon=True).start()

    while True:
        pass


if __name__ == '__main__':
    main()
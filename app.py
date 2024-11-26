from flask import Flask
import logging

# Налаштування логування
logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

# Простий ендпоінт для перевірки стану
@app.route('/health', methods=['GET'])
def health_check():
    app.logger.info("Health check endpoint called")
    return {'status': 'OK'}, 200

# Ендпоінт для головної сторінки
@app.route('/')
def home():
    app.logger.info("Home page accessed")
    return '<h1>Welcome to the Flask App</h1>', 200

# Ігнорування favicon-запитів
@app.route('/favicon.ico')
def favicon():
    app.logger.info("Favicon requested")
    return '', 204  # Повертає порожню відповідь із HTTP-кодом 204

if __name__ == '__main__':
    # Запуск на іншому порту, якщо порт 5000 зайнятий
    port = 5001
    app.logger.info(f"Starting Flask app on port {port}")
    app.run(host='0.0.0.0', port=port)

from flask import Flask
import logging

app = Flask(__name__)
logger = logging.getLogger("Admin")

logging.basicConfig(
    filename="logs/app.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)


@app.route("/", methods=["GET"])
def index():
    return "Hello, World"


if __name__ == "__main__":
    logger.debug("--- Starting Flask Application ---")
    app.run(host="0.0.0.0", port=5000, debug=True)

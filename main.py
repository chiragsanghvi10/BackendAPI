import pandas as pd
from flask import Flask, jsonify, make_response, Response, json

from src.services.translation_data import output_10_pairs
from src.utils.loggers import get_logger

logger = get_logger("main.py")

app = Flask(__name__)

# Loading the clean dataset
df = pd.read_excel('data/CleanData.xlsx')

logger.info("THE CleanData.xlsx has been loaded on to the memory. Length of data = `{}`".format(len(df)))


@app.route("/api/v1/status", methods=["GET"])
def get_status():
    """
    Returns the status of the server if it's still running.
    """
    response = Response(json.dumps({'success': True}), mimetype='application/json')
    response.status_code = 200
    logger.info("THE STATUS IS : ` {}`".format(response))
    return response


@app.route("/api/v1/sentences/<int:page>", methods=["GET"])
def translation_pairs(page):
    """
    Returns the list of dictionaries if `page` number is within the dataset limit.
    """
    try:
        response = output_10_pairs(df, page)
        logger.info("10 TRANSLATIONS FROM : `{}` to `{}`".format((page * 10), ((page * 10) + 10)))
        return make_response(jsonify(response), 200)
    except Exception as e:
        logger.info("ERROR in function.\n" + str(e))
        return jsonify(success=False)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="7003", debug=True)

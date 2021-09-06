from flask import Flask, send_from_directory, abort
import os
application = Flask(__name__)


@application.route("/")
def hello():
    print(application.instance_path)
    return "one thousand and one"


BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))
NFT_DIR = os.path.join(BASE_DIR, 'app/static/client/nft')
application.config["NFT_FILES"] = NFT_DIR


@application.route("/nft/<path:file_name>")
def get_file(file_name):
    try:
        return send_from_directory(directory=application.config["NFT_FILES"], path=application.config["NFT_FILES"], filename=file_name, as_attachment=False)
    except FileNotFoundError:
        abort(404)



if __name__ == "__main__":

    application.run(host='0.0.0.0')
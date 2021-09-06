from flask import Flask, send_from_directory, abort, render_template
import os
application = Flask(__name__)


@application.route("/")
def hello():
    print(application.instance_path)
    return "one thousand and one"


BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))
NFT_DIR = os.path.join(BASE_DIR, 'app/static/client/nft')
application.config["NFT_FILES"] = NFT_DIR


@application.route("/nft/<path:path>")
def get_file(path):
    try:
        return send_from_directory(directory=application.config["NFT_FILES"], path=path, as_attachment=False)
    except FileNotFoundError:
        abort(404)


@application.route("/nft/")
def make_tree():
    files = os.listdir(NFT_DIR)
    print(files)
    return render_template('files.html', files=files)


if __name__ == "__main__":

    application.run(host='0.0.0.0')
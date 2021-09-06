from flask import Flask, send_from_directory, abort
application = Flask(__name__)


@application.route("/")
def hello():
    print(application.instance_path)
    return "one thousand"


#application.config["NFT_IMAGES"] =

@application.route("/nft/<path:file_name>")
def get_file(file_name):
    print(file_name)
    return "Thanks."


if __name__ == "__main__":
    application.run(host='0.0.0.0')
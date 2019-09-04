from flask import Flask,request
from apis.api import ApkPure
from gevent import monkey
import json
import requests
monkey.patch_all()
app = Flask(__name__)
api = ApkPure(return_as="dict")
@app.route('/query', methods=['GET'])
def query():
    if (request.method == "GET"):
        if request.values['search']:
            query = request.values['search'] or ''
            find = api._search(query)
            data = api._detail(find, 1)
            app_json = json.dumps(find)
            return app_json
@app.route('/appDetail', methods=['GET'])
def appDetail():
    if (request.method == "GET"):
        if request.values['url']:
            appQuery = request.values['url'] or ''
            details = api.detail_from_url(appQuery)
            app_json = json.dumps(details)
            return app_json
@app.route('/trending', methods=['GET'])
def trending():
    if (request.method == "GET"):
        apps = api._trending()
        app_json = json.dumps(apps)
        return app_json

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

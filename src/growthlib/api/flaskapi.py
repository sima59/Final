from datetime import datetime
from sqlalchemy import create_engine
from flask import Flask, jsonify, request
from growthlib.adapters.orm import start_mappers, metadata
from growthlib.domain import commands
from growthlib.api import views
from growthlib import bootstrap

app = Flask(__name__)
bus = bootstrap.bootstrap()


''' Add bar chart
labels = [
   'Name','Lname','url','Head', 'Weight', 'Hight', 'Age','gender'
   
]

values = [
   name,lname, head, weight, hight,
    age
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C"]

@app.route('/bar')
def bar():
    bar_labels=labels
    bar_values=values
    return render_template('bar_chart.html', title='Child Growth Chart', max=17000, labels=bar_labels, values=bar_values)

'''
@app.route('/')
def index(self):
    return f'Growth API'

@app.route('/add_Growth', methods=['POST'])
def add_Growth():
    # title, url, notes, date_added, date_edited
    name = request.json["Name"]
    Lname = request.json["LName"]
    head = request.json["head"]
    weight = request.json["weight"]
    hight = request.json["hight"]
    age = request.json["age"]
    gender = request.json["gender"]
    notes = request.json["notes"]
    date_added = request.json["date_added"]
    date_edited = request.json["date_edited"]

    cmd = commands.AddGrowthCommand(
            name, Lname,head,weight,hight,age,gender,notes, date_added, date_edited
    )
    bus.handle(cmd)
    return "OK", 201


@app.route("/Growth/<name>", methods=['GET'])
def get_Growth_by_name(self, name):
    result = views.Growth_view(name, bus.uow)
    if not result:
         return "not found", 404
    return jsonify(result), 200

def get_Growth_by_id(self, name):
    pass

def delete(self, Growth):
    pass

def update(self,Growth):
    pass

if __name__ == "__main__":
    app.run()
#put and delete http verbs
#working with api --json
from flask import Flask,jsonify,request

app=Flask(__name__)

#initial data
item=[
    {"id":1,"name":"item 1","description":"this is item1"},
    {"id":2,"name":"item 2","description":"this is item2"}
]
#home
@app.route('/')
def home ():
    return "welcome to app"
#retrive all item by get
@app.route("/item",methods=['GET'])
def get_item():
    return jsonify(item)

#retrive by a id
@app.route('/get_item/<it_id>',methods=['GET'])
def item(it_id):
    it=next((i for i in item if i["id"]==it_id),None)
    if it==None:
        return jsonify("error not found")
    return jsonify(it)

#post: create new task
@app.route("/new",methods=['GET','POST'])
def create():
    if not request.json or not 'name' in request.json:
        return jsonify("error not found")
    new_item={
        "id":item[-1]["id"]+1 if item else 1,
        "name":request.json['name'],
        "description":request.json['description']
    }
    item.append(new_item)
    return jsonify(new_item)

if __name__=='__main__':
    app.run(debug=True)
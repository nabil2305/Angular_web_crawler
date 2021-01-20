from flask import Flask,render_template,request,jsonify
from flask_cors import CORS
app=Flask(__name__)
CORS(app)

s_item=[
  {
  'name':'Nabil'
}
  ];


@app.route('/data',methods=['POST'])
def data():
  request_data=request.get_json()
  new_item={'name':request_data['name']}
  s_item.append(new_item)
  return jsonify(new_item)

@app.route('/')
def show():
  return jsonify(s_item)

app.run(debug=True)


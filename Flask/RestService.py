from flask import Flask, jsonify, request, json,render_template;
from flask_cors import CORS;
import re
import mechanicalsoup
import csv
app = Flask(__name__)
CORS(app)


item=[
  {
    
  }
]
sol=[]
allsol=[]



@app.route("/", methods=['GET'])
def index():
  return "Welcome to CodezUp";




@app.route('/starting',methods=['POST'])
def startPage():
  sol=[];
 # global sol
  request_data=request.get_json()
  new_item={'value':request_data['item']}
  item.append(new_item)
  sitem=new_item['value']
  import re
  import mechanicalsoup
  
  # Connect to Google
  browser = mechanicalsoup.StatefulBrowser()
  browser.open("https://www.google.com/")
  
  # Fill-in the form
  browser.select_form('form[action="/search"]')
  browser["q"] = sitem
  # Note: the button name is btnK in the content served to actual
  # browsers, but btnG for bots.
  browser.submit_selected(btnName="btnG")
  
  # Display links
  for link in browser.links():
    target = link.attrs['href']
    # Filter-out unrelated links and extract actual URL from Google's
    # click-tracking.
    if (target.startswith('/url?') and not
    target.startswith("/url?q=http://webcache.googleusercontent.com")):
      target = re.sub(r"^/url\?q=([^&]*)&.*", r"\1", target)
      sol.append(target)
      allsol.append(target)
      
  
  return jsonify(sol)


@app.route('/starting',methods=['GET'])
def fpage():
  return jsonify(item);

@app.route('/generate',methods=['GET'])
def file_creation():
  l=len(allsol)
  num=[]
  for i in range(1,l+1):
    num.append(i)
  d1=zip(num,allsol)
  d1=dict(d1)
  with open("sample.json", "w") as outfile: 
    json.dump(d1, outfile) 
  with open('sample_csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(allsol)
  return d1




def main():
  print('nabil')


if __name__ == '__main__':
  main();
  app.run(debug=True)

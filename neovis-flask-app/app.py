from flask import Flask,render_template,request
import socket
import base64

app = Flask(__name__)

@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', hostname=host_name, ip=host_ip)
    except:
        return render_template('error.html')
    
@app.route("/form")
def form():
    try:
        return render_template('neo4j_vis_form.html')
    except:
        return render_template('error.html')
           
@app.route("/visconfig", methods=['GET'])
def config_json():
    json = request.args.get('json', type = str)
    print(json)
    encodedJSON = str(base64.b64encode(json.encode("utf-8")),"utf-8")
    print(encodedJSON)
    try:
        return render_template('neo4j_vis.html', query=encodedJSON)
    except:
        return render_template('error.html')
        

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

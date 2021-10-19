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
    
@app.route("/tests")
def tests():
    try:
        return render_template('tests.html')
    except:
        return render_template('error.html')

@app.route("/editor")
def editor():
    try:
        return render_template('editor.html')
    except:
        return render_template('error.html')


@app.route("/form", methods=['GET'])
def form():
    #nslots = request.args.get('nslots', type = int)
    neo4j_server = request.args.get('neo4j_server', type=str)
    #print(nslots)
    try:
        return render_template('form.html', query=neo4j_server)
    except:
        return render_template('error.html')

@app.route("/form-gui")
def form_gui():
    try:
        return render_template('form-gui.html')
    except:
        return render_template('error.html')
        
           
@app.route("/visconfig", methods=['GET'])
def config_json():
    
    json = request.args.get('json', type = str)
    
    try:
        encodedJSON = str(base64.b64encode(json.encode("utf-8")),"utf-8")
    except AttributeError as error:
        encodedJSON = {}

    try:
        return render_template('vis.html', query=encodedJSON)
    except:
        return render_template('error.html')
        

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

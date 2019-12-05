from flask import Flask,render_template
import socket

app = Flask(__name__)

@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', hostname=host_name, ip=host_ip)
    except:
        return render_template('error.html')
    
@app.route("/cypher/<cypher>")
def init_cypher(cypher):
    try:
        return render_template('neo4j_vis.html', query=cypher)
    except:
        return render_template('error.html')
    
@app.route("/config/<config>")
def config_vis(config):
    try:
        return render_template('neo4j_vis.html', query=config)
    except:
        return render_template('error.html')
    
@app.route("/config2", methods=['GET'])
def config_vis2():
    query2 = request.args.get('config')
    try:
        return render_template('neo4j_vis.html', query=query2)
    except:
        return render_template('error.html')
        

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

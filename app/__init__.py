from flask import Flask, render_template, request, jsonify
import subprocess, logging

app = Flask(__name__)
DLNAP_LOCATION = '/opt/web-util/app/dlnap/dlnap/dlnap.py'

@app.route("/", methods=['GET'])
def home():
    

    return render_template('home.html',devices=get_devices())

@app.route("/play_on_devices", methods=['POST'])
def play_on_devices():
    #logging.error("***************" + str(request.get_json()))
    devices = request.get_json().get('device_ip_list')
    location = request.get_json().get('location')

    for device_ip in devices:
        process = subprocess.Popen(['python3', DLNAP_LOCATION,'--ip',device_ip,'--play',location], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
    
    return jsonify({'out':out.decode(),'err':err.decode()})

@app.route("/max_volume", methods=['POST'])
def max_volume():
    #logging.error("***************" + str(request.get_json()))
    devices = request.get_json().get('device_ip_list')
    #location = request.get_json().get('location')

    for device_ip in devices:
        process = subprocess.Popen(['python3', DLNAP_LOCATION,'--ip',device_ip,'--volume','100'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
    
    return jsonify({'out':out.decode(),'err':err.decode()})


def get_devices():
    devices = dict()
    #Yes, absolute path bad. Lazy solution, it works
    process = subprocess.Popen(['python3', DLNAP_LOCATION,'--list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    
    #logging.error('out: ' + out.decode())
    #logging.error('err: ' + err.decode())
    
    if not err:
        tmp = out.decode().replace("[a]",'').splitlines()[1:]
        for x in tmp:
            dev_str = x.split('@')
            devices[dev_str[0].strip()] = dev_str[1].strip()
            
    return devices
        

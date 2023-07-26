import psutil
from flask import Flask, render_template


app = Flask('__name__')

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    Message = none
    if(cpu_percent > 80 or memory_percent > 80):
        Message = f"High CPU or Memory Utilization detected. Please scale up!!!"
    return f"WARNING : {Message}"

if '__main__' == __name__:
    app.run(host='0.0.0.0',debug=True,port=5001)
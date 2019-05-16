from flask import Flask, render_template, redirect, url_for, request, send_from_directory
import matplotlib.pyplot as plt

app = Flask(__name__)

# home route
@app.route('/')
def home():
    return render_template('home.html')


# plotting and graphing route
@app.route('/sukses', methods=['POST'])
def sukses():
    # ambil valuenya dari html file
    x = request.form['xaxis']
    y = request.form['yaxis']

    xvalue = []
    yvalue = []

    # di split, trs di masukin ke dalem list masing"
    for i in x.split(','):
            xvalue.append(int(i))
    
    for i in y.split(','):
            yvalue.append(int(i))

    print(x)
    print(y)

    # creating the graph
    plt.figure('Your graph')
    plt.plot(xvalue,yvalue)
    plt.xlabel('X Value')
    plt.xticks(xvalue)
    plt.ylabel('Y Value')
    plt.yticks(yvalue)
    plt.grid(True)

    # buat save figure graphnya ke dalem folder 'storage'
    plt.savefig('storage/graph.png') 
    graphname = 'graph.png'
    return redirect(url_for('load', x = graphname))


# loading the graph route
@app.route('/load/<path:x>')
def load(x):
    return send_from_directory('storage', x)

if __name__ == '__main__':
    app.run(debug = True)
from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<int:idnum>', methods=['GET'])
def id(idnum):
	idnum = idnum
	print(idnum)
	param = "pokemon/" + str(idnum) + "/"
	print(param)
	URL = "https://pokeapi.co/api/v2/" + param
	r = requests.get(URL)
	print(str(r))
	data = r.json()
	idname = data['forms'][0]['name']
	print(str(idname))
	return render_template('id.html', value1=idnum, value2=idname)

@app.route('/pokemon/<idname>', methods=['GET'])
def name(idname):
	idname = idname
	print(idname)
	param = "pokemon/" + str(idname) + "/"
	print(param)
	URL = "https://pokeapi.co/api/v2/" + param
	r = requests.get(URL)
	print(str(r))
	data = r.json()
	idnum = data['id']
	print(str(idnum))
	capname = idname.capitalize()
	return render_template('name.html', value1=capname, value2=idnum)

if __name__ == '__main__':
    app.run()

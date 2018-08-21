from flask import Flask, request, render_template

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 20*1024	# 20 kB

def checkExt(fileName):
	return fileName.split('.')[1].lower() == 'jpeg'

@app.route('/', methods=['GET', 'POST'])
def solve():
	if request.method == 'GET':
		return render_template('home.html')
	elif request.method == 'POST':
		if 'file' not in request.files:
			return ''

if __name__ == '__main__':
	app.run(debug=True)
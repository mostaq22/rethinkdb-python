from flask import Flask, render_template, request, redirect, url_for, jsonify, Response
from .model import save, get_all
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        save(title=title, description=description)
        return jsonify({'status': 'success'})
    return render_template('index.html')

@app.route('/feeds')
def live_data():
	def live_stream():
		try:
			cursor = get_all()
			for document in cursor:
				print(document['new_val'])
				yield "data:" + str(document['new_val']).replace("'",'"') + "\n\n"

		except:
			pass

	return Response(response = live_stream(),status=200, mimetype= 'text/event-stream')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
	app.run(host="0.0.0.0",debug=True)
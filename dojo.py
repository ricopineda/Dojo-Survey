from flask import Flask, render_template, request, redirect                                        

app = Flask(__name__)                     
                                          
@app.route('/')

def index():
  return render_template("index.html") 

# @app.route('/results')

# def results():
#   return render_template("results.html") 

@app.route('/process', methods=['POST'])                           
                                        
def dojo():
	name = request.form["name"]
	location = request.form["location"]
	language = request.form["language"]
	print name
	return render_template('results.html', name=name, location=location, language=language)


@app.route('/', methods=['POST'])  

def go_back():

	return redirect('/')


app.run(debug=True)
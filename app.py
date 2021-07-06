from flask import Flask ,render_template , url_for,request,redirect
from googletrans import Translator

#Deployed Successfully on Heroku : https://translator-app-omkar.herokuapp.com/

#Instantiate the web app
app = Flask(__name__)

# A global list of all the languages availaible
options = ["English","Arabic", "Bangla", "Chinese", "Hindi", "Dutch", "Korean",
               "Japanese", "Marathi", "Malyalam", "Portugese", "Russian", "Spanish",
               "Tamil", "Telugu", "Urdu"]

# .route to route the html pages on the web  by default we go to http://localhost:5000  <-- port number (default)
@app.route('/',methods=['POST','GET'])  #Methods include all the requests that it supports
def my_form():
    # We can use an html template stored in the templates dierctory of the venv#
    """ Note : We have to pass all the variables used in the html file in render_template """
    return render_template('register.html',options = options , title = 'Translator')


@app.route('/translated',methods = ['POST','GET'])
def home():
    # request.form returns a dictionary with key as the name and value as the input
    translator = Translator()

    # Retrieving text data from input field of html
    text = request.form['text']
    # Retrieving data from the dropdown list menu of template
    source = request.form['src']
    destination = request.form['dest']

    translation = translator.translate(text , src= source , dest= destination).text
    pronounce = translator.translate(text , src= source , dest= destination).pronunciation

    return render_template('home.html',text = text , source = source , destination = destination
                           ,translation = translation,pronounce = pronounce,options = options)

# Means app will run only if called from __main__ module
if __name__ == '__main__':
    app.run(debug= True)
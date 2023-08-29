from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.rout("/identify/<pepperoni_param>/<pineapple_param>")
def identify(pepperoni_param, cheese_param, pineapple_param):
  pepperoni_param = int(pepperoni_param)
  cheese_param = int(cheese_param)
  pineapple_param = int(pineapple_param)

  result = identify_pizza(pepperoni_param, cheese_param, pineapple_param)  

  return result
  
app.run(host = '0.0.0.0', port = 5000)



def identify_pizza(pepperoni, cheese, pineapple):
  return 123
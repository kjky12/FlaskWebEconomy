
# Import Libraries
from app import app
from flask import jsonify

# Define route "/api".
@app.route('/DataApi')
def DataApi():
  # return in JSON format. (For API)
  return "Test DataApi!"
  #return jsonify({"message":"Hello from Flask!"})

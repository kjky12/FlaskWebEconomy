# Import Libraries
from app import app
import os

# If file is called directly called, then run the app on the PORT provided defined in ENV or use '6969'.
if __name__ == "__main__":
    try :
        if 'liveconsole' not in gethostname():
            print("Web Hosting Start")
            app.run(debug=True)
    except Exception as e :
        print("Local Start")
        app.run(debug=True,
         host='0.0.0.0',
         port=9000,
         threaded=True)

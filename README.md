# pedramoura-app-backend

## Requirements
### Python modules
* ``flask``, ``flask_cors``, ``flask_restful``: framework for running a HTTP web service and ``firebase_admin``: framework to auth users with Firebase
```bash
pip install flask flask_restful flask_cors
```
### Firebase Credentials

Replace the path ```credentials/firebase-credentials.json``` with the actual path to your Firebase service credentials.

### Cloning the repository
```bash
git clone https://github.com/marcelozilio/pedramoura-delivery-route
```

## Usage
### Running web service
```bash
cd pedramoura-app-backend
python main.py
```
The output must show the IP address:
```console
 * Serving Flask app 'main'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```
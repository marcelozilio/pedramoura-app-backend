# pedramoura-app-backend

## Requirements
### Python modules
* ``flask``, ``flask_sqlalchemy``, ``flask_cors``: framework for running a HTTP web service
* ``firebase_admin``: framework to auth users with Firebase
```bash
pip install flask flask_sqlalchemy flask_cors firebase_admin
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
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 816-201-332


```
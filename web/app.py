import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def mainmenu():

    return """
    <html>
    <body>
    <center><h1>Hello World! from AWS CodeDeploy.</h1><br/>
    <h2>Piper, CI/CD Lab11-3</h2>
    <iframe src="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=Asia%2FTokyo&src=eW91bW15d2lmZUBnbWFpbC5jb20&src=ZjllZjBjNDlmYWMzMDYxN2NjNjNiZTBhMTM4NzgxOTAwNjI5OGM3NDdmMzUwY2EwNjUwZGZkNTIyNzlkNWVhNkBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&src=amEuamFwYW5lc2UjaG9saWRheUBncm91cC52LmNhbGVuZGFyLmdvb2dsZS5jb20&src=YWRkcmVzc2Jvb2sjY29udGFjdHNAZ3JvdXAudi5jYWxlbmRhci5nb29nbGUuY29t&color=%23039BE5&color=%239E69AF&color=%230B8043&color=%2333B679" style="border:solid 1px #777" width="800" height="600" frameborder="0" scrolling="no"></iframe>
    </body>
    </html>"""

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=80)

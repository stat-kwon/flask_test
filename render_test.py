from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/hello/<user>")
def hello_name(user):
    return render_template('render_template.html',
                           name1 = user,
                           name2 = "변수2")

if __name__ == "__main__":
    app.run(host="localhost", port="8080")
    
    
    
'''

정적 HTML 로드 할때 쓰는 render_template 방법
또한 변수를 할당해줄 수 있음

'''
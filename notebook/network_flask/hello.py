from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index(name=None):
	return render_template("index.html", name=name)

@app.route('/about')
def about(name=None):
	return render_template("about.html", name=name)



# 터미널에서 실행시키고, 인터넷에서 접속! localhost:5000
# 경로는 라우팅, 그리는건 랜더링
# html 파일은 templates 폴더 내부에 넣어놔야 적용가능!

if __name__ == '__main__':
	app.run(host='0.0.0.0')

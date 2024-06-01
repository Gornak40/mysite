from config import config
from flask import Flask, render_template, redirect


app = Flask(__name__)


@app.route('/')
def index():
	return redirect('/cli-tools')


@app.route('/cli-tools')
def cli_tool():
	return render_template('cli_tools.html', title='CLI Tools', config=config)


@app.route('/crosspawn')
def crosspawn():
	return render_template('crosspawn.html', title='CrossPawn', config=config)


@app.route('/tinkoff')
def tinkoff():
	return redirect('https://algocourses.ru')


@app.route('/contact')
def contact():
	return redirect('mailto:s-kozelsk@yandex.ru')


@app.errorhandler(404)
def not_found(e):
	return redirect('https://www.youtube.com/watch?v=__cqdc-dxWg')


if __name__ == '__main__':
	app.run(debug=True)

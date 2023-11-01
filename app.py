from config import config
from flask import Flask, render_template, redirect


app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html', title='Home', config=config)


@app.route('/cli-tools')
def cli_tool():
	return render_template('cli_tools.html', title='CLI Tools', config=config)


@app.route('/tinkoff')
def tinkoff():
	return redirect('https://algocourses.ru')


@app.route('/contact')
def contact():
	return redirect('mailto:s-kozelsk@yandex.ru')


if __name__ == '__main__':
	app.run(debug=True)
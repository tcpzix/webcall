from flask import Flask , render_template, Response, request, redirect, url_for, flash
from asterisk.ami import AMIClient, SimpleAction

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('home.html')

@app.route("/call/", methods=['POST'])
def call():

	call_message = "call in progress"
	client = AMIClient(address='172.16.1.254', port=5038)
	client.login(username='click2dial', secret='9787474')
	action = SimpleAction(
		'Originate',
		Channel='DAHDI/i1/09385255833',
		Exten='698',
		Priority=1,
		Context='from-internal',
		CallerID="Channel",
		)
	client.send_action(action)
	
	client.logoff()


	flash("success call",'success')
	return render_template('home.html', message=call_message)


if __name__ == '__main__':
	app.secret_key = 'snVbjqFMz7HpeMXuY4sTXVJVgpY9Dd'
	app.run(debug=True)

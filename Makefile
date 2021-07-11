run:
	source ./venv/bin/activate
	python main.py

start_nginx:
	sudo nginx -c $(pwd)/nginx.conf -s reload
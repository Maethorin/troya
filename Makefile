run:
	@python app/server.py --port 8000 --bind 0.0.0.0 -vvv --debug

mail:
	@python app/server.py --port 8001 --bind 0.0.0.0 -vvv --debug

run:
	python run.py
install:
	pip install -r requirements.txt

run-redis:
	@redis-server &

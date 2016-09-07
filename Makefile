virtualenv:
	virtualenv .virtualenv
	. ./.virtualenv/bin/activate && pip install -r requirements.pip

clean:
	rm -rf .virtualenv

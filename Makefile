STATIC = etrack/static
SCSS = etrack/assets/scss
APP_LIST ?= assessment course misc moderation qualification

.PHONY: collectstatics compile-scss compile-scss-debug watch-scss run install test

collectstatics: compile-scss
	./manage.py collectstatic --noinput

compile-scss:
	sassc -s compressed -I etrack/assets/components/bootstrap-sass/assets/stylesheets $(SCSS)/app.scss $(STATIC)/css/app.css

compile-scss-debug:
	sassc --sourcemap -I etrack/assets/components/bootstrap-sass/assets/stylesheets $(SCSS)/app.scss $(STATIC)/css/app.css

watch-scss:
	watchmedo shell-command --patterns=*.scss --recursive --command="make compile-scss-debug" $(SCSS)

run:
	python manage.py runserver 0.0.0.0:8000

install:
	pip install -r requirements/dev.txt
	npm install

migrations-check:
	python manage.py makemigrations --check --dry-run

test: migrations-check
	@coverage run --source=. manage.py test $(APP_LIST)


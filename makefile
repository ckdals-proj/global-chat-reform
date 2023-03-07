check-pre-p:
	cd ./tests & pytest --cache-clear -vv --color=yes
	rm -r .pytest_cache
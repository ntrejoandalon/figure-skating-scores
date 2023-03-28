default:

.PHONY: reproduce clear data data/tidy data/json

reproduce: clear data

clear: 
	rm -r makdata
	mkdir -p data/tidy data/json

data: data/json data/tidy

data/json:
	python310 -m scripts.parse_pdfs pdfs 2>&1 | tee data/parsing-log.txt

data/tidy:
	python310 -m scripts.tidify_results

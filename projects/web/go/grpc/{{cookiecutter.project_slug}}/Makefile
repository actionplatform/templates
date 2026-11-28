BUF = docker run --rm -v "$(CURDIR):/w" -w /w bufbuild/buf:1.50.0

.PHONY: generate lint-proto

generate:
	$(BUF) generate

lint-proto:
	$(BUF) lint

run:
	gcc -E main.c | grep -v '^#' | clang-format
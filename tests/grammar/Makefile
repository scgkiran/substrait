ANTLR_JAR=antlr-4.13.2-complete.jar
GRAMMARS=TestFileLexer.g4 TestFileParser.g4
OUTPUT_DIR=../coverage/antlr_generated

generate:
	java -jar $(ANTLR_JAR) -visitor -Dlanguage=Python3 -o $(OUTPUT_DIR) $(GRAMMARS)

clean:
	rm -rf $(OUTPUT_DIR)/*.py

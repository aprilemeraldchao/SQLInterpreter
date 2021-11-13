# SQLInterpreter

## Set Up ANTLR
1. Download Antlr
    ```
    cd /usr/local/lib
    curl -O https://www.antlr.org/download/antlr-4.9-complete.jar
    ```
2. Configure your ``bash_profile``.
   1. Navigate to your home directory: 
        ```
        cd ~/
        ```
   2. Create a ``bash_profile`` if one doesn't already exist:
        ```
        touch bash_profile
        ```
   3. Add the following lines to the file:
        ```
        export CLASSPATH=".:/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH"
        alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
        alias grun='java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig'
        ```
## Testing the Grammar
1. Generate the default ANTLR files: 
    ```
    antlr4 SQLGrammar.g4
    ```
2. Compile the generated files: 
    ```
    javac SQLGrammar*.java
    ```
1. Start the tester: 
    ```
    grun SQLGrammar statements
    ```
   1. Add ``-tokens`` to see how each word is being interpreted by the Grammar.
   2. Add ``-tokens -gui`` to see tokens in a GUI.
1. Enter some test cases.
    ```
    CREATE TABLE table_1 (col_1 string, col_2 int);
    DROP TABLE table_1;
    SHOW TABLES;
    SELECT col_1, col_2 FROM table_1;
    SELECT * FROM table_1;
    SELECT col_1, col_2 FROM table_1 WHERE col_1 = 123;
    INSERT INTO table_1 VALUES (123,'abc');
    ```
5. To close the tester, press ``control+D``.

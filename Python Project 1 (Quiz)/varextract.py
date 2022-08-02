from operator import sub


questions=[
    "What is a correct syntax to output \"Hello World\" in Python?",
    "How do you insert COMMENTS in Python code?",
    "Which one is NOT a legal variable name?",
    "How do you create a variable with the numeric value 5?",
    "What is the correct file extension for Python files?",
    "How do you create a variable with the floating number 2.8?",
    "What is the correct syntax to output the type of a variable or object in Python?",
    "What is the correct way to create a function in Python?",
    "In Python, 'Hello', is the same as \"Hello\"",
    "What is a correct syntax to return the first character in a string?",
    "Which method can be used to remove any whitespace from both the beginning and the end of a string?",
    "Which method can be used to return a string in upper case letters?",
    "Which method can be used to replace parts of a string?",
    "Which operator is used to multiply numbers?",
    "Which operator can be used to compare two values?",
    "Which of these collections defines a LIST?",
    "Which of these collections defines a TUPLE?",
    "Which of these collections defines a SET?",
    "Which of these collections defines a DICTIONARY?",
    "Which collection is ordered, changeable, and allows duplicate members?",
    "Which collection does not allow duplicate members?",
    "How do you start writing an if statement in Python?",
    "How do you start writing a while loop in Python?",
    "How do you start writing a for loop in Python?",
    "Which statement is used to stop a loop?"
]
response = ["0"] * len(questions)
answers =[
    [ "print(\"Hello World\")", "echo \"Hello World\"", "echo(\"Hello World\");", "p(\"Hello World\")" ],
    [ "//This is a comment", "/*This is a comment*/", "#This is a comment" ],
    [ "my-var", "_myvar", "my_var", "Myvar" ],
    [ "Both the other answers are correct", "x = int(5)", "x = 5" ],
    [ ".py", ".pt", ".pyt", ".pyth" ],
    [ "Both the other answers are correct","x = 2.8", "x = float(2.8)" ],
    [ "print(typeof(x))", "print(type(x))","print(typeof x)", "print(typeOf(x))"],
    [ "def myFunction():", "create myFunction():", "function myFunction():" ],
    [ "True", "False" ],
    [ "x = \"Hello\"[0]", "x = \"Hello\".sub(0, 1)", "x = sub(\"Hello\", 0, 1)" ],
    [ "trim()", "len()", "ptrim()", "strip()" ],
    [ "upper()", "uppercase()", "upperCase()", "toUpperCase()" ],
    [ "replace()", "switch()", "repl()", "replaceString()" ],
    [ "*", "#", "x", "%" ],
    [ "=", "><", "<>", "==" ],
    [ "[\"apple\", \"banana\", \"cherry\"] ", "{\"apple\", \"banana\", \"cherry\"}", "{\"name\": \"apple\", \"color\": \"green\"}", "(\"apple\", \"banana\", \"cherry\")" ],
    [ "(\"apple\", \"banana\", \"cherry\")", "[\"apple\", \"banana\", \"cherry\"]", "{\"name\": \"apple\", \"color\": \"green\"}", "{\"apple\", \"banana\", \"cherry\"}" ],
    [ "{\"apple\", \"banana\", \"cherry\"}", "(\"apple\", \"banana\", \"cherry\")", "[\"apple\", \"banana\", \"cherry\"]", "{\"name\": \"apple\", \"color\": \"green\"}" ],
    [ "{\"name\": \"apple\", \"color\": \"green\"} ", "[\"apple\", \"banana\", \"cherry\"]", "{\"apple\", \"banana\", \"cherry\"}", "(\"apple\", \"banana\", \"cherry\")" ],
    [ "LIST", "SET", "DICTIONARY", "TUPLE" ],
    [ "SET", "LIST", "TUPLE" ],
    [ "if x > y:", "if (x > y)", "if x > x then:" ],
    [ "while x > y:", "while x > y {", "x > y while {", "while (x > y)" ],
    [ "for x in y:", "for x > y:", "for each x in x:" ],
    [ "break", "return", "exit", "stop" ]
]
correctanwsers = [ "a","c","a","a","a","a","b","a","a","a","d","a","a","a","d","a","a","a","a","a","a","a","a","a","a" ]
anwserblock = ["A: ","B: ", "C: ", "D: "]
# StudyLensAI Retrieval Evaluation

## Experiment Information

- Timestamp: 2026-08-27_17-58-05
- Vector database: Chroma
- Embedding model: sentence-transformers/all-MiniLM-L6-v2
- Vector retriever: Chroma similarity search
- Hybrid retriever: Vector search + BM25 + Reciprocal Rank Fusion
- Final results per query: top 5
- Candidate retrieval count: 10

# Test 1: Exact technical terminology

**Category:** Exact terminology

**Query:**
> What is polymorphism?

**User ID:** user_A

**Expected Topic:** Python polymorphism

---

## Vector Retrieval Results

### Rank 1

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 185

**Content:**

> 17.9. Polymorphism 163
> >>> print 1337 + start
> 10:07:17
> Exercise 17.5. Write an add method for Points that works with either a Point object or a tuple:
> • If the second operand is a Point, the method should return a new Point whose x coordinate is
> the sum of the x coordinates of the operands, and likewise for the y coordinates.
> • If the second operand is a tuple, the method should add the ﬁrst element of the tuple to the x
> coordinate and the second element to the y coordinate, and return a new Poi

### Rank 2

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 196

**Content:**

> 174 Chapter 18. Inheritance
> Hand
> Deck * Card
> Figure 18.2: Class diagram.
> There are several kinds of relationship between classes:
> • Objects in one class might contain references to objects in another class. For example,
> each Rectangle contains a reference to a Point, and each Deck contains references to
> many Cards. This kind of relationship is called HAS-A, as in, “a Rectangle has a
> Point.”
> • One class might inherit from another. This relationship is called IS-A, as in, “a Hand
> is a kind of a De

### Rank 3

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 194

**Content:**

> 172 Chapter 18. Inheritance
> In this case we are deﬁning a “thin” method that expresses a list operation in terms that are
> appropriate for decks.
> As another example, we can write a Deck method named shuffle using the function
> shuffle from the random module:
> # inside class Deck:
> def shuffle(self):
> random.shuffle(self.cards)
> Don’t forget to importrandom .
> Exercise 18.2. Write a Deck method named sort that uses the list method sort to sort the cards
> in a Deck . sort uses the __cmp__ method we deﬁned

### Rank 4

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 171

**Content:**

> 15.8. Glossary 149
> The ﬁrst argument can be any object; the second argument is astring that contains the name
> of the attribute.
> 15.8 Glossary
> class: A user-deﬁned type. A class deﬁnition creates a new class object.
> class object: An object that contains information about a user-deﬁned type. The class ob-
> ject can be used to create instances of the type.
> instance: An object that belongs to a class.
> attribute: One of the named values associated with an object.
> embedded (object): An object that is s

### Rank 5

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 239

**Content:**

> C.5. Class Diagrams 217
> object Deck
> __init__
> __str__
> add_card
> move_cards
> pop_card
> remove_card
> shuffle
> sort
> cards
> Hand
> __init__
> PokerHand
> has_flush
> suit_hist
> cards
> label
> Card
> __cmp__
> __init__
> __str__
> rank_names
> suit_names
> rank
> suit
> Figure C.8: Class diagram.
> Class diagrams are different. They show the classes that make up a program and the re-
> lationships between them. They are timeless in the sense that they describe the program
> as a whole, not any particular point in time. For example, if an in


---

## Hybrid Retrieval Results

### Rank 1

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 185

**Content:**

> 17.9. Polymorphism 163
> >>> print 1337 + start
> 10:07:17
> Exercise 17.5. Write an add method for Points that works with either a Point object or a tuple:
> • If the second operand is a Point, the method should return a new Point whose x coordinate is
> the sum of the x coordinates of the operands, and likewise for the y coordinates.
> • If the second operand is a tuple, the method should add the ﬁrst element of the tuple to the x
> coordinate and the second element to the y coordinate, and return a new Poi

### Rank 2

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 196

**Content:**

> 174 Chapter 18. Inheritance
> Hand
> Deck * Card
> Figure 18.2: Class diagram.
> There are several kinds of relationship between classes:
> • Objects in one class might contain references to objects in another class. For example,
> each Rectangle contains a reference to a Point, and each Deck contains references to
> many Cards. This kind of relationship is called HAS-A, as in, “a Rectangle has a
> Point.”
> • One class might inherit from another. This relationship is called IS-A, as in, “a Hand
> is a kind of a De

### Rank 3

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 20

**Content:**

> xx Contents
> 17 Classes and methods 157
> 17.1 Object-oriented features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
> 17.2 Printing objects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158
> 17.3 Another example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
> 17.4 A more complicated example . . . . . . . . . . . . . . . . . . . . . . . . . . 160
> 17.5 The init method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160
> 17.

### Rank 4

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 194

**Content:**

> 172 Chapter 18. Inheritance
> In this case we are deﬁning a “thin” method that expresses a list operation in terms that are
> appropriate for decks.
> As another example, we can write a Deck method named shuffle using the function
> shuffle from the random module:
> # inside class Deck:
> def shuffle(self):
> random.shuffle(self.cards)
> Don’t forget to importrandom .
> Exercise 18.2. Write a Deck method named sort that uses the list method sort to sort the cards
> in a Deck . sort uses the __cmp__ method we deﬁned

### Rank 5

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 227

**Content:**

> B.3. Analysis of search algorithms 205
> • The run time of update is proportional to the size of the dictionary passed as a pa-
> rameter, not the dictionary being updated.
> • keys , values and items are linear because they return new lists; iterkeys ,
> itervalues and iteritems are constant time because they return iterators. But if
> you loop through the iterators, the loop will be linear. Using the “iter” functions
> saves some overhead, but it doesn’t change the order of growth unless the number of
> ite


---

# Test 2: Acronym or keyword

**Category:** Acronym / keyword

**Query:**
> What is an API?

**User ID:** user_B

**Expected Topic:** API terminology

---

## Vector Retrieval Results

### Rank 1

- Filename: Python.pdf
- Document ID: fc38bfb7-e987-444c-b769-7718c5060cfc
- Page: 30

**Content:**

> 8 Chapter 1. The way of the program
> source code: A program in a high-level language before being compiled.
> object code: The output of the compiler after it translates the program.
> executable: Another name for object code that is ready to be executed.
> prompt: Characters displayed by the interpreter to indicate that it is ready to take input
> from the user.
> script: A program stored in a ﬁle (usually one that will be interpreted).
> interactive mode: A way of using the Python interpreter by typing com

### Rank 2

- Filename: Python.pdf
- Document ID: fc38bfb7-e987-444c-b769-7718c5060cfc
- Page: 25

**Content:**

> 1.2. What is a program? 3
> 1.2 What is a program?
> A program is a sequence of instructions that speciﬁes how to perform a computation. The
> computation might be something mathematical, such as solving a system of equations or
> ﬁnding the roots of a polynomial, but it can also be a symbolic computation, such as search-
> ing and replacing text in a document or (strangely enough) compiling a program.
> The details look different in different languages, but a few basic instructions appear in just
> about eve

### Rank 3

- Filename: Python.pdf
- Document ID: fc38bfb7-e987-444c-b769-7718c5060cfc
- Page: 179

**Content:**

> Chapter 17
> Classes and methods
> Code examples from this chapter are available from http://thinkpython.com/code/
> Time2.py .
> 17.1 Object-oriented features
> Python is an object-oriented programming language , which means that it provides fea-
> tures that support object-oriented programming.
> It is not easy to deﬁne object-oriented programming, but we have already seen some of its
> characteristics:
> • Programs are made up of object deﬁnitions and function deﬁnitions, and most of the
> computation is express

### Rank 4

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 39

**Content:**

> Explore Flask Documentation, Release 1.0
> static_folder='static'
> )
> import .views
> Next we can register this blueprint in the U2FtIEJsYWNr package’s top-level__init__.py ﬁle.
> # U2FtIEJsYWNr/__init__.py
> from flask import Flask
> from .api import api
> app = Flask(__name__)
> # Puts the API blueprint on api.U2FtIEJsYWNr.com.
> app.register_blueprint(api, subdomain='api')
> Make sure that the routes are registered on the blueprint now rather than the app object.
> # U2FtIEJsYWNr/views.py
> from . import app
> @app.ro

### Rank 5

- Filename: Python.pdf
- Document ID: fc38bfb7-e987-444c-b769-7718c5060cfc
- Page: 24

**Content:**

> 2 Chapter 1. The way of the program
> SOURCE
> CODE
> INTERPRETER OUTPUT
> Figure 1.1: An interpreter processes the program a little at a time, alternately reading lines
> and performing computations.
> CODE
> OBJECT EXECUTOR
> CODE
> SOURCE COMPILER OUTPUT
> Figure 1.2: A compiler translates source code into object code, which is run by a hardware
> executor.
> Due to these advantages, almost all programs are written in high-level languages. Low-
> level languages are used only for a few specialized applications.
> Two ki


---

## Hybrid Retrieval Results

### Rank 1

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 39

**Content:**

> Explore Flask Documentation, Release 1.0
> static_folder='static'
> )
> import .views
> Next we can register this blueprint in the U2FtIEJsYWNr package’s top-level__init__.py ﬁle.
> # U2FtIEJsYWNr/__init__.py
> from flask import Flask
> from .api import api
> app = Flask(__name__)
> # Puts the API blueprint on api.U2FtIEJsYWNr.com.
> app.register_blueprint(api, subdomain='api')
> Make sure that the routes are registered on the blueprint now rather than the app object.
> # U2FtIEJsYWNr/views.py
> from . import app
> @app.ro

### Rank 2

- Filename: Python.pdf
- Document ID: fc38bfb7-e987-444c-b769-7718c5060cfc
- Page: 30

**Content:**

> 8 Chapter 1. The way of the program
> source code: A program in a high-level language before being compiled.
> object code: The output of the compiler after it translates the program.
> executable: Another name for object code that is ready to be executed.
> prompt: Characters displayed by the interpreter to indicate that it is ready to take input
> from the user.
> script: A program stored in a ﬁle (usually one that will be interpreted).
> interactive mode: A way of using the Python interpreter by typing com

### Rank 3

- Filename: Python.pdf
- Document ID: fc38bfb7-e987-444c-b769-7718c5060cfc
- Page: 25

**Content:**

> 1.2. What is a program? 3
> 1.2 What is a program?
> A program is a sequence of instructions that speciﬁes how to perform a computation. The
> computation might be something mathematical, such as solving a system of equations or
> ﬁnding the roots of a polynomial, but it can also be a symbolic computation, such as search-
> ing and replacing text in a document or (strangely enough) compiling a program.
> The details look different in different languages, but a few basic instructions appear in just
> about eve

### Rank 4

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 38

**Content:**

> Explore Flask Documentation, Release 1.0
> config.txt
> requirements.txt
> run.py
> U2FtIEJsYWNr/
> __init__.py
> home/
> views.py
> static/
> templates/
> dash/
> views.py
> static/
> templates/
> admin/
> views.py
> static/
> templates/
> api/
> views.py
> static/
> templates/
> blog/
> views.py
> static/
> templates/
> models.py
> tests/
> Step 3: Cut the crap
> Now we can go into each blueprint and remove the views, static ﬁles and templates that don’t apply to that blueprint.
> How you go about this step largely depends on how your app was organized

### Rank 5

- Filename: Python.pdf
- Document ID: fc38bfb7-e987-444c-b769-7718c5060cfc
- Page: 179

**Content:**

> Chapter 17
> Classes and methods
> Code examples from this chapter are available from http://thinkpython.com/code/
> Time2.py .
> 17.1 Object-oriented features
> Python is an object-oriented programming language , which means that it provides fea-
> tures that support object-oriented programming.
> It is not easy to deﬁne object-oriented programming, but we have already seen some of its
> characteristics:
> • Programs are made up of object deﬁnitions and function deﬁnitions, and most of the
> computation is express


---

# Test 3: Natural language question

**Category:** Paraphrased question

**Query:**
> How does Python organize reusable code?

**User ID:** user_A

**Expected Topic:** Python concepts

---

## Vector Retrieval Results

### Rank 1

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 162

**Content:**

> 140 Chapter 14. Files
> If you run this program, it reads itself and prints the number of lines in the ﬁle, which is 7.
> You can also import it like this:
> >>> import wc
> 7
> Now you have a module object wc :
> >>> print wc
> <module ' wc ' from ' wc.py ' >
> That provides a function called linecount :
> >>> wc.linecount( ' wc.py ' )
> 7
> So that’s how you write modules in Python.
> The only problem with this example is that when you import the module it executes the
> test code at the bottom. Normally when you impor

### Rank 2

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 130

**Content:**

> 108 Chapter 11. Dictionaries
> 11.6 Global variables
> In the previous example, known is created outside the function, so it belongs to the special
> frame called __main__ . Variables in __main__ are sometimes called global because they
> can be accessed from any function. Unlike local variables, which disappear when their
> function ends, global variables persist from one function call to the next.
> It is common to use global variables forﬂags; that is, boolean variables that indicate (“ﬂag”)
> whether a co

### Rank 3

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 207

**Content:**

> 19.7. Menus and Callables 185
> endrow ends this row of widgets, so subsequent widgets are packed in the column Frame.
> Gui.py keeps a stack of Frames:
> • When you use row , col or gr to create a Frame, it goes on top of the stack and becomes
> the current Frame.
> • When you use endrow , endcol or endgr to close a Frame, it gets popped off the stack
> and the previous Frame on the stack becomes the current Frame.
> The method run_file reads the contents of the Entry, uses it as a ﬁlename, reads the con-
> te

### Rank 4

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 179

**Content:**

> Chapter 17
> Classes and methods
> Code examples from this chapter are available from http://thinkpython.com/code/
> Time2.py .
> 17.1 Object-oriented features
> Python is an object-oriented programming language , which means that it provides fea-
> tures that support object-oriented programming.
> It is not easy to deﬁne object-oriented programming, but we have already seen some of its
> characteristics:
> • Programs are made up of object deﬁnitions and function deﬁnitions, and most of the
> computation is express

### Rank 5

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 198

**Content:**

> 176 Chapter 18. Inheritance
> class Markov(object):
> def __init__(self):
> self.suffix_map = {}
> self.prefix = ()
> Next, we transform the functions into methods. For example, here’sprocess_word :
> def process_word(self, word, order=2):
> if len(self.prefix) < order:
> self.prefix += (word,)
> return
> try:
> self.suffix_map[self.prefix].append(word)
> except KeyError:
> # if there is no entry for this prefix, make one
> self.suffix_map[self.prefix] = [word]
> self.prefix = shift(self.prefix, word)
> Transforming a program 


---

## Hybrid Retrieval Results

### Rank 1

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 162

**Content:**

> 140 Chapter 14. Files
> If you run this program, it reads itself and prints the number of lines in the ﬁle, which is 7.
> You can also import it like this:
> >>> import wc
> 7
> Now you have a module object wc :
> >>> print wc
> <module ' wc ' from ' wc.py ' >
> That provides a function called linecount :
> >>> wc.linecount( ' wc.py ' )
> 7
> So that’s how you write modules in Python.
> The only problem with this example is that when you import the module it executes the
> test code at the bottom. Normally when you impor

### Rank 2

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 227

**Content:**

> B.3. Analysis of search algorithms 205
> • The run time of update is proportional to the size of the dictionary passed as a pa-
> rameter, not the dictionary being updated.
> • keys , values and items are linear because they return new lists; iterkeys ,
> itervalues and iteritems are constant time because they return iterators. But if
> you loop through the iterators, the loop will be linear. Using the “iter” functions
> saves some overhead, but it doesn’t change the order of growth unless the number of
> ite

### Rank 3

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 130

**Content:**

> 108 Chapter 11. Dictionaries
> 11.6 Global variables
> In the previous example, known is created outside the function, so it belongs to the special
> frame called __main__ . Variables in __main__ are sometimes called global because they
> can be accessed from any function. Unlike local variables, which disappear when their
> function ends, global variables persist from one function call to the next.
> It is common to use global variables forﬂags; that is, boolean variables that indicate (“ﬂag”)
> whether a co

### Rank 4

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 207

**Content:**

> 19.7. Menus and Callables 185
> endrow ends this row of widgets, so subsequent widgets are packed in the column Frame.
> Gui.py keeps a stack of Frames:
> • When you use row , col or gr to create a Frame, it goes on top of the stack and becomes
> the current Frame.
> • When you use endrow , endcol or endgr to close a Frame, it gets popped off the stack
> and the previous Frame on the stack becomes the current Frame.
> The method run_file reads the contents of the Entry, uses it as a ﬁlename, reads the con-
> te

### Rank 5

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 60

**Content:**

> 38 Chapter 4. Case study: interface design
> This docstring is a triple-quoted string, also known as a multiline string because the triple
> quotes allow the string to span more than one line.
> It is terse, but it contains the essential information someone would need to use this func-
> tion. It explains concisely what the function does (without getting into the details of how
> it does it). It explains what effect each parameter has on the behavior of the function and
> what type each parameter should be 


---

# Test 4: Concept explanation

**Category:** Concept explanation

**Query:**
> Explain the main idea behind Flask.

**User ID:** user_B

**Expected Topic:** Flask concepts

---

## Vector Retrieval Results

### Rank 1

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 76

**Content:**

> Explore Flask Documentation, Release 1.0
> 72 Chapter 3. Thank you

### Rank 2

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 1

**Content:**

> Explore Flask Documentation
> Release 1.0
> Robert Picard
> March 31, 2016

### Rank 3

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 73

**Content:**

> Explore Flask Documentation, Release 1.0
> 2.14 Conclusion
> I don’t feel like there’s a lot to conclude at this point. I hope reading this book has helped you in your adventure with
> Flask. If that’s the case, please get in touch with me! I would love to hear from people who enjoyed reading this. Feel
> free to let me know if you have any suggestions to improve the book as well.
> Thanks for reading!
> - Robert
> 2.14. Conclusion 69

### Rank 4

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 8

**Content:**

> Explore Flask Documentation, Release 1.0
> 4 Chapter 1. About the author

### Rank 5

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 74

**Content:**

> Explore Flask Documentation, Release 1.0
> 70 Chapter 2. Contents


---

## Hybrid Retrieval Results

### Rank 1

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 5

**Content:**

> Explore Flask Documentation, Release 1.0
> Explore Flask is a book about best practices and patterns for developing web applications with Flask. The book was
> funded by 426 backers on Kickstarter in July 2013.
> I ﬁnally released the book, after spending almost a year working on it. Almost immediately I was tired of managing
> distribution and limiting the book’s audience by putting it behind a paywall. I didn’t write a book to run a business, I
> wrote it to put some helpful content out there and help g

### Rank 2

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 9

**Content:**

> CHAPTER 2
> Contents
> 2.1 Preface
> This book is a collection of the best practices for using Flask. There are a lot of pieces to the average Flask application.
> You’ll often need to interact with a database and authenticate users, for example. In the coming pages I’ll do my best
> to explain the “right way” to do this sort of stuff. My recommendations aren’t always going to apply, but I’m hoping
> that they’ll be a good option most of the time.
> 2.1.1 Assumptions
> In order to present you with more speciﬁc 

### Rank 3

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 76

**Content:**

> Explore Flask Documentation, Release 1.0
> 72 Chapter 3. Thank you

### Rank 4

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 12

**Content:**

> Explore Flask Documentation, Release 1.0
> PEP 8: Style Guide for Python Code
> PEP 8 is the ofﬁcial style guide for Python code. I recommend that you read it and apply its recommendations to
> your Flask projects (and all of your other Python code). Your code will be much more approachable when it starts
> growing to many ﬁles with hundreds, or thousands, of lines of code. The PEP 8 recommendations are all about having
> more readable code. Plus, if your project is going to be open source, potential cont

### Rank 5

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 1

**Content:**

> Explore Flask Documentation
> Release 1.0
> Robert Picard
> March 31, 2016


---

# Test 5: Programming terminology

**Category:** Programming / API terminology

**Query:**
> What does a Python function do?

**User ID:** user_A

**Expected Topic:** Python programming

---

## Vector Retrieval Results

### Rank 1

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 41

**Content:**

> Chapter 3
> Functions
> 3.1 Function calls
> In the context of programming, afunction is a named sequence of statements that performs
> a computation. When you deﬁne a function, you specify the name and the sequence of
> statements. Later, you can “call” the function by name. We have already seen one example
> of a function call:
> >>> type(32)
> <type ' int ' >
> The name of the function is type . The expression in parentheses is called the argument of
> the function. The result, for this function, is the type of 

### Rank 2

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 179

**Content:**

> Chapter 17
> Classes and methods
> Code examples from this chapter are available from http://thinkpython.com/code/
> Time2.py .
> 17.1 Object-oriented features
> Python is an object-oriented programming language , which means that it provides fea-
> tures that support object-oriented programming.
> It is not easy to deﬁne object-oriented programming, but we have already seen some of its
> characteristics:
> • Programs are made up of object deﬁnitions and function deﬁnitions, and most of the
> computation is express

### Rank 3

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 51

**Content:**

> 3.16. Exercises 29
> stack diagram: A graphical representation of a stack of functions, their variables, and the
> values they refer to.
> frame: A box in a stack diagram that represents a function call. It contains the local vari-
> ables and parameters of the function.
> traceback: A list of the functions that are executing, printed when an exception occurs.
> 3.16 Exercises
> Exercise 3.3. Python provides a built-in function called len that returns the length of a string, so
> the value of len( ' allen ' ) i

### Rank 4

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 48

**Content:**

> 26 Chapter 3. Functions
> The order of the functions in the traceback is the same as the order of the frames in the
> stack diagram. The function that is currently running is at the bottom.
> 3.11 Fruitful functions and void functions
> Some of the functions we are using, such as the math functions, yield results; for lack of a
> better name, I call them fruitful functions. Other functions, like print_twice , perform an
> action but don’t return a value. They are calledvoid functions.
> When you call a fruitf

### Rank 5

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 36

**Content:**

> 14 Chapter 2. Variables, expressions and statements
> In Python 3, the result of this division is a float . The new operator // performs ﬂoor
> division.
> If either of the operands is a ﬂoating-point number, Python performs ﬂoating-point divi-
> sion, and the result is a float :
> >>> minute/60.0
> 0.98333333333333328
> 2.5 Expressions and statements
> An expression is a combination of values, variables, and operators. A value all by itself
> is considered an expression, and so is a variable, so the following ar


---

## Hybrid Retrieval Results

### Rank 1

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 41

**Content:**

> Chapter 3
> Functions
> 3.1 Function calls
> In the context of programming, afunction is a named sequence of statements that performs
> a computation. When you deﬁne a function, you specify the name and the sequence of
> statements. Later, you can “call” the function by name. We have already seen one example
> of a function call:
> >>> type(32)
> <type ' int ' >
> The name of the function is type . The expression in parentheses is called the argument of
> the function. The result, for this function, is the type of 

### Rank 2

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 96

**Content:**

> 74 Chapter 8. Strings
> An empty string contains no characters and has length 0, but other than that, it is the same
> as any other string.
> Exercise 8.3. Given that fruit is a string, what does fruit[:] mean?
> 8.5 Strings are immutable
> It is tempting to use the [] operator on the left side of an assignment, with the intention of
> changing a character in a string. For example:
> >>> greeting = ' Hello, world! '
> >>> greeting[0] = ' J '
> TypeError: ' str ' object does not support item assignment
> The “object

### Rank 3

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 179

**Content:**

> Chapter 17
> Classes and methods
> Code examples from this chapter are available from http://thinkpython.com/code/
> Time2.py .
> 17.1 Object-oriented features
> Python is an object-oriented programming language , which means that it provides fea-
> tures that support object-oriented programming.
> It is not easy to deﬁne object-oriented programming, but we have already seen some of its
> characteristics:
> • Programs are made up of object deﬁnitions and function deﬁnitions, and most of the
> computation is express

### Rank 4

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 60

**Content:**

> 38 Chapter 4. Case study: interface design
> This docstring is a triple-quoted string, also known as a multiline string because the triple
> quotes allow the string to span more than one line.
> It is terse, but it contains the essential information someone would need to use this func-
> tion. It explains concisely what the function does (without getting into the details of how
> it does it). It explains what effect each parameter has on the behavior of the function and
> what type each parameter should be 

### Rank 5

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 51

**Content:**

> 3.16. Exercises 29
> stack diagram: A graphical representation of a stack of functions, their variables, and the
> values they refer to.
> frame: A box in a stack diagram that represents a function call. It contains the local vari-
> ables and parameters of the function.
> traceback: A list of the functions that are executing, printed when an exception occurs.
> 3.16 Exercises
> Exercise 3.3. Python provides a built-in function called len that returns the length of a string, so
> the value of len( ' allen ' ) i


---

# Test 6: User with no documents

**Category:** Empty user scope

**Query:**
> What is Python?

**User ID:** user_C

**Expected Topic:** No results expected

---

## Vector Retrieval Results

No results.


---

## Hybrid Retrieval Results

No results.


---

# Manual Evaluation Notes

- Which retriever produced more relevant results?
- Did hybrid improve exact terminology retrieval?
- Did vector retrieval perform better for paraphrased queries?
- Were there irrelevant results?
- Were there duplicate or highly repetitive chunks?
- Which approach would I choose based on this experiment?

# Conclusion

_To be completed after manual evaluation._

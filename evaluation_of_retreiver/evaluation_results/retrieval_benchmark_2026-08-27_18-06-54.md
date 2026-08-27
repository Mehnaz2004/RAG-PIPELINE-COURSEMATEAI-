# StudyLensAI Retrieval Benchmark

## Experiment Information

- Timestamp: 2026-08-27_18-06-54
- Number of test cases: 20
- Vector database: Chroma
- Embedding model: sentence-transformers/all-MiniLM-L6-v2
- Vector retriever: Chroma similarity search
- Hybrid retriever: Vector search + BM25 + Reciprocal Rank Fusion
- Results per query: Top 5

# Test Case 1: Exact Python Concept: Polymorphism

**Category:** exact_technical_term

**Query:**

> What is polymorphism?

**User:** user_A

**Expected Topic:** Python polymorphism

**Purpose:**

Tests direct retrieval of a fundamental OOP concept.

---

## Vector Retrieval
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

### Manual Evaluation — Vector
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

## Hybrid Retrieval
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

### Manual Evaluation — Hybrid
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

# Test Case 2: Exact Python Concept: Inheritance

**Category:** exact_technical_term

**Query:**

> What is inheritance?

**User:** user_A

**Expected Topic:** Python inheritance

**Purpose:**

Tests retrieval of OOP inheritance concept.

---

## Vector Retrieval
### Rank 1

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
- Page: 189

**Content:**

> Chapter 18
> Inheritance
> In this chapter I present classes to represent playing cards, decks of cards, and poker hands.
> If you don’t play poker, you can read about it at http://en.wikipedia.org/wiki/Poker ,
> but you don’t have to; I’ll tell you what you need to know for the exercises. Code examples
> from this chapter are available from http://thinkpython.com/code/Card.py .
> If you are not familiar with Anglo-American playing cards, you can read about them at
> http://en.wikipedia.org/wiki/Playing_cards

### Rank 4

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 199

**Content:**

> 18.12. Exercises 177
> parent class: The class from which a child class inherits.
> child class: A new class created by inheriting from an existing class; also called a “sub-
> class.”
> IS-A relationship: The relationship between a child class and its parent class.
> HAS-A relationship: The relationship between two classes where instances of one class
> contain references to instances of the other.
> class diagram: A diagram that shows the classes in a program and the relationships be-
> tween them.
> multiplici

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

### Manual Evaluation — Vector
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

## Hybrid Retrieval
### Rank 1

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
- Page: 189

**Content:**

> Chapter 18
> Inheritance
> In this chapter I present classes to represent playing cards, decks of cards, and poker hands.
> If you don’t play poker, you can read about it at http://en.wikipedia.org/wiki/Poker ,
> but you don’t have to; I’ll tell you what you need to know for the exercises. Code examples
> from this chapter are available from http://thinkpython.com/code/Card.py .
> If you are not familiar with Anglo-American playing cards, you can read about them at
> http://en.wikipedia.org/wiki/Playing_cards

### Rank 4

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

### Rank 5

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 190

**Content:**

> 168 Chapter 18. Inheritance
> The mapping for ranks is fairly obvious; each of the numerical ranks maps to the corre-
> sponding integer, and for face cards:
> Jack ↦→ 11
> Queen ↦→ 12
> King ↦→ 13
> I am using the↦→ symbol to make it clear that these mappings are not part of the Python
> program. They are part of the program design, but they don’t appear explicitly in the code.
> The class deﬁnition for Card looks like this:
> class Card(object):
> """Represents a standard playing card."""
> def __init__(self, suit=

### Manual Evaluation — Hybrid
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

# Test Case 3: Exact Python Concept: Modules

**Category:** exact_technical_term

**Query:**

> What is a Python module?

**User:** user_A

**Expected Topic:** Python modules and imports

**Purpose:**

Tests retrieval of module/import terminology.

---

## Vector Retrieval
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
- Page: 217

**Content:**

> A.2. Runtime errors 195
> • If you are writing a module and using import , make sure you don’t give your module
> the same name as one of the standard Python modules.
> • If you are using import to read a module, remember that you have to restart the
> interpreter or use reload to read a modiﬁed ﬁle. If you import the module again, it
> doesn’t do anything.
> If you get stuck and you can’t ﬁgure out what is going on, one approach is to start again
> with a new program like “Hello, World!,” and make sure you c

### Rank 4

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
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

### Rank 5

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 201

**Content:**

> Chapter 19
> Case study: Tkinter
> 19.1 GUI
> Most of the programs we have seen so far are text-based, but many programs usegraphical
> user interfaces, also known as GUIs.
> Python provides several choices for writing GUI-based programs, including wxPython,
> Tkinter, and Qt. Each has pros and cons, which is why Python has not converged on a
> standard.
> The one I will present in this chapter is Tkinter because I think it is the easiest to get started
> with. Most of the concepts in this chapter apply to the ot

### Manual Evaluation — Vector
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

## Hybrid Retrieval
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
- Page: 217

**Content:**

> A.2. Runtime errors 195
> • If you are writing a module and using import , make sure you don’t give your module
> the same name as one of the standard Python modules.
> • If you are using import to read a module, remember that you have to restart the
> interpreter or use reload to read a modiﬁed ﬁle. If you import the module again, it
> doesn’t do anything.
> If you get stuck and you can’t ﬁgure out what is going on, one approach is to start again
> with a new program like “Hello, World!,” and make sure you c

### Rank 3

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 42

**Content:**

> 20 Chapter 3. Functions
> >>> float(32)
> 32.0
> >>> float( ' 3.14159 ' )
> 3.14159
> Finally, str converts its argument to a string:
> >>> str(32)
> ' 32 '
> >>> str(3.14159)
> ' 3.14159 '
> 3.3 Math functions
> Python has a math module that provides most of the familiar mathematical functions. A
> module is a ﬁle that contains a collection of related functions.
> Before we can use the module, we have to import it:
> >>> import math
> This statement creates a module object named math. If you print the module object, you
> get

### Rank 4

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 201

**Content:**

> Chapter 19
> Case study: Tkinter
> 19.1 GUI
> Most of the programs we have seen so far are text-based, but many programs usegraphical
> user interfaces, also known as GUIs.
> Python provides several choices for writing GUI-based programs, including wxPython,
> Tkinter, and Qt. Each has pros and cons, which is why Python has not converged on a
> standard.
> The one I will present in this chapter is Tkinter because I think it is the easiest to get started
> with. Most of the concepts in this chapter apply to the ot

### Rank 5

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 49

**Content:**

> 3.13. Importing with from 27
> • Dividing a long program into functions allows you to debug the parts one at a time
> and then assemble them into a working whole.
> • Well-designed functions are often useful for many programs. Once you write and
> debug one, you can reuse it.
> 3.13 Importing with from
> Python provides two ways to import modules; we have already seen one:
> >>> import math
> >>> print math
> <module ' math ' (built-in)>
> >>> print math.pi
> 3.14159265359
> If you import math , you get a module object

### Manual Evaluation — Hybrid
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

# Test Case 4: Exact Python Concept: Classes

**Category:** exact_technical_term

**Query:**

> What is a Python class?

**User:** user_A

**Expected Topic:** Python classes

**Purpose:**

Tests direct class concept retrieval.

---

## Vector Retrieval
### Rank 1

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

### Rank 2

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 166

**Content:**

> 144 Chapter 15. Classes and objects
> x
> y
> 3.0
> 4.0
> blank
> Point
> Figure 15.1: Object diagram.
> >>> print Point
> <class ' __main__.Point ' >
> Because Point is deﬁned at the top level, its “full name” is __main__.Point .
> The class object is like a factory for creating objects. To create a Point, you callPoint as if it
> were a function.
> >>> blank = Point()
> >>> print blank
> <__main__.Point instance at 0xb7e9d3ac>
> The return value is a reference to a Point object, which we assign to blank . Creating a new
> obje

### Rank 3

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 165

**Content:**

> Chapter 15
> Classes and objects
> Code examples from this chapter are available from http://thinkpython.com/code/
> Point1.py ; solutions to the exercises are available from http://thinkpython.com/code/
> Point1_soln.py .
> 15.1 User-deﬁned types
> We have used many of Python’s built-in types; now we are going to deﬁne a new type. As
> an example, we will create a type called Point that represents a point in two-dimensional
> space.
> In mathematical notation, points are often written in parentheses with a comma

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
- Page: 35

**Content:**

> 2.4. Operators and operands 13
> The underscore character, _ , can appear in a name. It is often used in names with multiple
> words, such as my_name or airspeed_of_unladen_swallow .
> If you give a variable an illegal name, you get a syntax error:
> >>> 76trombones = ' big parade '
> SyntaxError: invalid syntax
> >>> more@ = 1000000
> SyntaxError: invalid syntax
> >>> class = ' Advanced Theoretical Zymurgy '
> SyntaxError: invalid syntax
> 76trombones is illegal because it does not begin with a letter. more@ is il

### Manual Evaluation — Vector
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

## Hybrid Retrieval
### Rank 1

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 165

**Content:**

> Chapter 15
> Classes and objects
> Code examples from this chapter are available from http://thinkpython.com/code/
> Point1.py ; solutions to the exercises are available from http://thinkpython.com/code/
> Point1_soln.py .
> 15.1 User-deﬁned types
> We have used many of Python’s built-in types; now we are going to deﬁne a new type. As
> an example, we will create a type called Point that represents a point in two-dimensional
> space.
> In mathematical notation, points are often written in parentheses with a comma

### Rank 2

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 166

**Content:**

> 144 Chapter 15. Classes and objects
> x
> y
> 3.0
> 4.0
> blank
> Point
> Figure 15.1: Object diagram.
> >>> print Point
> <class ' __main__.Point ' >
> Because Point is deﬁned at the top level, its “full name” is __main__.Point .
> The class object is like a factory for creating objects. To create a Point, you callPoint as if it
> were a function.
> >>> blank = Point()
> >>> print blank
> <__main__.Point instance at 0xb7e9d3ac>
> The return value is a reference to a Point object, which we assign to blank . Creating a new
> obje

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
- Page: 183

**Content:**

> 17.6. The __str__ method 161
> 17.6 The __str__ method
> __str__ is a special method, like __init__ , that is supposed to return a string representa-
> tion of an object.
> For example, here is a str method for Time objects:
> # inside class Time:
> def __str__(self):
> return ' %.2d:%.2d:%.2d ' % (self.hour, self.minute, self.second)
> When you print an object, Python invokes the str method:
> >>> time = Time(9, 45)
> >>> print time
> 09:45:00
> When I write a new class, I almost always start by writing__init__ , whic

### Rank 5

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 35

**Content:**

> 2.4. Operators and operands 13
> The underscore character, _ , can appear in a name. It is often used in names with multiple
> words, such as my_name or airspeed_of_unladen_swallow .
> If you give a variable an illegal name, you get a syntax error:
> >>> 76trombones = ' big parade '
> SyntaxError: invalid syntax
> >>> more@ = 1000000
> SyntaxError: invalid syntax
> >>> class = ' Advanced Theoretical Zymurgy '
> SyntaxError: invalid syntax
> 76trombones is illegal because it does not begin with a letter. more@ is il

### Manual Evaluation — Hybrid
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

# Test Case 5: Keyword: Python Function

**Category:** keyword_acronym

**Query:**

> What does a Python function do?

**User:** user_A

**Expected Topic:** Python functions

**Purpose:**

Tests keyword-based matching for function concept.

---

## Vector Retrieval
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

### Manual Evaluation — Vector
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

## Hybrid Retrieval
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

### Manual Evaluation — Hybrid
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

# Test Case 6: Keyword: Flask Route

**Category:** keyword_acronym

**Query:**

> What is a route in Flask?

**User:** user_B

**Expected Topic:** Flask routing

**Purpose:**

Tests Flask-specific keyword retrieval.

---

## Vector Retrieval
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
- Page: 8

**Content:**

> Explore Flask Documentation, Release 1.0
> 4 Chapter 1. About the author

### Rank 3

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

### Rank 4

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 1

**Content:**

> Explore Flask Documentation
> Release 1.0
> Robert Picard
> March 31, 2016

### Rank 5

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 40

**Content:**

> Explore Flask Documentation, Release 1.0
> • You can also deﬁne a dynamic subdomain for all routes in a blueprint.
> • Refactoring a growing application to use blueprints can be done in ﬁve relatively small steps.
> 2.8 Templates
> While Flask doesn’t force us to use any particular templating language, it assumes that we’re going to use Jinja. Most
> of the developers in the Flask community use Jinja, and I recommend that you do the same. There are a few extensions
> that have been written to let us use oth

### Manual Evaluation — Vector
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

## Hybrid Retrieval
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

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 25

**Content:**

> Explore Flask Documentation, Release 1.0
> 2.6.1 View decorators
> Python decorators are functions that are used to transform other functions. When a decorated function is called, the
> decorator is called instead. The decorator can then take action, modify the arguments, halt execution or call the original
> function. We can use decorators to wrap views with code we’d like to run before they are executed.
> @decorator_function
> def decorated():
> pass
> If you’ve gone through the Flask tutorial, the syntax in

### Rank 3

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 34

**Content:**

> Explore Flask Documentation, Release 1.0
> Now the routes deﬁned in facebook/views/proﬁle.py (e.g. /<user_url_slug>) are registered on the application
> and act just as if you’d deﬁned them with@app.route().
> Using a dynamic URL preﬁx
> Continuing with the Facebook example, notice how all of the proﬁle routes start with the<user_url_slug> portion
> and pass that value to the view. We want users to be able to access a proﬁle by going to a URL like https://facebo-
> ok.com/john.doe. We can stop repeating our

### Rank 4

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 76

**Content:**

> Explore Flask Documentation, Release 1.0
> 72 Chapter 3. Thank you

### Rank 5

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 8

**Content:**

> Explore Flask Documentation, Release 1.0
> 4 Chapter 1. About the author

### Manual Evaluation — Hybrid
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

# Test Case 7: Keyword: Python Dictionary

**Category:** keyword_acronym

**Query:**

> What is a dictionary?

**User:** user_A

**Expected Topic:** Python dictionaries and data structures

**Purpose:**

Tests retrieval of data structure terminology.

---

## Vector Retrieval
### Rank 1

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 134

**Content:**

> 112 Chapter 11. Dictionaries

### Rank 2

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 123

**Content:**

> Chapter 11
> Dictionaries
> A dictionary is like a list, but more general. In a list, the indices have to be integers; in a
> dictionary they can be (almost) any type.
> You can think of a dictionary as a mapping between a set of indices (which are calledkeys)
> and a set of values. Each key maps to a value. The association of a key and a value is called
> a key-value pair or sometimes an item.
> As an example, we’ll build a dictionary that maps from English to Spanish words, so the
> keys and the values are al

### Rank 3

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 128

**Content:**

> 106 Chapter 11. Dictionaries
> ’a’ 1
> 1
> dict
> hist
> ’p’
> 1
> ’o’ 1
> ’r’ 2
> ’t’
> 0
> 1
> ’a’
> ’p’
> list
> 2 ’t’
> ’o’3
> 1
> dict
> inv
> 2 0
> list
> ’r’
> Figure 11.1: State diagram.
> Figure 11.1 is a state diagram showing hist and inverse . A dictionary is represented as a
> box with the type dict above it and the key-value pairs inside. If the values are integers,
> ﬂoats or strings, I usually draw them inside the box, but I usually draw lists outside the
> box, just to keep the diagram simple.
> Lists can be values in a dictionary, as

### Rank 4

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 139

**Content:**

> 12.6. Dictionaries and tuples 117
> The output of this loop is:
> 0 a
> 1 b
> 2 c
> Again.
> 12.6 Dictionaries and tuples
> Dictionaries have a method called items that returns a list of tuples, where each tuple is a
> key-value pair.
> >>> d = { ' a ' :0, ' b ' :1, ' c ' :2}
> >>> t = d.items()
> >>> print t
> [( ' a ' , 0), ( ' c ' , 2), ( ' b ' , 1)]
> As you should expect from a dictionary, the items are in no particular order. In Python 3,
> items returns an iterator, but for many purposes, iterators behave like lists

### Rank 5

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 124

**Content:**

> 102 Chapter 11. Dictionaries
> >>> print eng2sp[ ' two ' ]
> ' dos '
> The key 'two' always maps to the value ' dos ' so the order of the items doesn’t matter.
> If the key isn’t in the dictionary, you get an exception:
> >>> print eng2sp[ ' four ' ]
> KeyError: ' four '
> The len function works on dictionaries; it returns the number of key-value pairs:
> >>> len(eng2sp)
> 3
> The in operator works on dictionaries; it tells you whether something appears as a key in
> the dictionary (appearing as a value is not good e

### Manual Evaluation — Vector
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

## Hybrid Retrieval
### Rank 1

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 123

**Content:**

> Chapter 11
> Dictionaries
> A dictionary is like a list, but more general. In a list, the indices have to be integers; in a
> dictionary they can be (almost) any type.
> You can think of a dictionary as a mapping between a set of indices (which are calledkeys)
> and a set of values. Each key maps to a value. The association of a key and a value is called
> a key-value pair or sometimes an item.
> As an example, we’ll build a dictionary that maps from English to Spanish words, so the
> keys and the values are al

### Rank 2

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 125

**Content:**

> 11.2. Looping and dictionaries 103
> 3. You could create a dictionary with characters as keys and counters as the correspond-
> ing values. The ﬁrst time you see a character, you would add an item to the dictionary.
> After that you would increment the value of an existing item.
> Each of these options performs the same computation, but each of them implements that
> computation in a different way.
> An implementation is a way of performing a computation; some implementations are
> better than others. For exa

### Rank 3

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 128

**Content:**

> 106 Chapter 11. Dictionaries
> ’a’ 1
> 1
> dict
> hist
> ’p’
> 1
> ’o’ 1
> ’r’ 2
> ’t’
> 0
> 1
> ’a’
> ’p’
> list
> 2 ’t’
> ’o’3
> 1
> dict
> inv
> 2 0
> list
> ’r’
> Figure 11.1: State diagram.
> Figure 11.1 is a state diagram showing hist and inverse . A dictionary is represented as a
> box with the type dict above it and the key-value pairs inside. If the values are integers,
> ﬂoats or strings, I usually draw them inside the box, but I usually draw lists outside the
> box, just to keep the diagram simple.
> Lists can be values in a dictionary, as

### Rank 4

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 139

**Content:**

> 12.6. Dictionaries and tuples 117
> The output of this loop is:
> 0 a
> 1 b
> 2 c
> Again.
> 12.6 Dictionaries and tuples
> Dictionaries have a method called items that returns a list of tuples, where each tuple is a
> key-value pair.
> >>> d = { ' a ' :0, ' b ' :1, ' c ' :2}
> >>> t = d.items()
> >>> print t
> [( ' a ' , 0), ( ' c ' , 2), ( ' b ' , 1)]
> As you should expect from a dictionary, the items are in no particular order. In Python 3,
> items returns an iterator, but for many purposes, iterators behave like lists

### Rank 5

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 126

**Content:**

> 104 Chapter 11. Dictionaries
> def print_hist(h):
> for c in h:
> print c, h[c]
> Here’s what the output looks like:
> >>> h = histogram( ' parrot ' )
> >>> print_hist(h)
> a 1
> p 1
> r 2
> t 1
> o 1
> Again, the keys are in no particular order.
> Exercise 11.3. Dictionaries have a method called keys that returns the keys of the dictionary, in
> no particular order, as a list.
> Modify print_hist to print the keys and their values in alphabetical order.
> 11.3 Reverse lookup
> Given a dictionary d and a key k , it is easy to ﬁn

### Manual Evaluation — Hybrid
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

# Test Case 8: Paraphrased: Code Organization

**Category:** paraphrased_query

**Query:**

> How can Python code be structured so it can be reused across projects?

**User:** user_A

**Expected Topic:** Python modules and reusability

**Purpose:**

Semantic query testing module/import concepts without exact terminology.

---

## Vector Retrieval
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
- Page: 217

**Content:**

> A.2. Runtime errors 195
> • If you are writing a module and using import , make sure you don’t give your module
> the same name as one of the standard Python modules.
> • If you are using import to read a module, remember that you have to restart the
> interpreter or use reload to read a modiﬁed ﬁle. If you import the module again, it
> doesn’t do anything.
> If you get stuck and you can’t ﬁgure out what is going on, one approach is to start again
> with a new program like “Hello, World!,” and make sure you c

### Rank 5

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
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

### Manual Evaluation — Vector
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

## Hybrid Retrieval
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
- Page: 26

**Content:**

> 4 Chapter 1. The way of the program
> 1.3.2 Runtime errors
> The second type of error is a runtime error, so called because the error does not appear until
> after the program has started running. These errors are also calledexceptions because they
> usually indicate that something exceptional (and bad) has happened.
> Runtime errors are rare in the simple programs you will see in the ﬁrst few chapters, so it
> might be a while before you encounter one.
> 1.3.3 Semantic errors
> The third type of error is these

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

### Rank 5

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

### Manual Evaluation — Hybrid
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

# Test Case 9: Paraphrased: Building Web Applications

**Category:** paraphrased_query

**Query:**

> How do you create web pages that respond to user requests?

**User:** user_B

**Expected Topic:** Flask web framework basics

**Purpose:**

Tests semantic understanding of web routing without exact keyword.

---

## Vector Retrieval
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
- Page: 30

**Content:**

> Explore Flask Documentation, Release 1.0
> 2.7 Blueprints
> 2.7.1 What is a blueprint?
> A blueprint deﬁnes a collection of views, templates, static ﬁles and other elements that can be applied to an application.
> For example, let’s imagine that we have a blueprint for an admin panel. This blueprint would deﬁne the views for routes
> like /admin/login and /admin/dashboard. It may also include the templates and static ﬁles that will be served on those
> routes. We can then use this blueprint to add an admin 

### Rank 3

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 34

**Content:**

> Explore Flask Documentation, Release 1.0
> Now the routes deﬁned in facebook/views/proﬁle.py (e.g. /<user_url_slug>) are registered on the application
> and act just as if you’d deﬁned them with@app.route().
> Using a dynamic URL preﬁx
> Continuing with the Facebook example, notice how all of the proﬁle routes start with the<user_url_slug> portion
> and pass that value to the view. We want users to be able to access a proﬁle by going to a URL like https://facebo-
> ok.com/john.doe. We can stop repeating our

### Rank 4

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 36

**Content:**

> Explore Flask Documentation, Release 1.0
> views.py
> templates/
> site/
> static/
> site/
> models.py
> This table explains the different blueprints in this app.
> URL Route Description
> sitemaker.com sitemaker/homeJust a vanilla blueprint. Views, templates and static ﬁles for index.html, about.html
> and pricing.html.
> big-
> daddy.sitemaker.com
> sitemaker/siteThis blueprint uses a dynamic subdomain and includes the elements of the user’s
> website. We’ll go over some of the code used to implement this blueprint below

### Rank 5

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 59

**Content:**

> Explore Flask Documentation, Release 1.0
> 2.12 Patterns for handling users
> One of the most common things that modern web applications need to do is handle users. An application with basic
> account features needs to handle a lot of things like registration, email conﬁrmation, securely storing passwords, secure
> password reset, authentication and more. Since a lot of security issues present themselves when it comes to handling
> users, it’s generally best to stick to standard patterns in this area.
> Not

### Manual Evaluation — Vector
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

## Hybrid Retrieval
### Rank 1

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 59

**Content:**

> Explore Flask Documentation, Release 1.0
> 2.12 Patterns for handling users
> One of the most common things that modern web applications need to do is handle users. An application with basic
> account features needs to handle a lot of things like registration, email conﬁrmation, securely storing passwords, secure
> password reset, authentication and more. Since a lot of security issues present themselves when it comes to handling
> users, it’s generally best to stick to standard patterns in this area.
> Not

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
- Page: 5

**Content:**

> Explore Flask Documentation, Release 1.0
> Explore Flask is a book about best practices and patterns for developing web applications with Flask. The book was
> funded by 426 backers on Kickstarter in July 2013.
> I ﬁnally released the book, after spending almost a year working on it. Almost immediately I was tired of managing
> distribution and limiting the book’s audience by putting it behind a paywall. I didn’t write a book to run a business, I
> wrote it to put some helpful content out there and help g

### Rank 4

- Filename: Python.pdf
- Document ID: fc38bfb7-e987-444c-b769-7718c5060cfc
- Page: 29

**Content:**

> 1.6. Debugging 7
> 1.6 Debugging
> It is a good idea to read this book in front of a computer so you can try out the examples as
> you go. You can run most of the examples in interactive mode, but if you put the code in a
> script, it is easier to try out variations.
> Whenever you are experimenting with a new feature, you should try to make mistakes.
> For example, in the “Hello, world!” program, what happens if you leave out one of the
> quotation marks? What if you leave out both? What if you spell print w

### Rank 5

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 30

**Content:**

> Explore Flask Documentation, Release 1.0
> 2.7 Blueprints
> 2.7.1 What is a blueprint?
> A blueprint deﬁnes a collection of views, templates, static ﬁles and other elements that can be applied to an application.
> For example, let’s imagine that we have a blueprint for an admin panel. This blueprint would deﬁne the views for routes
> like /admin/login and /admin/dashboard. It may also include the templates and static ﬁles that will be served on those
> routes. We can then use this blueprint to add an admin 

### Manual Evaluation — Hybrid
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

# Test Case 10: Paraphrased: Object-Oriented Organization

**Category:** paraphrased_query

**Query:**

> How do you organize data and behaviors together in Python?

**User:** user_A

**Expected Topic:** Classes and object-oriented programming

**Purpose:**

Semantic query about OOP concepts without exact terminology.

---

## Vector Retrieval
### Rank 1

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 151

**Content:**

> solution from http://thinkpython.com/code/markov.py . You will also need http://
> thinkpython.com/code/emma.txt .
> 13.9 Data structures
> Using Markov analysis to generate random text is fun, but there is also a point to this
> exercise: data structure selection. In your solution to the previous exercises, you had to
> choose:
> • How to represent the preﬁxes.

### Rank 2

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 1

**Content:**

> Think Python
> How to Think Like a Computer Scientist
> Version 2.0.17

### Rank 3

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 152

**Content:**

> 130 Chapter 13. Case study: data structure selection
> • How to represent the collection of possible sufﬁxes.
> • How to represent the mapping from each preﬁx to the collection of possible sufﬁxes.
> Ok, the last one is easy; the only mapping type we have seen is a dictionary, so it is the
> natural choice.
> For the preﬁxes, the most obvious options are string, list of strings, or tuple of strings. For
> the sufﬁxes, one option is a list; another is a histogram (dictionary).
> How should you choose? The ﬁrst

### Rank 4

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 53

**Content:**

> Chapter 4
> Case study: interface design
> Code examples from this chapter are available from http://thinkpython.com/code/
> polygon.py .
> 4.1 T urtleWorld
> To accompany this book, I have written a package called Swampy. You can download
> Swampy from http://thinkpython.com/swampy ; follow the instructions there to install
> Swampy on your system.
> A package is a collection of modules; one of the modules in Swampy is TurtleWorld ,
> which provides a set of functions for drawing lines by steering turtles around

### Rank 5

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

### Manual Evaluation — Vector
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

## Hybrid Retrieval
### Rank 1

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 152

**Content:**

> 130 Chapter 13. Case study: data structure selection
> • How to represent the collection of possible sufﬁxes.
> • How to represent the mapping from each preﬁx to the collection of possible sufﬁxes.
> Ok, the last one is easy; the only mapping type we have seen is a dictionary, so it is the
> natural choice.
> For the preﬁxes, the most obvious options are string, list of strings, or tuple of strings. For
> the sufﬁxes, one option is a list; another is a histogram (dictionary).
> How should you choose? The ﬁrst

### Rank 2

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 151

**Content:**

> solution from http://thinkpython.com/code/markov.py . You will also need http://
> thinkpython.com/code/emma.txt .
> 13.9 Data structures
> Using Markov analysis to generate random text is fun, but there is also a point to this
> exercise: data structure selection. In your solution to the previous exercises, you had to
> choose:
> • How to represent the preﬁxes.

### Rank 3

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 1

**Content:**

> Think Python
> How to Think Like a Computer Scientist
> Version 2.0.17

### Rank 4

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 44

**Content:**

> 22 Chapter 3. Functions
> >>> def print_lyrics():
> ... print "I ' m a lumberjack, and I ' m okay."
> ... print "I sleep all night and I work all day."
> ...
> To end the function, you have to enter an empty line (this is not necessary in a script).
> Deﬁning a function creates a variable with the same name.
> >>> print print_lyrics
> <function print_lyrics at 0xb7e99e9c>
> >>> type(print_lyrics)
> <type ' function ' >
> The value of print_lyrics is a function object, which has type ' function ' .
> The syntax for call

### Rank 5

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 228

**Content:**

> 206 Appendix B. Analysis of Algorithms
> Exercise B.3. Write a function called bisection that takes a sorted list and a target value and
> returns the index of the value in the list, if it’s there, orNone if it’s not.
> Or you could read the documentation of the bisect module and use that!
> Bisection search can be much faster than linear search, but it requires the sequence to be in
> order, which might require extra work.
> There is another data structure, called a hashtable that is even faster—it can do 

### Manual Evaluation — Hybrid
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

# Test Case 11: Conceptual: Purpose of Functions

**Category:** conceptual_explanation

**Query:**

> How do functions help organize a Python program?

**User:** user_A

**Expected Topic:** Functions and program structure

**Purpose:**

Tests retrieval of explanatory content about program organization.

---

## Vector Retrieval
### Rank 1

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

### Rank 2

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

### Rank 3

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

### Rank 4

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 13

**Content:**

> Contents
> Preface v
> 1 The way of the program 1
> 1.1 The Python programming language . . . . . . . . . . . . . . . . . . . . . . 1
> 1.2 What is a program? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
> 1.3 What is debugging? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
> 1.4 Formal and natural languages . . . . . . . . . . . . . . . . . . . . . . . . . . 5
> 1.5 The ﬁrst program . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
> 1.6 Debugging . . 

### Rank 5

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

### Manual Evaluation — Vector
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

## Hybrid Retrieval
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
- Page: 220

**Content:**

> 198 Appendix A. Debugging
> To simplify the program, there are several things you can do. First, scale down the problem
> the program is working on. For example, if you are searching a list, search a small list. If
> the program takes input from the user, give it the simplest input that causes the problem.
> Second, clean up the program. Remove dead code and reorganize the program to make
> it as easy to read as possible. For example, if you suspect that the problem is in a deeply
> nested part of the progr

### Rank 4

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

### Rank 5

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 222

**Content:**

> 200 Appendix A. Debugging
> A.3.4 I’m really, really stuck and I need help.
> First, try getting away from the computer for a few minutes. Computers emit waves that
> affect the brain, causing these symptoms:
> • Frustration and rage.
> • Superstitious beliefs (“the computer hates me”) and magical thinking (“the program
> only works when I wear my hat backward”).
> • Random walk programming (the attempt to program by writing every possible pro-
> gram and choosing the one that does the right thing).
> If you ﬁnd 

### Manual Evaluation — Hybrid
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

# Test Case 12: Conceptual: Purpose of Flask

**Category:** conceptual_explanation

**Query:**

> What is the purpose of Flask?

**User:** user_B

**Expected Topic:** Flask framework purpose and use cases

**Purpose:**

Tests retrieval of framework overview and purpose.

---

## Vector Retrieval
### Rank 1

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 1

**Content:**

> Explore Flask Documentation
> Release 1.0
> Robert Picard
> March 31, 2016

### Rank 2

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 76

**Content:**

> Explore Flask Documentation, Release 1.0
> 72 Chapter 3. Thank you

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

### Manual Evaluation — Vector
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

## Hybrid Retrieval
### Rank 1

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 1

**Content:**

> Explore Flask Documentation
> Release 1.0
> Robert Picard
> March 31, 2016

### Rank 2

- Filename: Python.pdf
- Document ID: fc38bfb7-e987-444c-b769-7718c5060cfc
- Page: 29

**Content:**

> 1.6. Debugging 7
> 1.6 Debugging
> It is a good idea to read this book in front of a computer so you can try out the examples as
> you go. You can run most of the examples in interactive mode, but if you put the code in a
> script, it is easier to try out variations.
> Whenever you are experimenting with a new feature, you should try to make mistakes.
> For example, in the “Hello, world!” program, what happens if you leave out one of the
> quotation marks? What if you leave out both? What if you spell print w

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
- Page: 55

**Content:**

> Explore Flask Documentation, Release 1.0
> As of 0.9, we should be importing that stuff straight fromwtforms.
> The form we deﬁned is going to be a user sign-in form. We could have called it SignInForm(), but by keeping
> things a little more abstract, we can re-use this same form class for other things, like a sign-up form. If we were to
> deﬁne purpose-speciﬁc form classes we’d end up with a lot of identical forms for no good reason. It’s much cleaner
> to name forms based on the ﬁelds they contain, as 

### Rank 5

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

### Manual Evaluation — Hybrid
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

# Test Case 13: Conceptual: Object-Oriented Design

**Category:** conceptual_explanation

**Query:**

> How does object-oriented programming help with writing better code?

**User:** user_A

**Expected Topic:** OOP design principles and benefits

**Purpose:**

Tests retrieval of conceptual explanations about OOP benefits.

---

## Vector Retrieval
### Rank 1

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

### Rank 2

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
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

### Rank 5

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 59

**Content:**

> 4.8. A development plan 37
> Finally, we can rewrite circle to use arc :
> def circle(t, r):
> arc(t, r, 360)
> This process—rearranging a program to improve function interfaces and facilitate code re-
> use—is called refactoring. In this case, we noticed that there was similar code in arc and
> polygon , so we “factored it out” into polyline .
> If we had planned ahead, we might have written polyline ﬁrst and avoided refactoring,
> but often you don’t know enough at the beginning of a project to design all the

### Manual Evaluation — Vector
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

## Hybrid Retrieval
### Rank 1

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

### Rank 2

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 181

**Content:**

> 17.3. Another example 159
> By convention, the ﬁrst parameter of a method is calledself , so it would be more common
> to write print_time like this:
> class Time(object):
> def print_time(self):
> print ' %.2d:%.2d:%.2d ' % (self.hour, self.minute, self.second)
> The reason for this convention is an implicit metaphor:
> • The syntax for a function call, print_time(start) , suggests that the function is the
> active agent. It says something like, “Hey print_time ! Here’s an object for you to
> print.”
> • In object

### Rank 3

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
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

### Rank 4

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 187

**Content:**

> 17.12. Glossary 165
> Keeping the interface separate from the implementation means that you have to hide the
> attributes. Code in other parts of the program (outside the class deﬁnition) should use
> methods to read and modify the state of the object. They should not access the attributes di-
> rectly. This principle is called information hiding; see http://en.wikipedia.org/wiki/
> Information_hiding .
> Exercise 17.6. Download the code from this chapter ( http: // thinkpython. com/ code/
> Time2. py ). Chan

### Rank 5

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

### Manual Evaluation — Hybrid
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

# Test Case 14: Programming: Import Statement

**Category:** programming_api_terminology

**Query:**

> What does an import statement do in Python?

**User:** user_A

**Expected Topic:** Python imports and module loading

**Purpose:**

Tests code-level terminology and mechanics.

---

## Vector Retrieval
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
- Page: 217

**Content:**

> A.2. Runtime errors 195
> • If you are writing a module and using import , make sure you don’t give your module
> the same name as one of the standard Python modules.
> • If you are using import to read a module, remember that you have to restart the
> interpreter or use reload to read a modiﬁed ﬁle. If you import the module again, it
> doesn’t do anything.
> If you get stuck and you can’t ﬁgure out what is going on, one approach is to start again
> with a new program like “Hello, World!,” and make sure you c

### Rank 3

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
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

### Rank 4

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 13

**Content:**

> Contents
> Preface v
> 1 The way of the program 1
> 1.1 The Python programming language . . . . . . . . . . . . . . . . . . . . . . 1
> 1.2 What is a program? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
> 1.3 What is debugging? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
> 1.4 Formal and natural languages . . . . . . . . . . . . . . . . . . . . . . . . . . 5
> 1.5 The ﬁrst program . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
> 1.6 Debugging . . 

### Rank 5

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 160

**Content:**

> 138 Chapter 14. Files
> >>> import pickle
> >>> t = [1, 2, 3]
> >>> pickle.dumps(t)
> ' (lp0\nI1\naI2\naI3\na. '
> The format isn’t obvious to human readers; it is meant to be easy for pickle to interpret.
> pickle.loads (“load string”) reconstitutes the object:
> >>> t1 = [1, 2, 3]
> >>> s = pickle.dumps(t1)
> >>> t2 = pickle.loads(s)
> >>> print t2
> [1, 2, 3]
> Although the new object has the same value as the old, it is not (in general) the same object:
> >>> t1 == t2
> True
> >>> t1 is t2
> False
> In other words, pickling 

### Manual Evaluation — Vector
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

## Hybrid Retrieval
### Rank 1

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 217

**Content:**

> A.2. Runtime errors 195
> • If you are writing a module and using import , make sure you don’t give your module
> the same name as one of the standard Python modules.
> • If you are using import to read a module, remember that you have to restart the
> interpreter or use reload to read a modiﬁed ﬁle. If you import the module again, it
> doesn’t do anything.
> If you get stuck and you can’t ﬁgure out what is going on, one approach is to start again
> with a new program like “Hello, World!,” and make sure you c

### Rank 2

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

### Rank 3

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 49

**Content:**

> 3.13. Importing with from 27
> • Dividing a long program into functions allows you to debug the parts one at a time
> and then assemble them into a working whole.
> • Well-designed functions are often useful for many programs. Once you write and
> debug one, you can reuse it.
> 3.13 Importing with from
> Python provides two ways to import modules; we have already seen one:
> >>> import math
> >>> print math
> <module ' math ' (built-in)>
> >>> print math.pi
> 3.14159265359
> If you import math , you get a module object

### Rank 4

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 70

**Content:**

> 48 Chapter 5. Conditionals and recursion
> The same is true of runtime errors.
> Suppose you are trying to compute a signal-to-noise ratio in decibels. The formula is
> SNR db = 10 log10(Psignal /Pnoise ). In Python, you might write something like this:
> import math
> signal_power = 9
> noise_power = 10
> ratio = signal_power / noise_power
> decibels = 10 * math.log10(ratio)
> print decibels
> But when you run it in Python 2, you get an error message.
> Traceback (most recent call last):
> File "snr.py", line 5, in ?
> 

### Rank 5

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
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

### Manual Evaluation — Hybrid
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

# Test Case 15: Programming: Flask Decorators

**Category:** programming_api_terminology

**Query:**

> What is a decorator in Flask?

**User:** user_B

**Expected Topic:** Python decorators and Flask usage

**Purpose:**

Tests specific code construct terminology.

---

## Vector Retrieval
### Rank 1

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 25

**Content:**

> Explore Flask Documentation, Release 1.0
> 2.6.1 View decorators
> Python decorators are functions that are used to transform other functions. When a decorated function is called, the
> decorator is called instead. The decorator can then take action, modify the arguments, halt execution or call the original
> function. We can use decorators to wrap views with code we’d like to run before they are executed.
> @decorator_function
> def decorated():
> pass
> If you’ve gone through the Flask tutorial, the syntax in

### Rank 2

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 27

**Content:**

> Explore Flask Documentation, Release 1.0
> 10 When a function is decorated with@check_expired,check_expired() is called and the decorated
> function is passed as a parameter.
> 11 @wraps is a decorator that does some bookkeeping so thatdecorated_function() appears as
> func() for the purposes of documentation and debugging. This makes the behavior of the functions a little
> more natural.
> 12 decorated_function will get all of the args and kwargs that were passed to the original view function
> func(). This 

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
- Page: 8

**Content:**

> Explore Flask Documentation, Release 1.0
> 4 Chapter 1. About the author

### Rank 5

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 1

**Content:**

> Explore Flask Documentation
> Release 1.0
> Robert Picard
> March 31, 2016

### Manual Evaluation — Vector
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

## Hybrid Retrieval
### Rank 1

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 25

**Content:**

> Explore Flask Documentation, Release 1.0
> 2.6.1 View decorators
> Python decorators are functions that are used to transform other functions. When a decorated function is called, the
> decorator is called instead. The decorator can then take action, modify the arguments, halt execution or call the original
> function. We can use decorators to wrap views with code we’d like to run before they are executed.
> @decorator_function
> def decorated():
> pass
> If you’ve gone through the Flask tutorial, the syntax in

### Rank 2

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 27

**Content:**

> Explore Flask Documentation, Release 1.0
> 10 When a function is decorated with@check_expired,check_expired() is called and the decorated
> function is passed as a parameter.
> 11 @wraps is a decorator that does some bookkeeping so thatdecorated_function() appears as
> func() for the purposes of documentation and debugging. This makes the behavior of the functions a little
> more natural.
> 12 decorated_function will get all of the args and kwargs that were passed to the original view function
> func(). This 

### Rank 3

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 31

**Content:**

> Explore Flask Documentation, Release 1.0
> 2.7.3 Where do you put them?
> Like everything with Flask, there are many ways that we can organize our app using blueprints. With blueprints, we
> can think of the choice as functional versus divisional (terms I’m borrowing from the business world).
> Functional structure
> With a functional structure, you organize the pieces of your app by what they do. Templates are grouped together in
> one directory, static ﬁles in another and views in a third.
> yourapp/
> __init

### Rank 4

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 76

**Content:**

> Explore Flask Documentation, Release 1.0
> 72 Chapter 3. Thank you

### Rank 5

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 44

**Content:**

> Explore Flask Documentation, Release 1.0
> Note: Jinja already has an upper ﬁlter that does this, and a capitalize ﬁlter that capitalizes the ﬁrst character
> and lowercases the rest. These also handle unicode conversion, but we’ll keep our example simple to focus on the
> concept at hand.
> We’re going to deﬁne our ﬁlter in a module located atmyapp/util/ﬁlters.py. This gives us autil package in which to
> put other miscellaneous modules.
> # myapp/util/filters.py
> from .. import app
> @app.template_filter()
> d

### Manual Evaluation — Hybrid
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

# Test Case 16: Programming: Object Attributes

**Category:** programming_api_terminology

**Query:**

> What are attributes of an object in Python?

**User:** user_A

**Expected Topic:** Object attributes and instance variables

**Purpose:**

Tests OOP terminology at code level.

---

## Vector Retrieval
### Rank 1

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 186

**Content:**

> 164 Chapter 17. Classes and methods
> 17.10 Debugging
> It is legal to add attributes to objects at any point in the execution of a program, but if you
> are a stickler for type theory, it is a dubious practice to have objects of the same type with
> different attribute sets. It is usually a good idea to initialize all of an object’s attributes in
> the init method.
> If you are not sure whether an object has a particular attribute, you can use the built-in
> function hasattr (see Section 15.7).
> Another way t

### Rank 2

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 166

**Content:**

> 144 Chapter 15. Classes and objects
> x
> y
> 3.0
> 4.0
> blank
> Point
> Figure 15.1: Object diagram.
> >>> print Point
> <class ' __main__.Point ' >
> Because Point is deﬁned at the top level, its “full name” is __main__.Point .
> The class object is like a factory for creating objects. To create a Point, you callPoint as if it
> were a function.
> >>> blank = Point()
> >>> print blank
> <__main__.Point instance at 0xb7e9d3ac>
> The return value is a reference to a Point object, which we assign to blank . Creating a new
> obje

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
- Page: 165

**Content:**

> Chapter 15
> Classes and objects
> Code examples from this chapter are available from http://thinkpython.com/code/
> Point1.py ; solutions to the exercises are available from http://thinkpython.com/code/
> Point1_soln.py .
> 15.1 User-deﬁned types
> We have used many of Python’s built-in types; now we are going to deﬁne a new type. As
> an example, we will create a type called Point that represents a point in two-dimensional
> space.
> In mathematical notation, points are often written in parentheses with a comma

### Manual Evaluation — Vector
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

## Hybrid Retrieval
### Rank 1

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 186

**Content:**

> 164 Chapter 17. Classes and methods
> 17.10 Debugging
> It is legal to add attributes to objects at any point in the execution of a program, but if you
> are a stickler for type theory, it is a dubious practice to have objects of the same type with
> different attribute sets. It is usually a good idea to initialize all of an object’s attributes in
> the init method.
> If you are not sure whether an object has a particular attribute, you can use the built-in
> function hasattr (see Section 15.7).
> Another way t

### Rank 2

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 166

**Content:**

> 144 Chapter 15. Classes and objects
> x
> y
> 3.0
> 4.0
> blank
> Point
> Figure 15.1: Object diagram.
> >>> print Point
> <class ' __main__.Point ' >
> Because Point is deﬁned at the top level, its “full name” is __main__.Point .
> The class object is like a factory for creating objects. To create a Point, you callPoint as if it
> were a function.
> >>> blank = Point()
> >>> print blank
> <__main__.Point instance at 0xb7e9d3ac>
> The return value is a reference to a Point object, which we assign to blank . Creating a new
> obje

### Rank 3

- Filename: Python.pdf
- Document ID: ed4a376f-4c62-429a-9830-d656f9f33e45
- Page: 190

**Content:**

> 168 Chapter 18. Inheritance
> The mapping for ranks is fairly obvious; each of the numerical ranks maps to the corre-
> sponding integer, and for face cards:
> Jack ↦→ 11
> Queen ↦→ 12
> King ↦→ 13
> I am using the↦→ symbol to make it clear that these mappings are not part of the Python
> program. They are part of the program design, but they don’t appear explicitly in the code.
> The class deﬁnition for Card looks like this:
> class Card(object):
> """Represents a standard playing card."""
> def __init__(self, suit=

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
- Page: 167

**Content:**

> 15.3. Rectangles 145
> >>> print ' (%g, %g) ' % (blank.x, blank.y)
> (3.0, 4.0)
> >>> distance = math.sqrt(blank.x**2 + blank.y**2)
> >>> print distance
> 5.0
> You can pass an instance as an argument in the usual way. For example:
> def print_point(p):
> print ' (%g, %g) ' % (p.x, p.y)
> print_point takes a point as an argument and displays it in mathematical notation. To
> invoke it, you can pass blank as an argument:
> >>> print_point(blank)
> (3.0, 4.0)
> Inside the function, p is an alias for blank , so if the funct

### Manual Evaluation — Hybrid
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

# Test Case 17: Multi-Doc: Python Question for user_B

**Category:** multi_document_user

**Query:**

> What are Python exceptions?

**User:** user_B

**Expected Topic:** Python exception handling (likely from Python.pdf)

**Purpose:**

Tests that Python-related query correctly retrieves from Python.pdf when user has multiple docs.

---

## Vector Retrieval
### Rank 1

- Filename: Python.pdf
- Document ID: fc38bfb7-e987-444c-b769-7718c5060cfc
- Page: 215

**Content:**

> Appendix A
> Debugging
> Different kinds of errors can occur in a program, and it is useful to distinguish among them
> in order to track them down more quickly:
> • Syntax errors are produced by Python when it is translating the source code into
> byte code. They usually indicate that there is something wrong with the syntax of
> the program. Example: Omitting the colon at the end of a def statement yields the
> somewhat redundant message SyntaxError: invalid syntax .
> • Runtime errors are produced by the int

### Rank 2

- Filename: Python.pdf
- Document ID: fc38bfb7-e987-444c-b769-7718c5060cfc
- Page: 26

**Content:**

> 4 Chapter 1. The way of the program
> 1.3.2 Runtime errors
> The second type of error is a runtime error, so called because the error does not appear until
> after the program has started running. These errors are also calledexceptions because they
> usually indicate that something exceptional (and bad) has happened.
> Runtime errors are rare in the simple programs you will see in the ﬁrst few chapters, so it
> might be a while before you encounter one.
> 1.3.3 Semantic errors
> The third type of error is these

### Rank 3

- Filename: Python.pdf
- Document ID: fc38bfb7-e987-444c-b769-7718c5060cfc
- Page: 159

**Content:**

> 14.6. Databases 137
> If an error occurs while opening, reading, writing or closing ﬁles, your program should catch the
> exception, print an error message, and exit. Solution: http: // thinkpython. com/ code/ sed.
> py .
> 14.6 Databases
> A database is a ﬁle that is organized for storing data. Most databases are organized like a
> dictionary in the sense that they map from keys to values. The biggest difference is that the
> database is on disk (or other permanent storage), so it persists after the program 

### Rank 4

- Filename: Python.pdf
- Document ID: fc38bfb7-e987-444c-b769-7718c5060cfc
- Page: 13

**Content:**

> Contents
> Preface v
> 1 The way of the program 1
> 1.1 The Python programming language . . . . . . . . . . . . . . . . . . . . . . 1
> 1.2 What is a program? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
> 1.3 What is debugging? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
> 1.4 Formal and natural languages . . . . . . . . . . . . . . . . . . . . . . . . . . 5
> 1.5 The ﬁrst program . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
> 1.6 Debugging . . 

### Rank 5

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

### Manual Evaluation — Vector
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

## Hybrid Retrieval
### Rank 1

- Filename: Python.pdf
- Document ID: fc38bfb7-e987-444c-b769-7718c5060cfc
- Page: 158

**Content:**

> 136 Chapter 14. Files
> if os.path.isfile(path):
> print path
> else:
> walk(path)
> os.path.join takes a directory and a ﬁle name and joins them into a complete path.
> Exercise 14.1. The os module provides a function called walk that is similar to this one but more
> versatile. Read the documentation and use it to print the names of the ﬁles in a given directory and
> its subdirectories.
> Solution: http: // thinkpython. com/ code/ walk. py .
> 14.5 Catching exceptions
> A lot of things can go wrong when you try to

### Rank 2

- Filename: Python.pdf
- Document ID: fc38bfb7-e987-444c-b769-7718c5060cfc
- Page: 215

**Content:**

> Appendix A
> Debugging
> Different kinds of errors can occur in a program, and it is useful to distinguish among them
> in order to track them down more quickly:
> • Syntax errors are produced by Python when it is translating the source code into
> byte code. They usually indicate that there is something wrong with the syntax of
> the program. Example: Omitting the colon at the end of a def statement yields the
> somewhat redundant message SyntaxError: invalid syntax .
> • Runtime errors are produced by the int

### Rank 3

- Filename: Python.pdf
- Document ID: fc38bfb7-e987-444c-b769-7718c5060cfc
- Page: 170

**Content:**

> 148 Chapter 15. Classes and objects
> y
> 0.0x
> 0.0
> width
> height
> 100.0
> corner
> 200.0
> box 100.0
> 200.0
> width
> height
> corner
> box2
> Figure 15.3: Object diagram.
> >>> box2 = copy.copy(box)
> >>> box2 is box
> False
> >>> box2.corner is box.corner
> True
> Figure 15.3 shows what the object diagram looks like. This operation is called a shallow
> copy because it copies the object and any references it contains, but not the embedded
> objects.
> For most applications, this is not what you want. In this example, invoking
> grow_re

### Rank 4

- Filename: Python.pdf
- Document ID: fc38bfb7-e987-444c-b769-7718c5060cfc
- Page: 26

**Content:**

> 4 Chapter 1. The way of the program
> 1.3.2 Runtime errors
> The second type of error is a runtime error, so called because the error does not appear until
> after the program has started running. These errors are also calledexceptions because they
> usually indicate that something exceptional (and bad) has happened.
> Runtime errors are rare in the simple programs you will see in the ﬁrst few chapters, so it
> might be a while before you encounter one.
> 1.3.3 Semantic errors
> The third type of error is these

### Rank 5

- Filename: Python.pdf
- Document ID: fc38bfb7-e987-444c-b769-7718c5060cfc
- Page: 19

**Content:**

> Contents xix
> 14.5 Catching exceptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
> 14.6 Databases . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
> 14.7 Pickling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
> 14.8 Pipes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
> 14.9 Writing modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
> 14.10 Debugging

### Manual Evaluation — Hybrid
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

# Test Case 18: Multi-Doc: Flask-Specific Question

**Category:** multi_document_user

**Query:**

> How do you handle HTTP requests in Flask?

**User:** user_B

**Expected Topic:** Flask HTTP request handling (likely from Flask.pdf)

**Purpose:**

Tests that Flask question retrieves from Flask.pdf when user has multiple docs.

---

## Vector Retrieval
### Rank 1

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 70

**Content:**

> Explore Flask Documentation, Release 1.0
> 2.13.2 The stack
> This section will cover some of the software that we’ll need to install on our server to serve our Flask application to
> the world. The basic stack is a front server that reverse proxies requests to an application runner that is running our
> Flask app. We’ll usually have a database too, so we’ll talk a little about those options as well.
> Application runner
> The server that we use to run Flask locally when we’re developing our application isn

### Rank 2

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 25

**Content:**

> Explore Flask Documentation, Release 1.0
> 2.6.1 View decorators
> Python decorators are functions that are used to transform other functions. When a decorated function is called, the
> decorator is called instead. The decorator can then take action, modify the arguments, halt execution or call the original
> function. We can use decorators to wrap views with code we’d like to run before they are executed.
> @decorator_function
> def decorated():
> pass
> If you’ve gone through the Flask tutorial, the syntax in

### Rank 3

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 40

**Content:**

> Explore Flask Documentation, Release 1.0
> • You can also deﬁne a dynamic subdomain for all routes in a blueprint.
> • Refactoring a growing application to use blueprints can be done in ﬁve relatively small steps.
> 2.8 Templates
> While Flask doesn’t force us to use any particular templating language, it assumes that we’re going to use Jinja. Most
> of the developers in the Flask community use Jinja, and I recommend that you do the same. There are a few extensions
> that have been written to let us use oth

### Rank 4

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 1

**Content:**

> Explore Flask Documentation
> Release 1.0
> Robert Picard
> March 31, 2016

### Rank 5

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 76

**Content:**

> Explore Flask Documentation, Release 1.0
> 72 Chapter 3. Thank you

### Manual Evaluation — Vector
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

## Hybrid Retrieval
### Rank 1

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 25

**Content:**

> Explore Flask Documentation, Release 1.0
> 2.6.1 View decorators
> Python decorators are functions that are used to transform other functions. When a decorated function is called, the
> decorator is called instead. The decorator can then take action, modify the arguments, halt execution or call the original
> function. We can use decorators to wrap views with code we’d like to run before they are executed.
> @decorator_function
> def decorated():
> pass
> If you’ve gone through the Flask tutorial, the syntax in

### Rank 2

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 70

**Content:**

> Explore Flask Documentation, Release 1.0
> 2.13.2 The stack
> This section will cover some of the software that we’ll need to install on our server to serve our Flask application to
> the world. The basic stack is a front server that reverse proxies requests to an application runner that is running our
> Flask app. We’ll usually have a database too, so we’ll talk a little about those options as well.
> Application runner
> The server that we use to run Flask locally when we’re developing our application isn

### Rank 3

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 72

**Content:**

> Explore Flask Documentation, Release 1.0
> }
> }
> Now we’ll create a symlink to this ﬁle at/etc/nginx/sites-enabled and restart Nginx.
> $ sudo ln -s \
> /etc/nginx/sites-available/exploreflask.com \
> /etc/nginx/sites-enabled/exploreflask.com
> We should now be able to make our requests to Nginx and receive the response from our app.
> Note: The Nginx conﬁguration section in the Gunicorn docs will give you more information about setting Nginx up
> for this purpose.
> ProxyFix
> We may run into some issues with Flas

### Rank 4

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 71

**Content:**

> Explore Flask Documentation, Release 1.0
> Making Gunicorn public
> Warning: Gunicorn is meant to sit behind a reverse proxy. If you tell it to listen to requests coming in from the
> public, it makes an easy target for denial of service attacks. It’s just not meant to handle those kinds of requests.
> Only allow outside connections for debugging purposes and make sure to switch it back to only allowing internal
> connections when you’re done.
> If we run Gunicorn like we have in the listings, we won’t be a

### Rank 5

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 40

**Content:**

> Explore Flask Documentation, Release 1.0
> • You can also deﬁne a dynamic subdomain for all routes in a blueprint.
> • Refactoring a growing application to use blueprints can be done in ﬁve relatively small steps.
> 2.8 Templates
> While Flask doesn’t force us to use any particular templating language, it assumes that we’re going to use Jinja. Most
> of the developers in the Flask community use Jinja, and I recommend that you do the same. There are a few extensions
> that have been written to let us use oth

### Manual Evaluation — Hybrid
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

# Test Case 19: Multi-Doc: General Web Development

**Category:** multi_document_user

**Query:**

> What is a web server?

**User:** user_B

**Expected Topic:** Web server concepts (could be in either document)

**Purpose:**

Tests retrieval relevance when concept may appear in multiple documents.

---

## Vector Retrieval
### Rank 1

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 69

**Content:**

> Explore Flask Documentation, Release 1.0
> Amazon Web Services EC2
> Amazon Web Services is a collection of services provided by ... Amazon! There’s a good chance that you’ve heard
> of them before as they’re probably the most popular choice for new startups these days. The AWS service that we’re
> most concerned with here is EC2, or Elastic Compute Cloud. The big selling point of EC2 is that we get virtual servers
> - or instances as they’re called in AWS parlance - that spin up in seconds. If we need to

### Rank 2

- Filename: Python.pdf
- Document ID: fc38bfb7-e987-444c-b769-7718c5060cfc
- Page: 155

**Content:**

> Chapter 14
> Files
> 14.1 Persistence
> Most of the programs we have seen so far are transient in the sense that they run for a short
> time and produce some output, but when they end, their data disappears. If you run the
> program again, it starts with a clean slate.
> Other programs are persistent: they run for a long time (or all the time); they keep at least
> some of their data in permanent storage (a hard drive, for example); and if they shut down
> and restart, they pick up where they left off.
> Examples

### Rank 3

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 69

**Content:**

> • Heroku Postgres
> • Amazon RDS
> Digital Ocean
> Digital Ocean is an EC2 competitor that has recently begun to take off. Like EC2, Digital Ocean lets us spin up virtual
> servers - now called droplets - quickly. All droplets run on SSDs, which isn’t something we get at the lower levels
> of EC2. The biggest selling point for me personally is an interface that is far simpler and easier to use than the AWS
> control panel. Digital Ocean is my preference for hosting and I recommend that you take a look at th

### Rank 4

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

### Rank 5

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

### Manual Evaluation — Vector
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

## Hybrid Retrieval
### Rank 1

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 69

**Content:**

> Explore Flask Documentation, Release 1.0
> Amazon Web Services EC2
> Amazon Web Services is a collection of services provided by ... Amazon! There’s a good chance that you’ve heard
> of them before as they’re probably the most popular choice for new startups these days. The AWS service that we’re
> most concerned with here is EC2, or Elastic Compute Cloud. The big selling point of EC2 is that we get virtual servers
> - or instances as they’re called in AWS parlance - that spin up in seconds. If we need to

### Rank 2

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

### Rank 3

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 69

**Content:**

> • Heroku Postgres
> • Amazon RDS
> Digital Ocean
> Digital Ocean is an EC2 competitor that has recently begun to take off. Like EC2, Digital Ocean lets us spin up virtual
> servers - now called droplets - quickly. All droplets run on SSDs, which isn’t something we get at the lower levels
> of EC2. The biggest selling point for me personally is an interface that is far simpler and easier to use than the AWS
> control panel. Digital Ocean is my preference for hosting and I recommend that you take a look at th

### Rank 4

- Filename: Flask.pdf
- Document ID: 39bb4809-8106-4822-9879-61ce6905c256
- Page: 70

**Content:**

> Explore Flask Documentation, Release 1.0
> 2.13.2 The stack
> This section will cover some of the software that we’ll need to install on our server to serve our Flask application to
> the world. The basic stack is a front server that reverse proxies requests to an application runner that is running our
> Flask app. We’ll usually have a database too, so we’ll talk a little about those options as well.
> Application runner
> The server that we use to run Flask locally when we’re developing our application isn

### Rank 5

- Filename: Python.pdf
- Document ID: fc38bfb7-e987-444c-b769-7718c5060cfc
- Page: 155

**Content:**

> Chapter 14
> Files
> 14.1 Persistence
> Most of the programs we have seen so far are transient in the sense that they run for a short
> time and produce some output, but when they end, their data disappears. If you run the
> program again, it starts with a clean slate.
> Other programs are persistent: they run for a long time (or all the time); they keep at least
> some of their data in permanent storage (a hard drive, for example); and if they shut down
> and restart, they pick up where they left off.
> Examples

### Manual Evaluation — Hybrid
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

# Test Case 20: Empty User: No Results Expected

**Category:** empty_user

**Query:**

> What is Python?

**User:** user_C

**Expected Topic:** No results

**Purpose:**

Verifies graceful handling of user with no indexed documents.

---

## Vector Retrieval
No results.
### Manual Evaluation — Vector
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

## Hybrid Retrieval
No results.
### Manual Evaluation — Hybrid
- Top 1 relevant: Not evaluated
- Top 3 relevant: Not evaluated
- Notes:

---

# Benchmark Summary

## Test Categories

| Category | Number of Tests | Vector Observation | Hybrid Observation |
|---|---:|---|---|
| Exact technical term | 4 | | |
| Keyword / acronym | 3 | | |
| Paraphrased query | 3 | | |
| Conceptual explanation | 3 | | |
| Programming/API terminology | 3 | | |
| Multi-document retrieval | 3 | | |
| Empty user | 1 | | |

# Overall Evaluation

## Vector Retrieval Strengths

_To be completed manually._

## Hybrid Retrieval Strengths

_To be completed manually._

## Failure Cases

_To be completed manually._

## Final Decision

_To be completed after reviewing all test cases._

Possible final decisions may include:

- Keep vector-only retrieval
- Use hybrid retrieval
- Improve hybrid retrieval
- Add reranking later
- Use different strategies depending on query type


What are the commonalities between Kurt Gödel, Johann Sebastian Bach, and Maurits Cornelis Escher?  
  
I don’t know, because that’s not what the book is about. _Gödel, Escher, Bach_ (GEB) is about a deeper topic: how can minds be formed from simple components? How do mental processes arise from non-mental ones?  
  
Many authors might have handled this topic by writing a dry, dense book on the matter. Not Hofstadter. The tagline of the book is “a metaphorical fugue on minds and machines in the spirit of Lewis Carroll”.  
  
Between each chapter is a dialogue between fictional characters (the three main ones are Achilles, the Tortoise, and the Crab), which serves to foreshadow the themes in the following chapter. Each dialogue mirrors the structure of a piece by Bach, though sometimes the link is very tenuous. Works of art by Escher appear frequently, also linked more or less strongly to the subject being discussed.  
  
Hofstadter particularly enjoys having the structure of the dialogue mirror the subject, self-reference, and simply messing with the structure purely for the sake of it.  
  
Perhaps the most impressive example is his “Crab Canon”, which reads (almost) the same when read backwards line by line. In the dialogue, both characters mention works of art with this property, including Bach’s Crab Canon on which the dialogue is based. This acts as a link to the topic of indirect self-reference in formal systems. And if you think this is a lot of layers of metaphor and meaning, Hofstadter pours on another truckload when referencing the dialogue in a later chapter.  
  
Another example is the dialogue “Contracrostipunctus”. The name is a portmanteau of “contrapunctus” and “acrostic”. When the first letter of each paragraph is written down the result is “Hofstadter’s contracrostipunctus acrostically backwards spells J S Bach”, which, acrostically backwards and treating “J S Bach” as one word, gives “J S BACH”.  
  
How did I realize this? Because Hofstadter points it out. There are countless parts in the book where the author says something to the effect of: “Behold! This seemingly arbitrary choice I made earlier actually reveal a deep analogy between these two seemingly disparate subjects, and now I will use this as a springboard to jump to the next topic”. And then the next topic is unfailingly linked in twenty different ways to other topics, and each link is symbolically represented by a Bach and/or Escher piece.  
  
I assume that there are countless things that Hofstadter does not directly point out that I missed while reading. Or maybe there’s the equivalent of a Schwarzschild radius for cleverness and trying to concentrate any more in a single book would make the book collapse into a black hole.  
  
I thought that this aspect of the book would get old by the time I got to the end, but instead I found myself as entertained as ever when the final dialogue included phrase after phrase from the author’s Ridiculously Inventive Collection of Extremely Recursive and Charming Acronyms for Ricercar (a ricercar is similiar to a fugue, and [two](https://www.youtube.com/watch?v=tUcMX0Pqx04) [ricercars](https://www.youtube.com/watch?v=KYouXtuk0T8) form the backbone of Bach’s Musical Offering, which Hofstadter references heavily). This sparkling of word play, self-reference, metaphor, and mini-insights makes the book a great joy to read, while also setting up the groundwork for the book’s heftier insights.  
  
  

### Informal Formal Systems

So what, then, are the heftier insights? The book starts by introducing the concept of formal systems and discussing the connection between formal systems and meaning.  
  
A formal system consists of two things: axioms and rules of inference. Axioms are the strings of symbols that you start with, and rules of inference are the rules for how you are allowed to change a string, split it into other strings, or combine many strings into one.  
  
Most of the time (such as in formal logic), the symbols are taken to mean something, and the object of using the rules of inference to get to other strings is to try to prove that they follow from the axioms of the system.  
  
Strings within a formal system can be divided into categories:  

- Non-well-formed strings. These use the same symbols as the formal language, but they do not make grammatical sense. For instance, “∧))p” makes no sense in the context of formal logic.
-  Well-formed strings. These are grammatically valid.

-  True strings.

-  Decidable true strings: strings that state true things and their truthhood can be determined within the system.

- Axioms: strings that are taken to be true as part of the system.
-  Derived true strings: strings that can be determined to be true by applying the system’s rules of inference to its axioms.

- Undecidable true strings. These strings state true things, but there is no derivation for them within the system and thus they cannot be proved. Guaranteed to exist because of Gödel’s theorems.

- False strings

- Decidable false strings

- Negations of axioms
- Derived false strings

- Undecidable false strings 

These categories are elegantly summed up by one of Hofstadter’s diagrams:  

![](img/godel-escher-bach/Screen+Shot+2018-04-22+at+21.27.55.png)

  
I will not discuss formal systems at great length since GEB does an excellent job of giving the reader a very intuitive understanding of formal systems in a gradual, easy-to-follow manner. The proof of Gödel's theorem given later assumes some familiarity with formal systems, however. If you want to learn more about formal systems, I suggest looking into [first-order logic](https://en.wikipedia.org/wiki/First-order_logic) (also called predicate logic or, less specifically, formal logic) or [Peano arithmetic](https://en.wikipedia.org/wiki/Peano_axioms).  
  
One more thing about formal systems: an important distinction Hofstadter makes is between reasoning inside a system versus outside a system. It might be obvious that a certain theorem can never be reached within the constraints of a formal system, but if we restrict ourselves to thinking only within the system, we can only churn out theorem after theorem.  
  
  

### BlooP to FlooP but not to GlooP

Hofstadter introduces three hypothetical programming languages to illustrate the differences in what can be expressed with different types of recursion: BlooP, FlooP and GlooP.  
  
In BlooP, only bounded loops are allowed (hence the name): whenever the program runs a loop of any kind, the number of times the loop will run has to be known when it is started. A BlooP-compatible factorial function could therefore be written in pseudocode as:  
  
```
define factorial (n):  
   p <– 1  
   for i in range n:  
      p <– n * p  
   return p  
```
  
(Hofstadter gives specific syntax for BlooP, but I feel that modern readers will find Python-esque pseudocode more legible)  
  
However, the following definition of factorials would not be allowed in BlooP:  
  
```
define factorial (n):  
   if n = 1:  
      return 1  
   else:  
      return n * factorial(n - 1)  
```
  
Neither would a function like this:  
  
```
define nextPrimeAfter (n):  
   d <– 1  
   while notAPrime(n + d):  
      d <– d + 1  
   return n + d  
```
  
Why? Because the loops in both examples do not run a predefined number of times. Why does this matter? When writing a factorial function, not being able to write the recursive version above is a mere inconvenience. With nextPrimeAfter, writing a BlooP version would require knowledge of some mathematical tricks (for example, it has been proved that for n > 3, there is always a prime greater than n and smaller than 2n; thus, the number of times you have to loop can be known before the loop is started).  
  
But are all algorithms Bloopable? Or are there programs that cannot be written in BlooP?  
  
Yes. It can be proved (and it is proved, in the book) that there exist algorithms which cannot be expressed in BlooP. For those, we must allow unbounded recursion, such as in the FlooP (Free Loop) language. Both of the unBloopable cases above are perfectly Floopable.  
  
Is there a language, call it GlooP, even more powerful than FlooP? The answer is no. Some programs, such as a program for determining whether another program will halt, have been proved to be impossible (much to the chagrin of programmers trying to stop their programs from freezing because of accidental loops). But if a procedure is possible, it can be written in FlooP.  
  
Hofstadter notes that all widely-used programming languages are equivalent in power to FlooP. This is less because of the ingenuity of their designers and more because unless limits are deliberately placed on a language for didactic purposes, any reasonable programming language can do everything that FlooP can (in theory - some, of course, are far more difficult to work with).  
  
A language for expressing algorithms therefore tends to be capable of expressing all possible algorithms, especially once recursion is allowed.  
  
This fact will come back to haunt us when it comes to formal systems and Gödelian incompleteness.  
  
  

### Incompleteness

The book walks through a proof of Gödel’s incompleteness theorem. It is fascinating enough that I will try to explain it in full.  
  
Gödel’s incompleteness theorems (there are two) are based on two key ideas.  

1.  Gödel numbering. This is simply the process of replacing all characters used in a formal system by numbers. We can completely arbitrarily define, for instance, that “(“ is “10”, “)” is “01”, “p” is “14”, and “∧” is “17”, and then write “1014171401” instead of “(p∧p)”. If, in the formal system we are dealing with, the interpretation of “(p∧p)” is “p is true and p is true”, then “1014171401” has the exact same interpretation. Thus, all statements, axioms, or even derivations within a formal system can be written as a single number (most of the time, a ridiculously large number, but what matters is that it is theoretically possible).
2.  If we have a formal system for arithmetic, Gödel numbering means that we can convert statements of that formal system into numbers. Furthermore, we can convert the rules of that formal system into (very complex) arithmetic operations. What this means is that the formal system can talk about itself.

Self-reference opens the door to a whole host of potential paradoxes. Can the statement “this statement is false” be made within F?  
  
Unfortunately, or perhaps fortunately, a formal system like Hofstadter’s TNT (Typographical Number Theory, based on Peano arithmetic) cannot encode a paradox as simple as “this statement is false”, since the property of a statement being “true” in TNT (or any other comparable system) cannot be stated in a Bloopable form, and it turns out that TNT can only express Bloopable properties.  
  
(For more on TNT, see the [Wikipedia article](https://en.wikipedia.org/wiki/Typographical_Number_Theory). For the purposes of this proof, it is sufficient to know that TNT statements can express arithmetic operations, contain variables, and be qualified with "there exists an X such that [statement]" or "for all X, [statement]")  
  
So the question is: is there a way in which TNT can be forced to say something paradoxical about itself and thus be proved incomplete?  
  
We might not be able to write a test in TNT for whether or not a TNT statement is true, but we can check the validity of a proof. For instance, an algorithm for checking a proof might be as follows:  

- For each line L in the proof (extracted by splitting the proof's Gödel number at each line break symbol):
  - If L is not an axiom:
    - For all pairs of prior statements S in the proof:
      - For all rules of inference $R$:
        - Does applying rule $R$ to one or both of $S$ result in $L$ (“one or both” because some rules will be about combining statements, others about modifying single statements)? This can be tested in TNT because when dealing with the Gödel numbers of statements, all rules for shuffling the symbols of those statements can be expressed as arithmetic operations, which is what TNT is all about.  
  
If each line is either an axiom or the result of applying one of the (finite) rules of TNT to the lines that come above it, and the last line of the derivation is $S$, then we can conclude that the derivation $P$ is a valid proof of $S$ and $S$ is a theorem of TNT.  
  
There are no unbounded loops, so therefore it is expressible in BlooP and therefore TNT (though the TNT expression will be enormous). And since it is an expression of TNT, there is an (even larger) Gödel number that corresponds to it.  
  
What we have now shown is that there exists a number which, when interpreted as a Gödel number of TNT, expresses a statement for checking whether another Gödel number is a valid proof for a third Gödel number. Call this statement $\text{TNT-PROOF}\{A,B\}$, where $A$ is a free variable for the Gödel number of the proof and $B$ a free variable for the Gödel number of the statement. For any value of $A$ and $B$, this statement will yield either true or false.  
  
Therefore we can write the sentence “there exists a number $A$ such that $A$ is the Gödel number of the derivation of statement $S$” as $\exists A:\text{TNT-PROOF}\{A,S\}$. This is equivalent to saying "there exists a way to derive $S$ within TNT" - all within the strict confines of TNT!  
  
The final trick is related to a process Hofstadter calls “quining” after its inventor Willard Van Orman Quine. An example in English given in the book is the following paradox: “‘yields a falsehood when preceded by its own quotation’ yields a falsehood when preceded by its own quotation”. This is the fundamental structure behind the TNT statement that results in the proof of Gödel's theorem.  
  
The general idea is to substitute the value of a string into some place inside the string. To “arithmoquine” is an implementation of quining inside TNT: take the Gödel number of sentence $S$, and substitute that in place of a free variable in $S$. Testing whether or not one number is the arithmoquinification of another is BlooPable and therefore expressible TNT; we will call the function that checks whether $Y$ is the result of substituting the Gödel number of $X$ into the place of the free variable in $X$ $\text{ARITHMOQUINE}\{X,Y\}$.  
  
We are now ready to introduce a statement (call it $U$):  
  

$$
U \equiv \neg \exists A: \exists B: (\text{TNT-PROOF}\{A,B\} \land \text{ARITHMOQUINE}\{C,B\})
$$

  
  
What this sentence means is:  
  
> _There does not exist a number $A$ such that there exists another number $B$ such that:_  

> - _$A$ is the Gödel number of a valid derivation of $B$ ($\text{TNT-PROOF}\{A,B\}$)_, AND
> - _$B$ is the arithmoquinification of $C$ ($\text{ARITHMOQUINE}\{C,B\}$)_

  
$U$ has exactly one free variable (C), so it can be arithmoquined. To do this, we take the Gödel number of $U$ (call it $N$), and replace $C$ with $N$ to yield sentence $G$:  
  

$$
G \equiv \neg \exists A: \exists B: (\text{TNT-PROOF}\{A,B\} \land \text{ARITHMOQUINE}\{N,B\})
$$

  
  
$G$, the infamous Gödel’s string, has the following meaning:  
  
> _There does not exist an $A$ such that there exists another number $B$ such that:_  

> - _$A$ is the Gödel number of a valid derivation of $B$_, AND
> - _$B$ is the arithmoquinification of $N$_

  
Since it is guaranteed that $N$ has an arithmoquinification (it has one free variable), the interpretation can be rephrased as:  

> _There is no number $A$ such that $A$ is the Gödel number of a valid derivation of the arithmoquinification of $N$_  
  
But what is the arithmoqunification of $N$? It is Gödel’s string, $G$! So we can further simplify our interpretation as:  

> _There is no number $A$ such that $A$ is the Gödel number of a valid derivation of $G$_  
  
In other words, $G$ says that there does not exist a derivation of $G$ in TNT. If there is no derivation of it, it cannot be a theorem of TNT.  
  
Using the concepts of Gödel numbering and arithmoquinification, we created a sentence of TNT which says “this sentence is unprovable in TNT”. Alright, but why should we listen to this sentence? We can make a sentence in TNT to say anything (about numbers) that we want, but that does not mean that 1 = 2.  
  
So let’s step back from Gödel’s string. Is it a theorem of TNT? If $G$ is a theorem, then what $G$ says must be true, and $G$ says that $G$ is not a theorem.  
  
At first glance, this seems just as paradoxical as “this statement is false”. But we’ve only considered the case that $G$ is a theorem - what if it isn’t?  
  
If $G$ is not a theorem, then there is no contradiction: $G$ says “I am not a theorem”, and it is not. Thus, we are forced to accept that $G$ is a true statement, but it is not a theorem: there cannot exist a chain of proof that starts from TNT’s axioms, proceeds by TNT’s rules of inference, and arrives at $G$.  
  
What Gödel’s incompleteness theorem (or, more precisely, Gödel’s first incompleteness theorem) shows is that within the framework of Typographical Number Theory (or any other framework equivalent to Peano arithmetic), there are statements of the formal system that cannot be proved to be true, even if they actually are true.  
  
Why the focus on formal systems of arithmetic? So what if certain extremely complex properties of numbers cannot be proved with only a handful of axioms and inference rules?  
  
It turns out that any formal system complex enough to embed arithmetic (and therefore complex enough to express all Bloopable properties) is vulnerable to Gödel’s proof. This is because Gödel numbering can be used to convert a statement in any formal system into a number, and because all formal rules for manipulating these numbers can then be expressed as arithmetic properties. Any sufficiently complex formal system can be written in terms of TNT, and has unprovable truths because of the possibility of self-reference.  
  
  
  

### Applying Gödel: Landscapes and Machines

What if we add Gödel’s string as an axiom of TNT? It wouldn’t help, since it would be possible to construct a sentence that has the same function in the new TNT as G has in standard TNT. It would, however, imply the existence of a class of numbers that Hofstadter terms “supernaturals”, which would have a whole bunch of interesting properties.  
  
But are they real? This begs the question of whether imaginary numbers are real, or whether natural numbers are real, or even whether real numbers are real. Hofstadter points out that choosing which mathematical system to use requires “stepping out” of the mathematical framework and making a judgement about what is applicable to the problem at hand. New number systems will not wreck the banking industry since imaginary numbers, for instance, are not applicable to reasoning about financial systems (despite what many might wish).  
  
At the beginning of the 20th century, there was a movement in mathematics, lead by David Hilbert, to find a set of central axioms and rules of inference from which all of mathematics could be derived. Gödel’s theorem ruined this dream, saying that no matter what the axioms and rules, there will always be unprovable truths. New axioms, and therefore new systems and concepts, will always be needed. I think one of the broader insights here, one which Hofstadter seems to hint at, is a view of mathematics not as a single, godly machine spitting out all truths, but instead as a landscape of overlapping regions, each applicable in different circumstances and with their own local rules, customs, and terrains.  
  
  

### Applying Gödel: Machine Intelligence?

When scientific or mathematical results become famous, there is a tendency for its conclusions to go through a game of “Telephone”. Examples include how the theory of relativity has been interpreted as a statement about how everything is relative, and probably most of what is written about quantum mechanics. Gödel’s incompleteness theorem is no exception: “sufficiently complex formal systems imply truths which cannot be proved within the system itself” easily morphs into far less precise statements.  
  
Hofstadter, who was already working on artificial intelligence in the 1970s, takes some time to refute the idea that Gödel’s theorem refutes the idea of AI. Why would this be the case? To quote Hofstadter quoting J. R. Lucas:  

> _However complicated a machine we construct, it will, if it is a machine, correspond to a formal system, which in turn will be liable to the Gödel procedure for finding a formula unprovable-in-that-system. This formula the machine will be unable to produce as being true, although a mind can see it is true. And so the machine will still not be an adequate model of the mind. We are trying to produce a model of the mind which is mechanical-which is essentially "dead"-but the mind, being in fact "alive," can always go one better than any formal, ossified, dead system can. Thanks to Gödel’s theorem. the mind always has the last word._

Hofstadter argues against this interpretation from various angles at some length, but acknowledges that C. H. Whitely might have done it best by inventing the sentence: “Lucas cannot consistently assert this sentence”. The statement is true, Lucas cannot assert it without being inconsistent, and the information we gain about his mind is zero.  
  
What, then, is the relevance of Gödel’s theorem to the central question of minds? It is not so much an “answer” as a fundamental fact about sufficiently complex formal systems that comes up in many contexts.  
  
For example, Hofstadter makes an analogy between formal systems and an idealized version of DNA replication. The equivalent of Gödel’s theorem within this framework is that for every cell (formal system) there exists a strand of DNA (a string of that formal system) that is unreproducible (cannot be proved) within that cell.  
  
  

### Gödel, Escher, Bach: An Eternal Giant Book

At the start of the review, I mentioned that primary topic of GEB is how minds can arise out of simpler pieces. I then went on to talk for over 3000 words about formal systems, their incompleteness, and Floopability.  
  
Where is the answer to the book’s central question? How do countless disparate topics come together into a unified whole that answers the question of how countless disparate components come together into a unified whole that can think and reason?  
  
A common complaint about GEB is that it spends 800 pages saying what could be condensed into 300. And it is true: if you take the essence of everything Hofstadter says, it boils down to maybe 300 pages. 300 pages, that is, of dry, dense material.  
  
But the book is not about the exact mechanisms of how minds work, or how to build an AI, but more about the general flavor of what systems any intelligent being will have in common.  Where GEB shines is its ability to explore these topics in a way that makes the conclusions seem natural and intuitive: you can know as a fact that mental activity comes down to the firing of unconscious neurons, but that is not the same as having an intuition of how this might happen.  
  
  

### Self-Referential Offering

I will conclude with an attempt to distill some of GEB’s main points into a few paragraphs. This is less of a summary and more of an attempt to separate one voice from GEB’s metaphorical fugue.  
  
Self-reference is an inherently dangerous business, yet also extremely hard to avoid in any formal system or language worth talking about. What often results are what Hofstadter calls “strange loops”, in which different layers of meaning interact in a surprising way. Because of this, there is a fundamental tendency of any complex reasoning system, whether mathematics or brains, to be in some sense incomplete, messy, and non-linear (this has shades of chaos theory, but hopefully the dinosaurs won’t escape).  
  
Hofstadter proposes that consciousness, and other “emergent” phenomenon in brains, are the result of the interaction of different levels in strange and complex ways.  
  
Is this an anti-reductionist position? No. As Hofstadter explains: ”In principle, I have no doubt that a totally reductionistic but incomprehensible explanation of the brain exists; the problem is how to translate it into a language we ourselves can fathom."  
  
The power of GEB is that it shows the beauty of this view.
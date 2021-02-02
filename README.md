# Minimum-Edit-Distance
A program that determines the minimum number of operations (edit, insert or substitute) between two strings

Much of natural language processing is concerned with measuring how similar two strings are. For example in spelling correction, the user typed some erroneous
string—let’s say graffe–and we want to know what the user meant. The user probably intended a word that is similar to graffe. Among candidate similar words,
the word giraffe, which differs by only one letter from graffe, seems intuitively to be more similar than, say grail or graf, which differ in more letters.

Edit distance gives us a way to quantify both of these intuitions about string simminimum edit distance ilarity. More formally, the minimum edit distance between two strings is defined
as the minimum number of editing operations (operations like insertion, deletion,
substitution) needed to transform one string into another.

The program calculates the minimum number of edits(insertions, deletions and substitutions between two strings using Lavenshtein's approach.
We assume the version of Levenshtein distance in which the insertions and deletions each have a cost of 1 (ins-cost(·) = del-cost(·) = 1), and substitutions have a
cost of 2 (except substitution of identical letters have zero cost).

# Parser-Comprehensive-Construction

 Parser, Scope, and Type Checking

** ****ONGOING**** **

An extension of [Parser-Building](https://github.com/zbl5332/Parser-Building) where it built a Lexer and Parser. 

Focusing on adding scope and symbol table management, as well as type checking. 

**The main aspects to consider are:**

* Variable Declaration Before Use: Variables must be declared before they are used.

* Type Consistency: Expressions cannot involve variables or values of different types. For example, 
	if int x = 5 and float z = y, you can not add x and z.

* Unique Variable Names in Scope: Variables must have unique names within the same scope.


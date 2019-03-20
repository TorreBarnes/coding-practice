# cis301-fall2018

## Koans Assignment

Project 2 - Koans

A koan is a “teaching question” that is used in Buddhist discourse that seeks to provide deep insight into a problem. While the answer to a koan can be subtle, they are not meant to be tricky like a puzzle is. Koans have correct answers, but the intention of working through a koan is to understand its deeper meaning. To gain a better understanding of the Java programming language, you will work through a series of Java koans during the first half of this course. Each koan is a small piece of code (about the size of a unit test) that demonstrates a particular feature or aspect of the Java language or API. The koans were originally authored by Mat Bentley and can found in their original form at https://github.com/matyb/java-koans

Similar to project1, you need to clone a copy to your own repository by clicking on this link:
https://classroom.github.com/a/_xUprayY

Once you clone your repository, you will be able to look at the readme of your repository under java-koans folder. 

There 3 steps in this process:
Develop and solve each koan:
	You need to import your project into an IDE (i.e. intellij) and start developing from beginner to intermediate and then advanced problems. 
Test your work:
Open a terminal and go to the directory in which the koans dir is located. Now execute run.bat for windows and run.sh for OSx and Linux.
      3. Every time you solve a problem set you will commit your work to your github account.   

### Java Koans
Build Status

#### __Running Instructions:__
Download and unarchive the contents of the most recent java-koans in development from: https://github.com/matyb/java-koans/archive/master.zip

Open a terminal and cd to the directory you unarchived: cd <the directory you just unarchived>

Within it you'll find:
koans: this directory contains the application and its lessons, it is all that is needed to advance through the koans themselves and it can be distributed independently

#### lib: this directory contains the code the koans engine is comprised of and built with

#### gradle: wrapper for build library used to build koans source, setup project files in eclipse/idea, run tests, etc. you probably don't need to touch anything in here

#### Change directory to the koans directory: cd koans
If you are using windows enter: run.bat or ./run.sh if you are using Mac or Linux

#### __Developing a Koan:__
Follow any of the existing koans as an example to create a new class with koan methods (indicated by the @Koan annotation, they're public and specify no arguments)
Define the order the koan suite (if it's new) will run in the koans/app/config/PathToEnlightenment.xml file
Override the lesson text when it fails (default is expected 'X' found 'Y')
Optionally you may use dynamic content in your lesson, examples are located in the XmlVariableInjector class (and Test) and the AboutKoans.java file

#### __Something's wrong:__
If the koans app is constantly timing out compiling a koan, your computer may be too slow to compile the koan classes with the default timeout value. Update the compile_timeout_in_ms property in koans/app/config/config.properties with a larger value and try again.

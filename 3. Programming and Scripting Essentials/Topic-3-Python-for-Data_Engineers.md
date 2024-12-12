# Topic 3 - Python for data engineers - 12/12/2024

TO Check!
Apply task - can't get into into it 
Linux course not completing
  
## Introduction to the Software Development Lifecycle

### Software development lifecycle SDLC

**Planning**
- **Definition**: This initial phase involves defining the scope and purpose of the project, identifying stakeholders, and setting objectives.

- **Examples**: Gathering requirements from clients, defining project timelines, and resource allocation.

- **Role of Data Engineering**: Data engineers may be involved in assessing data needs, understanding data sources, and planning for data integration and storage solutions.

**Analysis**
- **Definition**: During the analysis phase, detailed requirements are gathered and analysed to create a comprehensive project specification.

- **Examples**: Conducting feasibility studies, defining functional and non-functional requirements.

- **Role of Data Engineering**: Data engineers analyse data requirements, ensure data quality, and design data models that meet the project needs.
  
**Design**
- **Definition**: The design phase focuses on creating the architecture and detailed design of the software based on the requirements gathered.

- **Examples**: System architecture design, user interface design, database schema design.

- **Role of Data Engineering**: Data engineers design the data architecture, including database schemas, ETL (Extract, Transform, Load) processes, and data pipelines.

**Development**
- **Definition**: In this phase, actual coding takes place. Developers write the code to implement the designed functionalities.

- **Examples**: Writing code, developing algorithms, creating user interfaces.

- **Role of Data Engineering**: Data engineers develop the data infrastructure, implement ETL processes, and create data pipelines to ensure data flows smoothly across the system.

**Testing**
- **Definition**: The testing phase involves verifying that the software works as intended and identifying any defects.

- **Examples**: Unit testing, integration testing, system testing, user acceptance testing.

- **Role of Data Engineering**: Data engineers test data flows, validate data accuracy and integrity, and ensure that data processing meets performance requirements.

**Deployment**
- **Definition**: Once testing is complete, the software is deployed to a production environment where it becomes available to users.

- **Examples**: Once testing is complete, the software is deployed to a production environment where it becomes available to users.

- **Role of Data Engineering**: Data engineers ensure that data systems are correctly deployed, migrate data if necessary, and verify that data systems are operational in the production environment.

## Introduction to Python basics
Did you know that Python's simple and readable syntax has made it one of the most popular programming languages, used by tech giants like Google and NASA? Understanding the basics of Python can open doors to a wide range of applications in web development, data science, artificial intelligence, and more. This lesson will cover essential Python concepts such as syntax, variables, functions, reserved keywords, program structure, control flow, recursion, and functions. The illustration below outlines the features provided by Python:

![python features](https://media.licdn.com/dms/image/D4D12AQHEHLbwo8rdSg/article-cover_image-shrink_600_2000/0/1673251056920?e=2147483647&v=beta&t=EgmtXW_H_GGYom-GgMYY-30Gul3U0jKFBAYmFUnyy84)

Python’s simplicity and flexibility make it an excellent choice for a wide range of applications, from web development to data science and artificial intelligence. 

Its clean syntax and dynamic typing allow for rapid development and prototyping, while its powerful features like functions and control flow structures enable the creation of complex, interactive programs.

**Syntax**
Syntax refers to the set of rules that defines the combinations of symbols considered correctly structured programs in a programming language. In Python, syntax is designed to be easy to read and write, making it an excellent choice for beginners and experienced programmers alike. For instance, unlike some other programming languages, Python uses indentation to define code blocks rather than braces or keywords, which enhances readability. 

**Variables**
Variables are used to store data that can be referenced and manipulated in a program. In Python, you do not need to declare a variable before using it, and the variable's type is determined automatically at runtime. This flexibility allows for rapid development and prototyping.

**Functions**
Functions are reusable blocks of code that perform a specific task. They help in organising code, making it modular, and avoiding repetition. Defining a function in Python is straightforward using the def keyword, followed by the function name and parentheses.

**Reserved keywords**
Reserved keywords are special words that are part of the Python language syntax and have specific meanings. They cannot be used as identifiers such as variable names, function names, or any other user-defined item.

![python reserved keywords](https://waytoeasylearn.com/storage/2024/05/Python-Keywords.png.webp)

**Program structure**
The structure of a Python program refers to how the code is organised and written, ensuring it is clean, understandable, and maintainable. Python relies on indentation to define code blocks, which is critical for readability and functionality. Consistent indentation is not just a matter of style but a syntactic requirement. Additionally, comments are used to explain code, making it easier to understand and maintain. 

![python program structure](https://images.wondershare.com/edrawmax/articles2024/input-output-algorithm-maker/understanding-the-fundamentals-basic-structure-of-c-programs-02.jpg)

**Control flow**
Control flow refers to the order in which individual statements, instructions, or function calls are executed or evaluated in a Python program. Control flow structures include conditional statements and loops, which allow for decision-making and the repetitive execution of code. Conditional statements like if, elif, and else are used to execute code based on specific conditions.

![python control flow](https://pynative.com/wp-content/uploads/2021/03/python-flow-control-statements.png)

**Recursion**
*Function calling itself iteratively*
Recursion is a technique where a function calls itself to solve a problem. Each recursive call reduces the problem size, bringing it closer to a base case, which stops the recursion. Recursion can simplify the solution of complex problems by breaking them down into simpler sub-problems.

*A factorial is a mathematical function that multiplies a number by every number that comes before it, down to one*
![python recursion](https://cdn.programiz.com/sites/tutorial2program/files/python-factorial-function.png)

For Example:
You could do a normal loop to count steps. Or a recursive method that runs the function itself. This is good for complex processes like the above factorial example.

# ITERATIVE
def walk(steps):
  for step in range(1, steps + 1):
    print(f"You take step #{step}")

# RECURSIVE
def walk(steps):
  if steps == 0: # don't need negative steps
    return # stops the loop if it hits 0
  walk(steps - 1)
  print(f"You take step #{step}")

walk(100) will show
You take step 100
You take step 99 etc down to 0

But the important bit is, it's actually running a function everytime
walk(100)
walk(99)
walk(98) etc

There is a limit to how many recursions you can run

**For a factorial** 
*A factorial is a mathematical function that multiplies a number by every number that comes before it, down to one*
# ITERATIVE
def factorial(x):
  result = 1
  if x > 0:
    for y in range(1, x + 1):
      result *= y
    return result

# RECURSIVE
def factorial(x):
  if x == 1:
    return 1 # stops recursion loop
  else:
    return x * factorial(x)

print(factorial(10))

*the code here is much easier to write but the drawback is it runs a bit slower*

**A basic example**
def countdown(n): 
  if n == 0: 
    print("Blast off!") 
  else: 
    print(n) 
    countdown(n - 1)

countdown(5)

## Introduction to test-driven development TTD
Did you know that test-driven development (TDD) can significantly reduce the number of bugs in your code, improving overall software quality and developer productivity? Many leading tech companies, including IBM and Microsoft, use TDD to ensure their software meets the highest standards. This lesson will explore the benefits of TDD, providing you with a comprehensive understanding of why this approach is favoured in modern software development.

Test-driven development (TDD) is a software development approach where tests are written before the actual code. This method involves writing a test for a specific function or feature, running the test to see it fails (since the feature isn't implemented yet), writing the minimum amount of code to pass the test, and then refactoring the code while keeping the tests green (passing). This cycle is often referred to as the Red-Green-Refactor cycle, as follows:

- Red: Write a test that fails because the feature is not yet implemented
- Green: Write just enough code to make the test pass
- Refactor: Improve the code while ensuring that all tests still pass

![test driven development](https://www.zealousys.com/wp-content/uploads/2023/09/Steps-to-Implementing-Test-Driven-Development.png)

### The benefits of Test Driven Development 

**Improved code quality**

- **Definition**: TDD encourages writing code that is clean, efficient, and free of defects.
- **Examples**: By writing tests first, developers are forced to consider edge cases and potential issues early on. This leads to more robust and reliable code.
- **Details**: Tests serve as a form of documentation, making it easier for other developers to understand the code. Additionally, the need to write tests often leads to simpler, more modular code that is easier to maintain and extend.

**Enhanced productivity**

- **Definition**: TDD can streamline the development process, allowing for faster and more confident coding.
- **Examples**: Developers can focus on one small piece of functionality at a time, leading to steady progress and reducing the likelihood of getting stuck on complex problems.
- **Details**: Automated tests provide immediate feedback, helping developers quickly identify and fix bugs. This reduces the time spent on debugging and allows for more efficient use of development time.

**Better test coverage**

- **Definition**: TDD ensures that all features of the code are tested, leading to comprehensive test coverage.
- **Examples**: By writing tests for every new feature before implementation, developers ensure that each part of the codebase is covered by tests.
- **Details**: TDD mandates tests before coding, enhancing coverage, reducing bugs, and aiding refactoring by detecting regressions. 

**Facilitates refactoring**

- **Definition**: With a suite of tests in place, developers can refactor code with confidence, knowing that any errors introduced will be quickly detected.
- **Examples**: Refactoring can improve code readability, reduce complexity, and enhance performance without altering the code's functionality.
- **Details**: Tests safeguard functionality, promote continuous code improvement, and enhance software scalability and maintainability. 

**Clear documentation**

- **Definition**: Tests serve as live documentation that describes how the code is supposed to behave.
- **Examples**: Instead of sifting through outdated or incomplete documentation, developers can look at the tests to understand the intended behaviour of the code.
- **Details**: This documentation, always synced with the code, simplifies onboarding for new developers and code review for existing ones. 








## Lecture Notes

## Topic 3 Reflections
Try and design our definition of done to reflect the SDCL.
Introduce Test driven development 






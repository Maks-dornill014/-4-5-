class ProgrammingLanguage:
    def __init__(self, name):
        
        self.name = name

    def greet(self):
        
        return f"Привіт! Я — {self.name}, мова програмування."


# Підклас для Python
class PythonLanguage(ProgrammingLanguage):
    def __init__(self):
        
        super().__init__("Python")

    def unique_feature(self):
        
        return "Я чудово підходжу для розробки штучного інтелекту, веб-додатків та автоматизації."


# Підклас для Java
class JavaLanguage(ProgrammingLanguage):
    def __init__(self):
       
        super().__init__("Java")

    def unique_feature(self):
        
        return "Я широко використовуюсь у корпоративних рішеннях і є кросплатформною завдяки JVM."


# Підклас для JavaScript
class JavaScriptLanguage(ProgrammingLanguage):
    def __init__(self):
        
        super().__init__("JavaScript")

    def unique_feature(self):
        
        return "Я основна мова для розробки веб-інтерфейсів і працюю безпосередньо в браузері."



python = PythonLanguage()
print(python.greet())
print(python.unique_feature())

java = JavaLanguage()
print(java.greet())
print(java.unique_feature())

javascript = JavaScriptLanguage()
print(javascript.greet())
print(javascript.unique_feature())

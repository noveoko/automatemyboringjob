
class MyCustomException(Exception):
    def __init__(self, message="A custom exception occurred"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"
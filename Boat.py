class Boat:
    def __init__(self, model, availability):
        self.model=model
        self.availability=availability
    
    def is_available(self):
        return self.availability
    
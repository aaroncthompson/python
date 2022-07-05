"""Currently unimplemented - I don't actually think it serves us to use these right now."""

class Item():
    """An item belonging to our library, which can be checked in and out."""

    def __init__(self, title, author, year):
        """Initialize title and author attributes."""
        self.title = title
        self.author = author
        self.year = year

    def check_out(self):
        """Check the item out."""
        print(f"{self.title.title()} has been checked out. Enjoy!")

    def check_in(self):
        """Check the item in."""
        print(f"{self.title.title()} has been checked in. Thanks!")

class Book(Item):
    """Text media belonging to our library."""

    def __init__(self, title, author, year):
        """Initialize attributes."""
        super().__init__(title, author, year)

class Video(Item):
    """Video media belonging to our library."""

    def __init__(self, title, author, year):
        """Initialize attributes."""
        super().__init__(title, author, year)

class Audio(Item):
    """Audio media belonging to our library."""

    def __init__(self, title, author, year):
        """Initialize attributes."""
        super().__init__(title, author, year)

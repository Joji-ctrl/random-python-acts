class Book:
    title = ''
    author = ''
    rating = []
    rating2 = []
    

    def add_rating(self):
        for i in range(3):
            rating = input("Enter rating: ")
            rating = int(rating)
            self.rating.append(rating)

    def add_rating2(self):
        for i in range(3):
            rating = input("Enter rating: ")
            rating = int(rating)
            self.rating2.append(rating)

    def calculate_average_rating(self):
        sum = self.rating[0] + self.rating[1] + self.rating[2]
        average = sum/3
        print ("Average Rating: " , average)

    def display_info(self):
        print(f"Title: {self.title} Author: {self.author} ")


book1 = Book()
book2 = Book()

book1.title = input("Enter the title: ")
book1.author = input("Enter the author: ")
book1.add_rating()


book2.title = input("Enter the title: ")
book2.author = input("Enter the author: ")
book2.add_rating2()

book1.display_info()
book1.calculate_average_rating()
book2.display_info()
book2.calculate_average_rating()
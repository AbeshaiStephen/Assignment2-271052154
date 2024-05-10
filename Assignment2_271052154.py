from datetime import datetime, timedelta, time
import time
import pickle

class SystemAdministrator:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def decideMovies(self, cinema):
        cinema.show_details()
        cinema.addMovies("Mission Impossible", timedelta(hours=2.5), 500)
        cinema.addMovies("The Dark Knight", timedelta(hours=2.5), 200)
        cinema.addMovies("Inception", timedelta(hours=2.5), 400)
        cinema.addMovies("Avengers: Endgame", timedelta(hours=2.5), 500)
        print(cinema.movies)

class Movies:
    def __init__(self, title, totaltime, no_ofseats):
        self.title = title
        self.totaltime = totaltime
        self.no_ofseats = no_ofseats

    def gettitle(self):
        return self.title

    def get_totaltime(self):
        return self.totaltime

    def get_no_ofseats(self):
        return self.no_ofseats

    def reduce_seats(self, num_seats):
        self.no_ofseats -= num_seats


class Cinema:
    def __init__(self, name, screens):
        self.name = name
        self.screens = screens
        self.cine = []
        self.movies = []

    def show_details(self):
        print(f"*{self.name} cinema has {self.screens} screens*")

    def add_screen(self, screen: int):
        self.cine.append(screen)
        print("NEW SCREEN!!!")
        self.screens = screen + self.screens

    def addMovies(self, title, totaltime, no_ofseats):
        m = Movies(title, totaltime, no_ofseats)
        self.movies.append(m)

    def displayMovies(self):
        print("Movies in the cinema:")
        for movie in self.movies:
            print(movie.gettitle())

    def book_ticket(self, movie_title, num_seats):
        found = False
        for movie in self.movies:
            if movie.gettitle() == movie_title:
                found = True
                if movie.get_no_ofseats() >= num_seats:
                    movie.reduce_seats(num_seats)
                    print(f"Booking successful! {num_seats} seats booked for {movie_title}.")
                    print("Receipt:")
                    print(f"Movie: {movie_title}")
                    print(f"Number of seats booked: {num_seats}")
                else:
                    print("Not enough seats available.")
                break
        if not found:
            print("Invalid movie title.")


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def book_ticket(self, cinema):
        cinema.displayMovies()
        movie_titles = [movie.gettitle() for movie in cinema.movies]
        movie_title = input("Enter the movie title you want to book: ")
        print(cinema.movies)
        
        if movie_title in movie_titles:
            num_seats = int(input("Enter the number of seats you want to book: "))
            cinema.book_ticket(movie_title, num_seats)
        else:
            print("Invalid movie title.")

def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    # You may have a dictionary to store user credentials and roles
    users = {
        "user@example.com": {"password": "xyz", "role": "user"},
        "admin@example.com": {"password": "123", "role": "admin"}
    }
    if email in users and users[email]["password"] == password:
        return users[email]["role"]
    else:
        print("Invalid email or password.")
        return None

def operatemovie(cinema):
    while True:
        current_time = datetime.now().time()
        current_hour = current_time.hour
        if 10 <= current_hour < 13 and len(cinema.movies) > 0:
            movie_title = cinema.movies[0].gettitle()
        elif 13 <= current_hour < 16 and len(cinema.movies) > 1:
            movie_title = cinema.movies[1].gettitle()
        elif 16 <= current_hour < 19 and len(cinema.movies) > 2:
            movie_title = cinema.movies[2].gettitle()
        elif 19 <= current_hour <= 22 and len(cinema.movies) > 3:
            movie_title = cinema.movies[3].gettitle()
        else:
            movie_title = "Cinema closed!!!"
        
        print(f"{movie_title} is running now")
        inpTObreak=input("Enter x to return to log in")

        if inpTObreak=='x':
            break

        time.sleep(10)



def main(cinema_instance):
    role = login()

    if role == "user":
        user = User("User", "user@example.com", "xyz")
        user.book_ticket(cinema_instance)

    elif role == "admin":
        admin = SystemAdministrator("Admin Name", "admin@example.com", "123")
        admin.decideMovies(cinema_instance)
        operatemovie(cinema_instance)

    else:
        print("You are not authorized to access the system.")

cinema_instance = Cinema("Cue Cinema", 4)

#pickle-work down,logical code up

def save_cinema_instance(cinema_instance):
    with open('cinema_instance.pickle', 'wb') as f:
        pickle.dump(cinema_instance, f)

def load_cinema_instance():
    try:
        with open('cinema_instance.pickle', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None

cinema_instance = load_cinema_instance()
if cinema_instance is None:
    cinema_instance = Cinema("Cue Cinema", 4)

while True:
    main(cinema_instance)
    save_cinema_instance(cinema_instance)

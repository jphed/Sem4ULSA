#movies list Jorge Parra Hidalgo - ITIT 13104

movies = [
    "Inception",
    "The Shawshank Redemption",
    "The Godfather",
    "The Dark Knight",
    "Pulp Fiction",
    "Forrest Gump",
    "The Matrix",
    "Titanic",
    "Star Wars: Episode IV - A New Hope",
    "The Lord of the Rings: The Fellowship of the Ring"
]

def list_movies():
    c = 0
    print("List of Movies")
    print("-------------")
    for movie in movies:
        print(f"{c + 1}.- {movie}")
        c += 1
    print("-------------")
    main()

def add_movie():
    movie = input("Enter the name of the movie: ")
    movies.append(movie)
    print("Movie added successfully")
    main()

def delete_movie():
    movie = int(input("Enter the number of the movie to delete: "))
    if movie > len(movies) or movie < 1:
        print("Invalid movie number")
    else:
        movies.pop(movie - 1)
        print("Movie deleted successfully")
    
    main()

def exit_program():
    print("Goodbye!")
    exit()

#Command menu
def main():
    print("1. List Movies")
    print("2. Add Movie")
    print("3. Delete Movie")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        list_movies()
    elif choice == 2:
        add_movie()
    elif choice == 3:
        delete_movie()
    elif choice == 4:
        exit_program()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
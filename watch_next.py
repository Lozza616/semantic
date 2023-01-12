import spacy

nlp = spacy.load('en_core_web_md')
hulk_movie = nlp("""Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.""")


# Defines function
def movie_comparison(movie_description):
    movies = []
    # Opens movie.txt file in read mode
    with open('movies.txt', 'r') as movie_file:
        # iterates thorough each line of movie.txt file stores
        for line in movie_file:
            # Removes new line special character
            s_line = line.replace("\n", "")
            # Stores each line in the movies list
            movies.append(nlp(s_line))
    similaritys = []
    # iterates through the movies list
    for movie in movies:
        # Finds similarity between movie and input movie_description and stores in similaritys list.
        similaritys.append(movie_description.similarity(movie))
    # Finds the highest similarity in the list, stores in variable
    max_similarity = max(similaritys)
    # Iterate through movies list.
    for moviee in movies:
        # finds the similarity
        movie_similarity = movie_description.similarity(moviee)
        # If the similarity is equal to the max similarity
        if movie_similarity == max_similarity:
            # Print the return movie title
            return moviee[0:2]


Most_similar_movie = movie_comparison(hulk_movie)

print(Most_similar_movie)

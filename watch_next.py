#--IMPORT LIBRARIES--
import spacy

nlp = spacy.load("en_core_web_md")

#--FUNCTION TO FIND SIMILAR MOVIE--
def find_similar_movie(input_description, input_file):
    #load input file
    with open(input_file, "r") as f:
        movies = f.readlines()

    #calculate similarity between input description and each movie description
    max_score = 0
    best_movie = ""
    for movie in movies:
        title, description = movie.strip().split(":")
        score = nlp(input_description).similarity(nlp(description))
        if score > max_score:
            max_score = score
            best_movie = title.strip()

    #return title of most similar movie
    return best_movie

#--EXAMPLE USAGE SECTION--
input_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
input_file = "movies.txt"
similar_movie = find_similar_movie(input_description, input_file)
print(similar_movie)
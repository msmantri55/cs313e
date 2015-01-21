# ---------------------------
# project repos/cs313e-netflix/RunNetflix.py
# CS313E - Elements of Software Design
# Parth H. Patel
# php274
# Daniel Croy
# dsc986
# ---------------------------

# -------------
# imports
# -------------

import ast


# -------------
# rmse
# -------------

def rmse(w, a, p):
    """
    w is a writer

    a and p are lists of equal length
    
    Both contain ratings, one with given 
    ratings and the other with the predictions
    """
    assert (len(p) == len(a))

    z = zip(a,p)  #the actual rating and prediction rating are brought together into an iterable of tuples


    sum = 0

    for x,y in z: 
        sum += (x-y)**2

    assert sum != 0
    RMSE =  (sum / len(a))**(1/2)

    w.write("RMSE: {0:.2f}".format(RMSE))


# -------------
# netflix_solve
# -------------

def netflix_solve (r, w) :
    """
    r a reader
    w a writer
    """

    #---------------------------------------------------------------------------
    #CACHE BUILDING
    #---------------------------------------------------------------------------


    inFile = open("/u/prat0318/netflix-tests/aip256-cacheAvgAndModeRatingPerMovie.txt", "r")
    movie_avg_cache = inFile.readline()
    movie_avg_cache = ast.literal_eval(movie_avg_cache)
    assert (movie_avg_cache != {})

    inFile = open("/u/prat0318/netflix-tests/aip256-cacheAvgAndModeRatingPerCust.txt", "r")
    customer_avg_cache = inFile.readline()
    customer_avg_cache = ast.literal_eval(customer_avg_cache)
    assert (customer_avg_cache != {})

    inFile = open("/u/prat0318/netflix-tests/erb988+np6593-ProbeAnswersDictionary.txt", "r")
    answers_cache = inFile.readline()
    answers_cache = ast.literal_eval(answers_cache)
    assert (answers_cache != {})

    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------


    #--------------------------
    #Total Movie Average Rating
    #--------------------------

    total_sum = 0 

    for i in range(1,10001):
        movie_info_list = movie_avg_cache[i]

        total_sum += movie_info_list[0]

    assert (total_sum != 0)
    total_movie_avg = total_sum/10000





    prediction_list = []
    actual_list = []




    for line in r:

        prediction = 0
        actual = 0



        if line.count(":") == 1: #The code continues here in the case that a movieID is present

            print_movie = line.rstrip()
            movie = print_movie.rstrip(":")
            movie_info_list = movie_avg_cache[eval(movie)]  #pulling movie average rate from cache
            movie_rate = movie_info_list[0]

            movie_offset = (movie_rate - total_movie_avg)/2  

            #movie_offset takes the average of the difference between the particular
            #movie's average and the total movie average

            print(print_movie)



        elif line == "\n":

            #In the case that a blank new line is received as 
            #input, the code loop will break, indicating the end of file

            break



        else:

            customer = line.rstrip()
            customer_info_list = customer_avg_cache[eval(customer)]  #pulling customer average rate from cache
            customer_rate = customer_info_list[0]

            customer_offset = (customer_rate - movie_rate)/2

            #customer_offset takes the average of the difference between the particular
            #customer's average and the particular movie's average


            prediction = (movie_rate + (((0.65*movie_offset) + (1.2*customer_offset))))

            #prediction takes the particular movie's average rating and adds the two offsets with different weights to each

            
            if customer_rate < 1.3:  #If the customer consistently rates majority of movies a 1, then the program will predict a 1
                prediction = 1
            elif customer_rate > 4.7:  #If the customer consistently rates majority of movies a 5, then the program will predict a 5
                prediction = 5

            assert (prediction != 0)
        
            probe_movie = answers_cache[eval(movie)]
            probe_answer = probe_movie[eval(customer)]
            actual_list.append(probe_answer)  #Both the actual rating and the prediction rating are appended to lists used for rmse
            prediction_list.append(prediction)


            print("{0:.1f}".format(prediction))

    assert (prediction_list != [])
    assert (actual_list != [])

    rmse(w, actual_list, prediction_list)


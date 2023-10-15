"""
Spark V2 Style Code
"""

# from spark version 2, sparkcontext is no longer used (directly).
# rather, SparkSession is used to manage each session.
from pyspark.sql import SparkSssion, Row, functions

def loadMovieNames():
    movieNames = {}
    with open("ml-100k/u.item") as f:
        for line in f:
            fields = line.split('|')
            movieNames[int(fields[0])] = fields[1]

    return movieNames

def parseInput(line):
    fields = line.split()
    return Row(movieID = int(fields[1]), rating = float(fields[2]))

if __name__ == "__main__":
    # getOrCreate function is new in Spark V2.
    spark = SparkSession.builder.appName("PopularMovies").getOrCreate()

    movieNames = loadMovieNames()

    # a spark session contains a sparkcontext connection
    lines = spark.sparkContext.textFile("hdfs:///user/maria_dev/ml-100k/u.data")

    # this is creating an RDD (currently like a list in python case
    movies = lines.map(parseInput)

    # in spark v2 you can create dataframes to work with and perform actions on
    # them
    movieDataset = spark.createDataFrame(movies)

    # example of an action on a dataframe
    averageRatings = movieDataset.groupBy("movieID").avg("rating")

    # you can perform multiple actions on a single dataframe.
    counts = movieDataset.groupBy("movieID").count()

    # you can also work with the results of dataframe actions
    # in this case, counts and averageRatings are both grouped by the same
    # field and thus able to join
    averagesAndCounts = counts.join(averageRatings, "movieID")

    topTen = averagesAndCounts.orderBy("avg(rating)").take(10)

    for movie in topTen:
        print(movieNames[movie[0]], movie[1], movie[2])

    spark.stop()

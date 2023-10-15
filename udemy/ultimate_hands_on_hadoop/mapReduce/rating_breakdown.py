from mrjob.job import MRJob
from mrjob.step import MRStep

class RatingsBreakdown(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer=self.reducer_count_ratings)
        ]

    def mapper_get_ratings(self, _, line):
        (user_id, movie_id, rating, timestampe) = line.split('\t')
        yield movie_id, rating

    def reducer_count_ratings(self, key, values):
        yield str(sum(values)).zfill(5), key

    def reducer_sort_output(self, count, movies):
        for movie in movies:
            yield movie, count

if __name__ == "__main__":
    RatingsBreakdown.run()

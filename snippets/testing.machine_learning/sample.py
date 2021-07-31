from functools import reduce
from random import sample


class Perceptron:
    def __init__(self, vector_width: int):
        """
        Initialize a perceptron.

        - `vector_width`: Width of a feature vector, plus one for the expected value.
        """

        self.weights = [0.0] * vector_width

    def predict(self, vector: list[float]) -> float:
        """
        Classify a vector with the perceptron's current weights.

        - `vector`: A feature vector of the same width that the perceptron was initialized with.
        The last value is ignored, but must be present.
        """

        assert len(vector) == len(
            self.weights), "Feature vector of wrong length."

        prediction_raw = self.weights[0] + reduce(
            lambda accum, next: accum + (next[0] * next[1]),
            zip(self.weights[1:], vector[:-1]),
            0)
        return 1.0 if prediction_raw >= 0 else 0.0

    def train_single(self, learning_rate: float, vector: list[float]) -> None:
        """
        Train the perceptron on a single vector once.

        - `learning_rate`: How strongly the weights change for this training datum.
        - `vector`: A feature vector of the same width that the perceptron was initialized with. The last value is the expected value.
        """
        prediction = self.predict(vector)
        error = vector[-1] - prediction

        self.weights[0] += learning_rate * error
        self.weights[1:] = [weight + (learning_rate * error * feature) for weight,
                            feature in zip(self.weights[1:], vector[:-1])]

    def train_many(self, learning_rate: float, epochs: int, vectors: list[list[float]]) -> None:
        """
        Train the perceptron on one or more feature vectors multiple times, randomizing the order of the training vectors each time.

        - `learning rate`: How strongly the weights change for the training data.
        - `epochs`: The number of iterations for all training data.
        - `vectors`: A list of training vectors. The last value in each vector is the expected value for that vector.
        """

        for _ in range(epochs):
            rows = sample(vectors, len(vectors))
            for row in rows:
                self.train_single(learning_rate, row)

    def error_rate(self, vectors: list[list[float]]) -> float:
        """
        Calculate the rate at which the perceptron misclassifies vectors for a given set of vectors.

        - `vectors`: A list of vectors to calculate the error rate for. The last value in each vector is the expected value for that vector.
        """

        num_errors = 0.0
        for row in vectors:
            num_errors += abs(self.predict(row) - row[-1])
        return num_errors / len(vectors)

    def train_many_with_rollbacks(self, learning_rate: float, epochs: int, vectors: list[list[float]]) -> None:
        """
        Train the perceptron on one or more feature vectors multiple times,
        randomizing the order of the training vectors each time, and rolling
        back to the previous weights on each iteration if the error rate increases.

        - `learning rate`: How strongly the weights change for the training data.
        - `epochs`: The number of iterations for all training data.
        - `vectors`: A list of training vectors. The last value in each vector is the expected value for that vector.
        """

        lowest_error_rate = self.error_rate(vectors)
        lowest_error_rate_weights = self.weights.copy()
        for _ in range(epochs):

            rows = sample(vectors, len(vectors))
            for row in rows:
                self.train_single(learning_rate, row)

            new_error_rate = self.error_rate(vectors)

            if new_error_rate < lowest_error_rate:
                lowest_error_rate = new_error_rate
                lowest_error_rate_weights = self.weights.copy()

        self.weights = lowest_error_rate_weights
from Genetic_Algorithm import GeneticAlgorithm


class Decoder:
    def __init__(self, encoded_text):
        self.encoded_text = encoded_text

    def decode(self):
        ga = GeneticAlgorithm(50, 500, 0.4, 2, self.encoded_text)
        decoded_text = ga.evolve()
        return decoded_text

from sys import argv

script, sample_a_filename, sample_b_filename, target_filename = argv


def word_probability(file):
    words = file.read().split(" ")
    tally = {}
    for word in words:
        if word in tally:
            tally[word] += 1 / len(words)
        else:
            tally[word] = 1 / len(words)
    return tally


def probability_calc(probabilities, target_text):
    p_value = 0
    for word in target_text:
        if word in probabilities:
            p_value *= probabilities[word]
    return p_value


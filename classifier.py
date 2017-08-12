from sys import argv


def word_probability(file):
    file = open(file)
    words = file.read().split(" ")
    tally = {}
    for word in words:
        if word in tally:
            tally[word] += 1 / len(words)
        else:
            tally[word] = 1 / len(words)
    file.close()
    return tally


def sample_probability(probabilities, target):
    target = open(target)
    target_text = target.read().split(" ")
    p_value = 1
    for word in target_text:
        if word in probabilities:
            p_value *= probabilities[word]
    target.close()
    return p_value


def file_probability(filename, target_filename):
    return sample_probability(word_probability(filename), target_filename)


def normalise_probabilities(a, b):
    total = a + b
    return {'a': a / total, 'b': b / total}


def classify(sample_a_filename, sample_b_filename, target_filename):
    sample_a = file_probability(sample_a_filename, target_filename)
    sample_b = file_probability(sample_b_filename, target_filename)
    normalised = normalise_probabilities(sample_a, sample_b)

    if normalised['a'] == normalised['b']:
        print("No classification is possible")
        return
    elif normalised['a'] > normalised['b']:
        selection = "Sample A"
        selection_probability = normalised['a']
    else:
        selection = "Sample B"
        selection_probability = normalised['b']

    selection_probability = round(selection_probability * 100, 2)

    print("There is a {0}% chance that the target text was written by {1}.".format(
        selection_probability, selection))


def main():
    script, a, b, target = argv
    classify(a, b, target)

main()

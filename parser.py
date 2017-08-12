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


def probability_calc(probabilities, target):
    target_text = open(target).read().split(" ")
    p_value = 1
    for word in target_text:
        if word in probabilities:
            p_value *= probabilities[word]
    return p_value


def classify(sample_a_filename, sample_b_filename, target_filename):
    sample_a_probabilities = word_probability(sample_a_filename)
    sample_b_probabilities = word_probability(sample_b_filename)
    sample_a_likelihood = probability_calc(sample_a_probabilities, target_filename)
    sample_b_likelihood = probability_calc(sample_b_probabilities, target_filename)
    print(sample_a_likelihood)
    print(sample_b_likelihood)
    if sample_a_likelihood == sample_b_likelihood:
        print("Even chance")
    elif sample_a_likelihood > sample_b_likelihood:
        print("Sample A")
    else:
        print("Sample B")

classify("a.txt", "b.txt", "c.txt")


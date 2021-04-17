
import random

def generate_text(length):
    # It doesn't really matter, so we'll do uniform distribution
    text = [bool(random.randint(0, 1)) for i in range(length)]
    return text


def corrupt_text(text, flip_probability):
    # Return version of the given text in which each character has a uniform probability of being flipped
    return [not char
            if random.random() < flip_probability
            else char
            for char in text]


def num_diffs(text1, text2):
    # Returns number of times corresponding characters in two texts are different
    return sum([1 if c1 != c2 else 0 for c1, c2 in zip(text1, text2)])


def majority(variants_list):
    pass # TODO
    


def rectify_majoritarian(*args):
    # Given some number of texts, choose for each character position the most frequent option as the inferred original value
    return [majority(char_variants) for char_variants in zip(*args)]


def main():
    length = 100
    corrupt_prob = 1e-1

    orig = generate_text(length)

    ms1 = corrupt_text(orig, corrupt_prob)
    ms2 = corrupt_text(orig, corrupt_prob)

    print('Manuscript length:', length)
    print('Bit corruption probability', corrupt_prob)

    print('Child 1 errors:', num_diffs(orig, ms1))
    print('Child 2 errors:', num_diffs(orig, ms2))

    print(orig)
    print(ms1)
    print(ms2)


if __name__ == '__main__':
    main()

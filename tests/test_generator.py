import unittest
import generator


def test_sample_single_word():
    sample = ('foo', 'bar', 'foobar')
    word = generator.get_sample(sample)
    assert word in sample


def test_sample_multiple_words():
    sample = ('foo', 'bar', 'foobar')
    words = generator.get_sample(sample, 2)
    assert len(words) == 2
    assert words[0] in sample
    assert words[1] in sample
    assert words[0] is not words[1]


def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 5

from __future__ import print_function
import random

adjectives = ('complete', 'modern', 'self-service', 'integrated', 'end-to-end')
ci_cd = ('continuous testing', 'continuous integration', 'continuous deployment', 'continuous improvement', 'DevOps')
adverbs = ('remarkably', 'enormously', 'substantially', 'significantly', 'seriously')
verbs = ('accelerates', 'improves', 'enhances', 'revamps', 'boosts')
buzz = ('smaller code changes', 'Faster Mean Time To Resolution (MTTR)', 'Smaller Backlog', 'Faster Release Rate')


def get_sample(tuple_data, n=1):
    result = random.sample(tuple_data, n)
    if n == 1:
        return result[0]
    return result


def generate_buzz():
    phrase = ' '.join([get_sample(adjectives), get_sample(ci_cd), get_sample(adverbs), get_sample(verbs),
                       get_sample(buzz)])
    return phrase.title()


if __name__ == "__main__":
    print(generate_buzz())

# -*- coding: utf-8 -*-
import pickle

from nltk.corpus import wordnet as wn


def remove_tokens_from_list(l, rm):
    if type(rm) is not set:
        rm = set(rm)

    return [t for t in l if t not in rm]


def pickle_data(data, picklefile):
    """Helper function to pickle `data` in `picklefile`."""
    with open(picklefile, 'wb') as f:
        pickle.dump(data, f, protocol=2)


def unpickle_file(picklefile):
    """Helper function to unpickle data from `picklefile`."""
    with open(picklefile, 'rb') as f:
        return pickle.load(f)


def require_types(x, valid_types):
    if all(isinstance(x, t) is False for t in valid_types):
        raise ValueError('requires type:', str(valid_types))


def require_listlike(x):
    require_types(x, (set, tuple, list))


def require_dictlike(x):
    require_types(x, (dict,))


def pos_tag_convert_penn_to_wn(tag):
    if tag in ['JJ', 'JJR', 'JJS']:
        return wn.ADJ
    elif tag in ['RB', 'RBR', 'RBS']:
        return wn.ADV
    elif tag in ['NN', 'NNS', 'NNP', 'NNPS']:
        return wn.NOUN
    elif tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
        return wn.VERB
    return None


def simplified_wn_pos(pos):
    """
    Return a simplified POS tag for a full WordNet POS tag `pos`.
    Does the following conversion:
    - all N... (noun) tags to 'N'
    - all V... (verb) tags to 'V'
    - all ADJ... (adjective) tags to 'ADJ'
    - all ADV... (adverb) tags to 'ADV'
    - all other to None
    """
    if pos.startswith('N') or pos.startswith('V'):
        return pos[0]
    elif pos.startswith('ADJ') or pos.startswith('ADV'):
        return pos[:3]
    else:
        return None
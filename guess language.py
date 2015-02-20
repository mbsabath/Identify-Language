__author__ = 'Ben'

def eng_letter_prob(c):
    """ if c is the space character (' ') or an alphabetic character,
        returns c's monogram probability (for English);
        returns 1.0 for any other character.
        adapted from:
        http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    if c == ' ': return 0.1960
    if c == 'e' or c == 'E': return 0.1017
    if c == 't' or c == 'T': return 0.0737
    if c == 'a' or c == 'A': return 0.0661
    if c == 'o' or c == 'O': return 0.0610
    if c == 'i' or c == 'I': return 0.0562
    if c == 'n' or c == 'N': return 0.0557
    if c == 'h' or c == 'H': return 0.0542
    if c == 's' or c == 'S': return 0.0508
    if c == 'r' or c == 'R': return 0.0458
    if c == 'd' or c == 'D': return 0.0369
    if c == 'l' or c == 'L': return 0.0325
    if c == 'u' or c == 'U': return 0.0228
    if c == 'm' or c == 'M': return 0.0205
    if c == 'c' or c == 'C': return 0.0192
    if c == 'w' or c == 'W': return 0.0190
    if c == 'f' or c == 'F': return 0.0175
    if c == 'y' or c == 'Y': return 0.0165
    if c == 'g' or c == 'G': return 0.0161
    if c == 'p' or c == 'P': return 0.0131
    if c == 'b' or c == 'B': return 0.0115
    if c == 'v' or c == 'V': return 0.0088
    if c == 'k' or c == 'K': return 0.0066
    if c == 'x' or c == 'X': return 0.0014
    if c == 'j' or c == 'J': return 0.0008
    if c == 'q' or c == 'Q': return 0.0008
    if c == 'z' or c == 'Z': return 0.0005
    if c == 'é' or c == 'É': return 0.0
    if c == 'é' or c == 'É': return 0.0
    if c == 'í' or c == 'Í': return 0.0
    if c == 'á' or c == 'Á': return 0.0
    if c == 'ñ' or c == 'Ñ': return 0.0
    if c == 'ú' or c == 'Ú': return 0.0
    if c == 'ü' or c == 'Ü': return 0.0
    if c == 'æ' or c == 'Æ' or c == 'œ' or c == 'Œ': return 0.0
    if c == 'è' or c == 'È': return 0.0
    if c == 'â' or c == 'Â': return 0.0
    if c == 'ï' or c == 'Ï': return 0.0
    if c == 'ê' or c == 'Ê': return 0.0
    if c == 'ç' or c == 'Ç': return 0.0
    if c == 'î' or c == 'Î': return 0.0
    if c == 'ô' or c == 'Ô': return 0.0
    if c == 'û' or c == 'Û': return 0.0
    if c == 'ü' or c == 'Ü': return 0.0
    if c == 'ë' or c == 'Ë': return 0.0
    if c == 'à' or c == 'À': return 0.0
    if c == 'ù' or c == 'Ù': return 0.0
    return 1.0

def esp_letter_prob(c):
    """ if c is the space character (' ') or an alphabetic character,
        returns c's monogram probability (for Spanish);
        returns 1.0 for any other character.
        adapted from:
        http://www.sttmedia.com/characterfrequency-spanish
    """
    if c == ' ': return 0.1915
    if c == 'e' or c == 'E': return 0.1372
    if c == 't' or c == 'T': return 0.0460
    if c == 'a' or c == 'A': return 0.1172
    if c == 'o' or c == 'O': return 0.0844
    if c == 'i' or c == 'I': return 0.0528
    if c == 'n' or c == 'N': return 0.0683
    if c == 'h' or c == 'H': return 0.0118
    if c == 's' or c == 'S': return 0.0720
    if c == 'r' or c == 'R': return 0.0641
    if c == 'd' or c == 'D': return 0.0467
    if c == 'l' or c == 'L': return 0.0524
    if c == 'u' or c == 'U': return 0.0455
    if c == 'm' or c == 'M': return 0.0308
    if c == 'c' or c == 'C': return 0.0387
    if c == 'w' or c == 'W': return 0.0004
    if c == 'f' or c == 'F': return 0.0069
    if c == 'y' or c == 'Y': return 0.0109
    if c == 'g' or c == 'G': return 0.0100
    if c == 'p' or c == 'P': return 0.0289
    if c == 'b' or c == 'B': return 0.0149
    if c == 'v' or c == 'V': return 0.0105
    if c == 'k' or c == 'K': return 0.0011
    if c == 'x' or c == 'X': return 0.0014
    if c == 'j' or c == 'J': return 0.0052
    if c == 'q' or c == 'Q': return 0.0111
    if c == 'z' or c == 'Z': return 0.0047
    if c == 'é' or c == 'É': return 0.0036
    if c == 'í' or c == 'Í': return 0.0070
    if c == 'á' or c == 'Á': return 0.0044
    if c == 'ñ' or c == 'Ñ': return 0.0017
    if c == 'ú' or c == 'Ú': return 0.0012
    if c == 'ü' or c == 'Ü': return 0.0002
    if c == 'æ' or c == 'Æ' or c == 'œ' or c == 'Œ': return 0.0
    if c == 'è' or c == 'È': return 0.0
    if c == 'â' or c == 'Â': return 0.0
    if c == 'ï' or c == 'Ï': return 0.0
    if c == 'ê' or c == 'Ê': return 0.0
    if c == 'ç' or c == 'Ç': return 0.0
    if c == 'î' or c == 'Î': return 0.0
    if c == 'ô' or c == 'Ô': return 0.0
    if c == 'û' or c == 'Û': return 0.0
    if c == 'ë' or c == 'Ë': return 0.0
    if c == 'à' or c == 'À': return 0.0
    if c == 'ù' or c == 'Ù': return 0.0
    return 1.0

def fra_letter_prob(c):
    """ if c is the space character (' ') or an alphabetic character,
        returns c's monogram probability (for Spanish);
        returns 1.0 for any other character.
        adapted from:
        http://www.lexique.org/listes/liste_lettres.php
    """
    if c == ' ': return 0.1949
    if c == 'e' or c == 'E': return 0.13754
    if c == 't' or c == 'T': return 0.06699
    if c == 'a' or c == 'A': return 0.07265
    if c == 'o' or c == 'O': return 0.05095
    if c == 'i' or c == 'I': return 0.07027
    if c == 'n' or c == 'N': return 0.06671
    if c == 'h' or c == 'H': return 0.00810
    if c == 's' or c == 'S': return 0.07800
    if c == 'r' or c == 'R': return 0.06216
    if c == 'd' or c == 'D': return 0.03538
    if c == 'l' or c == 'L': return 0.05438
    if c == 'u' or c == 'U': return 0.05697
    if c == 'm' or c == 'M': return 0.02743
    if c == 'c' or c == 'C': return 0.03029
    if c == 'w' or c == 'W': return 0.00025
    if c == 'f' or c == 'F': return 0.01018
    if c == 'y' or c == 'Y': return 0.00269
    if c == 'g' or c == 'G': return 0.00972
    if c == 'p' or c == 'P': return 0.02704
    if c == 'b' or c == 'B': return 0.00893
    if c == 'v' or c == 'V': return 0.01398
    if c == 'k' or c == 'K': return 0.00046
    if c == 'x' or c == 'X': return 0.00411
    if c == 'j' or c == 'J': return 0.00480
    if c == 'q' or c == 'Q': return 0.01045
    if c == 'z' or c == 'Z': return 0.00116
    if c == 'é' or c == 'É': return 0.01974
    if c == 'í' or c == 'Í': return 0.0
    if c == 'á' or c == 'Á': return 0.0
    if c == 'ñ' or c == 'Ñ': return 0.0
    if c == 'ú' or c == 'Ú': return 0.0
    if c == 'æ' or c == 'Æ' or c == 'œ' or c == 'Œ': return 0.00341
    if c == 'è' or c == 'È': return 0.00343
    if c == 'â' or c == 'Â': return 0.00045
    if c == 'ï' or c == 'Ï': return 0.00010
    if c == 'ê' or c == 'Ê': return 0.00056
    if c == 'ç' or c == 'Ç': return 0.00080
    if c == 'î' or c == 'Î': return 0.00044
    if c == 'ô' or c == 'Ô': return 0.00053
    if c == 'û' or c == 'Û': return 0.00033
    if c == 'ü' or c == 'Ü': return 0.00001
    if c == 'ë' or c == 'Ë': return 0.00003
    if c == 'à' or c == 'À': return 0.00459
    if c == 'ù' or c == 'Ù': return 0.00039
    return 1.0

def what_language(s):
    """
    determines what language a sentence (s) is is most likely to be
    :param s: string
    :return: string
    """
    languages = ['English', 'Spanish', 'French']
    score_list = [[score_sentence(s, language), language] for language in languages]
    print(score_list)
    best_fit = max(score_list)
    return best_fit[1]


def score_sentence(s, language):
    """
    determines the probability of a sentence in a given language
    having the combination of characters in the input sentence
    :param s: Sentence in question input as a string
    :param language: the language being checked against (string)
    :return: float value of the joint letter probability
    """
    if s == '':
        return 1
    if language == 'English':
        rest = score_sentence(s[1:], language)
        if rest == 0: return 0
        return (eng_letter_prob(s[0])*10) * rest
    if language == 'Spanish':
        rest = score_sentence(s[1:], language)
        if rest == 0: return 0
        return (esp_letter_prob(s[0])*10) * rest
    if language == 'French':
        rest = score_sentence(s[1:], language)
        if rest == 0: return 0
        return (fra_letter_prob(s[0])*10) * rest

from Eng_Bigram import Eng_Bigram_Freq
def bigram_sentence_score(s, language):
    """
    scores how like a language a string is based on two character sequences
    :param s: a string
    :param language: English, French, or Spanish
    :return: Float
    """
    if language == 'English':
        rest = score_sentence(s[1:], language)
        if rest == 0: return 0
        return (Eng_Bigram_Freq(s[0:2])*10) * rest

def run():
    """
    Runs the program
    :return: None
    """
    sentence = input('What sentence would you like to test:  ')
    print(what_language(sentence))
    return None

run()
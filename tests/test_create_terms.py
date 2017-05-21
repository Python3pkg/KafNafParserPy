"""
Test the create_token and create_term methods
"""

from nose.tools import assert_equal

from KafNafParserPy import KafNafParser

def test_create_terms():
    """
    Can we create_terms via the create_{term,token} functions?
    """
    
    naf = KafNafParser(type="NAF")
    sent=1; offset=0
    input = [('dit', 'dit', 'O', 'VNW'),
             ('is', 'zijn', 'V', 'WW'),
             ('een', 'een', 'D', 'LID'),
             ('test', 'test', 'N', 'N')]

    offset = 0
    for (word, lemma, pos, morph) in input:
        token = naf.create_wf(word, 1, offset)
        offset += len(word)
        term = naf.create_term(lemma, pos, morph, [token])

    tokens = {t.get_id(): t for t in naf.get_tokens()}
    assert_equal(len(tokens), 4)
    
    result = {}
    for term in naf.get_terms():
        for token_id in term.get_span().get_span_ids():
            token = tokens[token_id]
            result[term.get_id()] = (token.get_text(), term.get_lemma(),
                                     term.get_pos(), term.get_morphofeat())
    result = [result[tid] for tid in sorted(result.keys())]
    assert_equal(input, result)


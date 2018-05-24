import unicodedata

import betacode.conv

def _test_beta_uni_equality(beta, uni):
    """
    Test that the result of converting beta is uni.

    Comparison is done via the NFC normalization for unicode.

    Args:
    beta: The beta code to convert.
    uni: The expected unicode result from conversion.
    """
    conv = betacode.conv.beta_to_uni(beta)
    conv_normalized = unicodedata.normalize('NFC', conv)
    uni_normalized = unicodedata.normalize('NFC', uni)

    assert conv_normalized == uni_normalized

def test_empty():
    beta = ''
    uni = ''

    _test_beta_uni_equality(beta, uni)

def test_simple_conv():
    beta = 'tou='
    uni = 'τοῦ'

    _test_beta_uni_equality(beta, uni)

def test_final_sigma():
    beta = 'th=s'
    uni = 'τῆς'

    _test_beta_uni_equality(beta, uni)

def test_numeric_sigma_id():
    beta = 'th=s2'
    uni = 'τῆς'

    _test_beta_uni_equality(beta, uni)

def test_keep_non_final_sigma_numeric():
    beta = 'th=s3 tou='
    uni = 'τῆϲ τοῦ'

    _test_beta_uni_equality(beta, uni)

def test_final_sigma_word():
    beta = 'th=s tou='
    uni = 'τῆς τοῦ'

    _test_beta_uni_equality(beta, uni)

def test_final_sigma_whitespace():
    beta = 'th=s\ttou='
    uni = 'τῆς\tτοῦ'

    _test_beta_uni_equality(beta, uni)

def test_final_sigma_punctuation():
    beta = 'th=s\' tou='
    uni = 'τῆς’ τοῦ'

    _test_beta_uni_equality(beta, uni)

def test_multi_word():
    beta = 'analabo/ntes de\ kaq\' e(/kaston'
    uni = 'αναλαβόντες δὲ καθ’ ἕκαστον'

    _test_beta_uni_equality(beta, uni)

def test_punctuation_semicolon():
    beta = 'e)/oiken h)\ dida/skonti; nh\\'
    uni = 'ἔοικεν ἢ διδάσκοντι; νὴ'

    _test_beta_uni_equality(beta, uni)

def test_punctuation_colon():
    beta = 'dh=lon: oi(/ te'
    uni = 'δῆλον· οἵ τε'

    _test_beta_uni_equality(beta, uni)

def test_out_of_order():
    beta = 'e/)oiken h\) dida/skonti; nh\\ a=|)i+\\'
    uni = 'ἔοικεν ἢ διδάσκοντι; νὴ ᾆῒ'

def test_cap_out_of_order():
    beta = '*)/eforos ka*)/ei\ a/)lloi'
    uni = 'Ἔφορος καἜὶ ἄλλοι'

    _test_beta_uni_equality(beta, uni)

def test_cap_out_of_order_with_iota():
    beta = '*)/eforos ka*)/ei\ a/)lloi *)h\|'
    uni = 'Ἔφορος καἜὶ ἄλλοι ᾛ'

    _test_beta_uni_equality(beta, uni)

def test_case_insensitive():
    beta = '*)/eFoRos kA*)/Ei\ a/)Lloi *)H\|'
    uni = 'Ἔφορος καἜὶ ἄλλοι ᾛ'

    _test_beta_uni_equality(beta, uni)

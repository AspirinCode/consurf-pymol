from consurfcolor import parse_line, parse_file


def test_parse_line():
    line = '   67	   Q	   GLN67:A	 1.247		  2	 0.310, 1.797			    4,1			   16/16	T,H,Q,D,S,A,K,N,E,C,G'
    resi, score = parse_line(line)
    assert resi == 67
    assert score == 2


def test_insignificant_score_line():
    line = '  72	   D	   ASP72:A	 0.976		  2*	-0.096, 1.797			    5,1			   16/16	S,K,D,E,M,T,L,Q,P'
    resi, score = parse_line(line)
    assert resi == 72
    assert score == 0


def test_parse_comment():
    line = '- POS: The position of the AA in the SEQRES derived sequence.'
    result = parse_line(line)
    assert result is False


def test_parse_file():
    with open('cpf1.consurf.grades') as f:
        results = 0
        for _ in parse_file(f):
            results += 1
    assert results == 1307

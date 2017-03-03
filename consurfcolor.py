import re


def parse_line(line):
    match = re.search(r'(?P<resi>\d+)\s+\w\s+[A-Z0-9:\-]+\s+[0-9.\-]+\s+(?P<conservation_score>\d+\*?)', line)
    if match:
        residue = int(match.group('resi'))
        score = match.group('conservation_score')
        if '*' in score:
            score = 0
        else:
            score = int(score)
        return residue, score
    return False


def parse_file(f):
    for line in f:
        parse_result = parse_line(line)
        if not parse_result:
            continue
        residue, score = parse_result
        yield residue, score


def colors(r=8, g=58, b=0):
    # builds up a gradient of colors for each conservation score
    delta_r = float(255 - r) / 10.0
    delta_g = float(255 - g) / 10.0
    delta_b = float(255 - b) / 10.0
    return {10-i: ((r + delta_r * i)/255.0,
                   (g + delta_g * i)/255.0,
                   (b + delta_b * i)/255.0) for i in range(11)}


def main():
    # We have to give names to our custom RGB colors in order to use them later
    for i, rgb in colors().items():
        cmd.set_color("consurf%d" % i, rgb)
    try:
        with open('consurf.grades') as f:
            for residue, score in parse_file(f):
                # We specify the residue number and require that it be an amino acid,
                # because otherwise some nucleic acids will get colored as well
                cmd.select("sele", "resi %d & resn ala+arg+asn+asp+cys+glu+gln+gly+his+ile+leu+lys+met+phe+pro+ser+thr+trp+tyr+val" % residue)
                color = "consurf%d" % score
                cmd.color(color, "sele")
    except Exception as e:
        print("You need a file called consurf.grades")

if __name__ == 'pymol':
    main()

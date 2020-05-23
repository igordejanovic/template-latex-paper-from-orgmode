# -*- coding: utf-8 -*-
import sys


def chop_off_header(s):
    assert s.count(r'\author{') == 1
    return r'\author{{{}'.format(s.split(r'\author{')[1])


def chop_off_footer(s):
    assert s.count(r'\end{document}') == 1
    return s.split(r'\end{document}')[0]


def extract_body(s):
    s = chop_off_header(s)
    s = chop_off_footer(s)
    return s


def other_changes(s):
    # s = s.replace("section{", "section*{")
    s = s.replace('£', r'$\pounds$')
    return s


def main():
    input = sys.argv[1]
    output = sys.argv[2]
    content = open(input).read()
    result = extract_body(content)
    result = other_changes(result)
    open(output, 'w').write(result)


if __name__ == '__main__':
    main()

import sys
import threading


data = sys.stdin.read().strip()

tokens = []
i = 0
ln = len(data)
while i < ln:
    c = data[i]
    if c.isspace():
        i += 1
        continue
    if c in '()+-*/':

        if c == '-' and i+1 < ln and data[i+1].isdigit():
            j = i+1
            while j < ln and data[j].isdigit():
                j += 1
            tokens.append(data[i:j])
            i = j
        else:
            tokens.append(c)
            i += 1
    elif c.isdigit():
        j = i
        while j < ln and data[j].isdigit():
            j += 1
        tokens.append(data[i:j])
        i = j
    else:
        i += 1


pos = 0
def parse_expr():
    global pos
    tok = tokens[pos]

    if tok not in '()+-*/' or (tok.startswith('-') and tok[1:].isdigit()):
        pos += 1
        return int(tok)


    assert tok == '(', "Expected '('"
    pos += 1

    op = tokens[pos]
    pos += 1

    e1 = parse_expr()

    if op == '-' and tokens[pos] == ')':
        pos += 1
        return -e1

    e2 = parse_expr()
    assert tokens[pos] == ')', "Expected ')'"
    pos += 1

    if op == '+':
        return e1 + e2
    elif op == '-':
        return e1 - e2
    elif op == '*':
        return e1 * e2
    elif op == '/':
        q = e1 // e2
        r = e1 - e2 * q
        if r < 0:
            r += abs(e2)
            if e2 > 0:
                q -= 1
            else:
                q += 1
        return q

result = parse_expr()
print(result)


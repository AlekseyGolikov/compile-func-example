# using byte string

st = bytes('2 + 2', 'utf-8')
print(st)
code = compile(st, '', 'eval')
r = eval(code)
print(r)
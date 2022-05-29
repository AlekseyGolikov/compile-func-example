
with open('test.py', encoding='utf-8', newline=None) as file:
    src = file.read()
    start_doc = src.find('"""', 0)
    end_doc = src.find('"""', start_doc + 1)
    doc = src[start_doc:end_doc+3]
    src = src.replace(doc, '')
    src = src.replace('    \n', '')
    src = src.replace('\n\n', '\n')
    for s in src:
        if s.startswith('#'):
            start = src.find('#')
            end = src.find('\n',start)
            src = src.replace(src[start:end], '\n\n')
    src = src.replace('\n\n', '')
    print(src)

code = compile(src, 'test.py', 'exec')
print(type(code))
exec(code)
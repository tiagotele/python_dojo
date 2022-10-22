from collections import OrderedDict

a = OrderedDict(nome= 'Tiago', idade= 37, conje= 'Luthana', filha= 'Mariana')
print(a)
print(a.get('idade'))
print(a.get('unexisting','default to save map : p'))
a.setdefault("vai", "Missing value. I'm a default")
print(a['vai'])
a.move_to_end('nome')
print(a)
a.clear()
print(a)

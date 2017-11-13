def reindex(string, triplet):
    ind = [string.index(t) for t in triplet]
    for n,idx in enumerate(sorted(ind)):
        string.insert(idx,triplet[n])
        string.pop(idx+1)
    return string

def recoverSecret(triplets):
    s = []
    for triplet in triplets:
        for el in triplet:
            if el not in s:
                s.append(el)
    for i in range(len(triplets)):
        for triplet in triplets:
            s = reindex(s,triplet)
    return ''.join(s) 

secret = "whatisup"
triplets = [['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

'''
def recoverSecret(triplets):
  r = list(set([i for l in triplets for i in l]))
  for l in triplets:
    fix(r, l[1], l[2])
    fix(r, l[0], l[1])
  return ''.join(r)
  
def fix(l, a, b):
   """let l.index(a) < l.index(b)"""
   if l.index(a) > l.index(b):
       l.remove(a)
       l.insert(l.index(b), a)

'''
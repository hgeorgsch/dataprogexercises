
def f(x,a=7,m=97): return x*a % m


def g(s,**kw):
    s.append( f( s[-1], **kw ) )
    return s


def r(s,m=97,**kw):
    if len(s) >= m: return s
    else: return r(g(s,**kw))

def test(a,m=97):
    s = set(r([1],a=a,m=m))
    return (a,len(s))

r = [ test(a) for a in range(2,97) ]

print( r )

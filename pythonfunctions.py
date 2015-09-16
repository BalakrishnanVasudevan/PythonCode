def Hello(name):
    if name == 'Bala':
        name = name + '@@@'
    name = name + '!!!!'
    print 'Hello', name
    
def main():
    Hello(sys.argv[1])

from языкcat import kitty

def test_input_and_output():
    codei = '''calm_cat h=smart_cat(reading_cat())
sleeping_cat(h*3)
'''
    code2='''h=int(input())
print(h*3)
'''
    result = kitty(codei)
    assert result == code2
def testif():
    codei='''
calm_cat k=0
calm_cat j=4
calm_cat g=1
playing_cat h=0
fish j==0 cookie j==7:
    sleeping_cat(':)')
fg k==0 cake g==1:
    h=40
dog:
    h=50
'''
    code2='''
k=0
j=4
g=1
h=0
if j==0 or j==7:
    print(':)')
elif k==0 and g==1:
    h=40
else:
    h=50
'''
    result = kitty(codei)    
    assert result == code2
def testfor():
    code2='''for i in range(1,10):
    print(i)
'''
    codei='''whiskas i box purina(1,10):
    sleeping_cat(i)
'''
    result = kitty(codei)    
    assert result == code2
def testw():
    code2='''x=1
while x!=100:
    x+=1
'''
    codei='''playing_cat x=1
fast_cat x!=0:
    x+=1
'''
    result = kitty(codei)    
    assert result == code2
test_input_and_output()

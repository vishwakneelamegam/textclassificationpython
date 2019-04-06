a=['on','the','switch','bot','it','just','not','do','put']
b=['off','the','switch','bot','it','just','not','do','put']
ans=['on','the','switch','off','bot','it','just','not','do','put']
#print len(ans)
la=len(a)
lb=len(b)
lans=len(ans)
ans1=0
ans2=0
c=0
c1=0
s=raw_input("enter a sentence : ")
w=s.split()
wlen=len(w)
w1=[0]*wlen
w2=[0]*wlen
for y in range(0,wlen,1):
    for x in range(0,la,1):
        #print "the values : ",w[y]
        if w[y]==a[x]:
            ans1=w[y]
            
        if w[y]!=a[x]:
            ans1==w[y]
        if w[y]==b[x]:
            ans2=w[y]
            
        if w[y]!=b[x]:
            ans2==w[y]    
    
    for i in range(0,la,1):
        if a[i]==ans1:
            c=c+1
        if a[i]!=ans1:
            c=c
        if b[i]==ans2:
            c1=c1+1
        if b[i]!=ans2:
            c1=c1    
    #print "the count of ",ans1," is : ",c
    p = (float)(((float)(c) + 1))/((float)(la)+(float)(lans))
    #print "the probability of",ans1," is : ",p
    p1 = (float)(((float)(c1) + 1))/((float)(lb)+(float)(lans))
    #print "the probability of",ans1," is : ",p1
    w1[y]=p
    w2[y]=p1
    print w2
    print w1
    c = c*0
    c1 = c1 *0
    ans1=ans1*0
    ans2=ans2*0

lw1=len(w1)
answer=0
answer1=0
for q in range(0,lw1,1):
    answer=w1[q]+answer
    answer1=w2[q]+answer1
#print answer    
positive=0.5*answer
negative=0.5*answer1
#print "the positive probability is",positive
#print "the negative probability is",negative

if positive > negative:
    print "switching on sir"
if negative > positive:
    print "switching off sir"
if positive == negative:
    print "its confusing sir repeat again"

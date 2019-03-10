def WordCound(date):
    ls={}
    for i in date:
        ls[i]=ls.get(i,0)+1
    returnn ls

if __name__"__main__":
    f=open("Shakespeare Sonnet.txt")
    st=""
    for line in f.readline():
        st+line
    print(WordCound(st))
    f.close()

def easy():
    boolean=True
    while boolean:
        h=random.randrange(0,10)
        v=random.randrange(0,10)
        sublist=player2_hit[h]
        if sublist[v]==False:
            sublist[v]=True
            boolean=False
    return None
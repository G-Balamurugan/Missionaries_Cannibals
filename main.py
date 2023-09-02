from queue import Queue

def valid_chk( node ):
    m , c = node[0] , node[1]
    if m < 0 or c < 0 or ( m < c and m > 0 ) or ( 3-m < 3-c and 3-m > 0 ): return False
    return True

def bfs_traversal():
    q = Queue()
    q.put([ [3 , 3 , 'L'] , [[3 , 3 , 'L']] ])       
    
    visit = set()

    while ( not q.empty()):
        temp = q.get()
        node = temp[0]
        path = temp[1]

        # Final Destination ..!!
        if node == [ 0 , 0 , 'R' ]:
            return path

        # Already Visited ..!! 
        if tuple(node) in visit:
            continue
        visit.add( tuple(node) )

        # Next Possible path which can be formed ..!!!
        possible_path = []
        m , c = node[0] , node[1]

        if node[2] == 'L':
            nxt = [m-1 , c, 'R']
            if valid_chk(nxt):possible_path += [nxt]
            nxt = [m-2 , c , 'R']
            if valid_chk( nxt):possible_path += [nxt]
            nxt = [m-1 , c-1 , 'R']
            if valid_chk( nxt):possible_path += [nxt]
            nxt = [m , c-1 , 'R']
            if valid_chk( nxt):possible_path += [nxt]
            nxt = [m , c-2 , 'R']
            if valid_chk( nxt):possible_path += [nxt]
        
        else:
            nxt = [m+1 , c, 'L']
            if valid_chk(nxt):possible_path += [nxt]
            nxt = [m+2 , c , 'L']
            if valid_chk( nxt):possible_path += [nxt]
            nxt = [m+1 , c+1 , 'L']
            if valid_chk( nxt):possible_path += [nxt]
            nxt = [m , c+1 , 'L']
            if valid_chk( nxt):possible_path += [nxt]
            nxt = [m , c+2 , 'L']
            if valid_chk( nxt):possible_path += [nxt]

        for ele in possible_path:
            q.put( [ ele , path + [ele] ]) 


sol = bfs_traversal()

for ele in sol:
    if ele[2] == 'L':
        print("            |>")
        print( "M"*ele[0], " "*(3-ele[0]) , "C"*ele[1] , " "*(3-ele[1]), "\_|_/________________  " , "M"*(3-ele[0]) , " "*(ele[0]), "C"*(3-ele[1]) , " "*ele[1])
    else:
        print("                            |>")
        print( "M"*ele[0], " "*(3-ele[0]) , "C"*ele[1] , " "*(3-ele[1]), "________________\_|_/  " , "M"*(3-ele[0]) , " "*(ele[0]), "C"*(3-ele[1]) , " "*ele[1])
    
    print()

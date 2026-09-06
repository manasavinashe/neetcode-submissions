class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def row() :
            for i in range(len(board)) :
                dic = {}
                for j in board[i] : 
                    dic[j] = dic.get(j , 0) + 1

                for c,d in dic.items() : 
                    if d > 1 and c != "." :
                        return False
            return True

        def column () :
            for i in range(len(board[1])) :
                dic = {}
                for j in range(len(board)) : 
                    dic[board[j][i]]  = dic.get(board[j][i] , 0) + 1
                for c,d in dic.items() : 
                        if d > 1 and c != "." :
                            return False 
            return True 
        def block() :
            for i in [0,3,6] :
                for j in [0,3,6] : 
                    dic = {}
                    for a in range(i, i +3 ) :      
                        for b in range (j,j+3) : 
                            dic[board[a][b]] = dic.get(board[a][b], 0) + 1 
                    for e,f in dic.items() : 
                        if f > 1 and e !="." : 
                            return False
            return True
        
        return row() and column () and block()









            






        

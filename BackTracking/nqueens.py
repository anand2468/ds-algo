class NQueens:
    def __init__(self, n:int=4):
        """
        n is number of queens. \n
        use solve funtion to print all the posiblities to place the queen in an nxn cross board
        """
        self.n = n
        self.x = [-1]*n
        self.nos = 0
        self.res = []

    def __print_solution(self) -> None:
        """
        helper function used to print the solution in the chess board
        """
        for k in range(self.nos):
            print(f"\nSulution no. :{k+1}")
            for i in range(self.n):
                for j in range(self.n):
                    if self.res[k][i] == j:
                        print("Q", end=" ")
                    else:
                        print("*", end=" ")
                print()
            print()

    def __isPlace(self, qn:int, clm:int)-> bool:
        """qn is the queen number and clm is the index of column, 
        this function returns weather if the queen k can be placed at ith index or not"""
        for i in range(qn):
            if self.x[i] == clm:
                return False
            elif abs(i-qn) == abs(self.x[i] - clm):
                return False
        return True



    def solve(self,qn:int=0) -> None:
        """
        qn is number of queen to be placed in a n x n chess board
        """
        if qn == self.n:
            self.nos += 1
            self.res.append(self.x[:])
            return
        for clm in range(self.n):
            if self.__isPlace(qn,clm):
                self.x[qn] = clm
                self.solve(qn+1)
        return self.res
    
    def show(self):
        """
        This function used to show all the possibilities of n queens problem
        """
        if len(self.res) == 0:
            self.solve()
        self.__print_solution()

    def getPositions(self):
        """
        This function returns all the possible indexes of the n queens problem 
        """
        if not self.res:
            self.solve()
        return self.res

if __name__ == "__main__":
    obj = NQueens(8)
    obj.show()
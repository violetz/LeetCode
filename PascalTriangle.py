class PascalTriangle(object):
    def __init__(self):
        self.elements = []

    def __repr__(self):
        return str(self.elements)

    def generate(self, i_num_rows):
        if i_num_rows < 1:
            return
        if i_num_rows >= 1:
            self.elements = [[1]]
            for ith_row in range(2, i_num_rows + 1):
                ls_pre_row = self.elements[-1]
                ls_pre_row.append(0)
                ls_cur_row = []
                for ind_ele in range(len(ls_pre_row)):
                    ls_cur_row.append(ls_pre_row[ind_ele - 1] + 
                                      ls_pre_row[ind_ele])
                ls_pre_row.pop()
                self.elements.append(ls_cur_row)

    def get_row(self, ith_row):
        import math
        ls_cur_row = ([math.factorial(ith_row) /
        (math.factorial(ith_row - i) * math.factorial(i)) 
                       for i in range(ith_row + 1)])
        self.ith_row = ls_cur_row
        

def main(ith_row):
    p_tri = PascalTriangle()
    # p_tri.generate(30)
    p_tri.get_row(ith_row)
    print p_tri.ith_row
            
        

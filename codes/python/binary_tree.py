class BinarySearchTree:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

    

    def insert(self,val):
        
        if val==self.data: # to a void duplicate value 
            return
        
        if val<self.data:
            if self.left:
                self.left.insert(val)
            else:
                self.left=BinarySearchTree(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right=BinarySearchTree(val)


    def get_node_count(self) :
        count=1
        if self.right:
            count+=self.right.get_node_count()
        if self.left:
            count+=self.left.get_node_count()
        
        return  count


    def print_values(): pass
    def delet_tree():pass
    def is_in_tree():pass
    def get_height(): pass
    def get_min():pass
    def get_max():pass
    def is_binary_tree():pass
    def delete_vale():pass
    def get_succesor():pass




if __name__=='__main__':

    root=BinarySearchTree(10)
    root.insert(3)
    root.insert(1)
    count= root.get_node_count()
    print(count)


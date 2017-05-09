def insert_sort(self,lists):
    count=len(self.lists)
    for i in range(1,count):
        key=self.lists[i]
        j=i-1
        while j>=0:
            if self.lists[j]>key:
                self.lists[j+1]=self.lists[j]
                self.lists[j]=key
                j-=1
    return lists



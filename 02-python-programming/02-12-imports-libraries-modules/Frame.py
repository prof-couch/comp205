# library that implements a simplified DataFrame for instructional purposes.

class Frame:
    """ A small data frame package for illustration purposes """
    data = {}  # the ingested data as a dictionary
    titles = []  # a list of column headings
    def __init__(self, tuples=None): 
        if tuples is not None: 
            self.set(tuples)
        else: 
            data = {}
            
    def set(self, tuples):
        """ set the contents based upon a list of tuples """
        lists = []
        self.titles = []
        # first tuple consists of column titles 
        t = tuples[0]
        for name in t: 
            self.titles.append(name)
            lists.append([])
        for tup in tuples[slice(1,len(tuples))]: 
            for index in range(len(tup)): 
                lists[index].append(tup[index])
        self.data = {}
        for index in range(len(t)):
            self.data[self.titles[index]]=lists[index]

    def read(self, filename): 
        """ read contents from a csv file """
        f = open(filename, "r")
        tuples = []
        for line in f: 
            values = line.strip().split(',')
            # convert each field to a number if it can be converted. 
            for index in range(len(values)): 
                try: 
                    f = float(values[index])
                    values[index]=f
                except:
                    pass
            tuples.append(tuple(values))
        # Now make a file out of the read tuple
        self.set(tuples)
    
    def rows(self): 
        """ return number of rows """
        return len(self.data[self.titles[0]])
    
    def row(self, n): 
        """ return the tuple for a row n """
        out = []
        for t in self.titles:  # indexes of columns
            out.append(self.data[t][n])
        return tuple(out)
    
    def columns(self):
        """ return the number of columns """
        return len(self.titles)
    
    def column(self, n): 
        """ return column n """
        return self.data[self.titles[n]]
   
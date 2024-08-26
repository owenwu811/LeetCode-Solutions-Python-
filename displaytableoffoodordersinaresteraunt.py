
#medium
#75.0% acceptance rate
#1418

#Given the array orders, which represents the orders that customers have done in a restaurant. More specifically orders[i]=[customerNamei,tableNumberi,foodItemi] where customerNamei is the name of the customer, tableNumberi is the table customer sit at, and foodItemi is the item customer orders.

#Return the restaurant's “display table”. The “display table” is a table whose row entries denote how many of each food item each table ordered. The first column is the table number and the remaining columns correspond to each food item in alphabetical order. The first row should be a header whose first column is “Table”, followed by the names of the food items. Note that the customer names are not part of the table. Additionally, the rows should be sorted in numerically increasing order.


#my own solution using python3: (note this solution took me nearly a week of trial and error, but I finally did it):

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        res, foodnames = [], []
        for i in range(len(orders)):
            foodnames.append(orders[i][2])
        foodnames.append("Table")
        rd = set()
        for f in foodnames:
            rd.add(f)
        final1stcol = []
        for r in rd:
            final1stcol.append(r)
        ff = sorted(final1stcol)
        last = [0] * len(ff)
        last[0] = "Table"
        ff.remove("Table")
        for i in range(len(ff)):
            last[i + 1] = ff[i]
        #print(last)
        res.append(last)
        tablenames = []
        for i in range(len(orders)):
            tablenames.append(orders[i][1])
        settablenames = set()
        for t in tablenames:
            settablenames.add(t)
        finaltablenames = []
        for s in settablenames:
            finaltablenames.append(int(s))
        a = sorted(finaltablenames)
        #print(a)
        mydict = dict()
        for i in range(len(orders)):
            if orders[i][2] not in mydict:
                mydict[orders[i][2]] = 0
            mydict[orders[i][2]] += 1
        numberofextrar = len(a)
        for i in range(numberofextrar):
            res.append([])
        for i in range(len(res)):
            if i < len(a):
                res[i + 1].append(a[i])
        mydict = dict()
        items = res[0]
        #print(items) #['Table', 'Beef Burrito', 'Ceviche', 'Fried Chicken', 'Water']
        mydict = defaultdict(list)
        for i in range(len(orders)):
            if orders[i][2] in items: #"Beef Burrito"
                mydict[orders[i][1]].append(orders[i][2])
        for i in range(len(res[0]) - 1): #['Table', 'Beef Burrito', 'Ceviche', 'Fried Chicken', 'Water']
            for j in range(1, len(res)):
                res[j].append(0)
                #print(res)
        #fineprint(res) > [['Table', 'Beef Burrito', 'Ceviche', 'Fried Chicken', 'Water'], [3, 0, 0, 0, 0], [5, 0, 0, 0, 0], [10, 0, 0, 0, 0]]
        mydict = defaultdict(list)
        for i in range(len(orders)):
            if orders[i][2] in items: #"Beef Burrito"
                mydict[orders[i][1]].append(orders[i][2])
        #print(mydict) #{'3': ['Ceviche', 'Fried Chicken', 'Ceviche'], '10': ['Beef Burrito'], '5': ['Water', 'Ceviche']}
        #print(items) #['Table', 'Beef Burrito', 'Ceviche', 'Fried Chicken', 'Water']
        print(res) #[['Table', 'Beef Burrito', 'Ceviche', 'Fried Chicken', 'Water'], [3, 0, 0, 0, 0], [5, 0, 0, 0, 0], [10, 0, 0, 0, 0]]
        foodd = defaultdict(int) 
        print(res[0]) #['Table', 'Beef Burrito', 'Ceviche', 'Fried Chicken', 'Water']
        for i in range(len(orders)):
            tablenumber = int(orders[i][1])
            for j in range(len(res)):
                #print(foodd[orders[j][2]])
                #["David","3","Ceviche"]
                if res[j][0] == tablenumber and orders[i][2] in res[0]:
                    for a, k in enumerate(res[0]):
                        if k == orders[i][2]:
                            res[j][a] += 1
        for i in range(len(res)):
            for j in range(len(res[i])):
                res[i][j] = str(res[i][j])
        return res

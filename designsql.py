
#2408
#medium


#You are given n tables represented with two arrays names and columns, where names[i] is the name of the ith table and columns[i] is the number of columns of the ith table.

#You should be able to perform the following operations:

#Insert a row in a specific table. Each row you insert has an id. The id is assigned using an auto-increment method where the id of the first inserted row is 1, and the id of each other row inserted into the same table is the id of the last inserted row (even if it was deleted) plus one.
#Delete a row from a specific table. Note that deleting a row does not affect the id of the next inserted row.
#Select a specific cell from any table and return its value.
#Implement the SQL class:

#SQL(String[] names, int[] columns) Creates the n tables.
#void insertRow(String name, String[] row) Adds a row to the table name. It is guaranteed that the table will exist, and the size of the array row is equal to the number of columns in the table.
#void deleteRow(String name, int rowId) Removes the row rowId from the table name. It is guaranteed that the table and row will exist.
#String selectCell(String name, int rowId, int columnId) Returns the value of the cell in the row rowId and the column columnId from the table name.



#my own solution using python3:

class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.d = defaultdict(list)
        for i, n in enumerate(names):
            self.d[n].append(columns[i])

    def insertRow(self, name: str, row: List[str]) -> None:
        self.d[name].append(row)

    def deleteRow(self, name: str, rowId: int) -> None:
        if name in self.d[name]:
            self.d[name].remove(rowId)

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.d[name][rowId][columnId - 1]

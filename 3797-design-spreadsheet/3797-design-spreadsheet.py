class Spreadsheet:

    def __init__(self, rows: int):
        self.mapp = {}
        self.rows = rows
        
    def setCell(self, cell: str, value: int) -> None:
        self.mapp[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.mapp:
            del self.mapp[cell]

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        val1, val2 = formula.split("+")

        def get_cell_value(val):
            val = val.strip()
            if val.isdigit():
                return int(val)
            else:
                return self.mapp.get(val, 0)

        value1 = get_cell_value(val1)
        value2 = get_cell_value(val2)

        return value1 + value2
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
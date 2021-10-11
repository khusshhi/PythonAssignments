import pandas as pd

employees=[(1,'khushi',50000),(2,'sohit',45000),(2,'khushi',50000),(3,'dolly',40000),(4,'raghav',47000),(1,'khushi',50000),(2,'sohan',45000),(2,'sohit',45000),(5,'muskan',44000)]
df = pd.DataFrame(employees,
                  columns = ['EmpId', 'EmpName', 'EmpSalary'])
duplicate = df[df.duplicated('EmpName')]
print('duplicate rows: ')
print(duplicate)
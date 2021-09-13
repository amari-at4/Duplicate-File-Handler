# write your code here
with open('salary.txt') as monthly_file:
    with open('salary_year.txt', 'w') as yearly_file:
        yearly_file.writelines([str(int(monthly.rstrip('\n')) * 12) + '\n' for monthly in monthly_file])

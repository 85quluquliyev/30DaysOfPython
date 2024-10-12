# Ex1
"""
lst = []
lst = ['Xaliq','Siqura','Atie','Qulu']
father, *girls, son = lst
print(len(lst))
print(girls)
"""
#Ex2
"""
mixed_data_types = ['Qulu',24,183,{'marital status':'single'},{'address':'Boston,USA'}]
companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print('Number of company: ',len(companies))
print(companies[0],companies[2],companies[4])
companies.append('MSI')
companies.insert(1,"Xaoimi")
companies[0] = 'Facebook'.lower()
join_companies = '#; '.join(companies)
print(companies)
print(join_companies)
companies.sort()
print(companies)
companies.reverse()
print(companies)
"""
# Ex3
"""
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
first_three_companies = it_companies[:3]
print(first_three_companies)

last_three_companies = it_companies[-3:]
print(last_three_companies)
it_companies.pop(0)
it_companies.pop()
print(it_companies)
del it_companies
"""
# Ex4
"""
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
"""
# Ex5
"""
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
n = len(ages)
median = (ages[(n-1)//2] + ages[n//2])/2
print(median)
"""

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
n = len(ages)
min_age = min(ages)
max_age = max(ages)
average = sum(ages) / n
print(average)
min_avg_diff = abs(min_age - average)
max_avg_diff = abs(max_age - average)

# Step 3: Print the results
print(f"abs(min - average): {min_avg_diff}")
print(f"abs(max - average): {max_avg_diff}")
"""
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
ages_range = max(ages) - min(ages)
print(ages_range)
"""
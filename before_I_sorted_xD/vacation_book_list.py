book_pages = int(input())
pages_read_per_hour = int(input())
days_deadline = int(input())
hours_needed = book_pages // pages_read_per_hour
days_needed = hours_needed // days_deadline
print(days_needed)
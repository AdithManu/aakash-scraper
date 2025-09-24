from modules import extract_process, from_df, print_fails
from rank import print_rank


course = 'JEE'
json_data, fails = from_df()

print_rank(json_data, course=course)

print_fails(fails, course=course)



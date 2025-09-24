from modules import extract_process, from_df, print_fails
from rank import print_rank


# 1,1173754,410242120050 # jee
# 1,1173758,410241120106 # neet

# 1,1186662,410242120049

test_id = 1191081
course='JEE'

1191081


json_data, fails = extract_process(test_id=test_id,course=course)

# json_data, fails = from_df()

print_rank(json_data, course=course)

print_fails(fails, course=course)



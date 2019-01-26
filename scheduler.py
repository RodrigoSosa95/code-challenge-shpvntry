from copy import copy

# example input
user_list = list(range(1000, 3500))
TOTAL_MINUTES = 15

# not the best solution
def get_account_ids_to_run(account_ids_list):
    account_ids_to_return = []
    for _ in range(0, 15):
        account_ids_to_return.append([])

    total_users = len(account_ids_list)
    
    minute_interval = total_users % TOTAL_MINUTES

    for user_id in account_ids_list:
        index = account_ids_list.index(user_id)
        temp = minute_interval

        index_to_append = (index * temp + 10) % len(account_ids_to_return)
        account_ids_to_return[index_to_append].append(user_id)

    return account_ids_to_return


# simple solution perhaps?
def queue_users_in_time_range(account_ids_list):
    schedule = []
    for _ in range(0, 15):
        schedule.append([])

    account_index = 0
    while account_index <= len(account_ids_list):
        if account_index == account_ids_list.index(account_ids_list[-1]):
            print("All account id's have been run")
            break

        temp = copy(account_index)

        if temp >= 15:
            temp = (temp % 15) - 15
            schedule[temp].append(account_ids_list[account_index])
        else:
            schedule[temp].append(account_ids_list[account_index])

        account_index += 1
    return schedule
        

# for list in get_account_ids_to_run(user_list):
#     print(list)

for list in queue_users_in_time_range(user_list):
    print(list, end="\n \n")

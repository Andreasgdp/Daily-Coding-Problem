# string = 's'

# string_list = ['dog', 'deer', 'sweet', 'deal', 'steal', 'sucess']

# auto_list = []

# for i in string_list:
#     if i.startswith(string):
#         auto_list.append(i)

# print(auto_list)


prefix = 's'

string_list = ['dog', 'deer', 'sweet', 'deal', 'steal', 'sucess']


def autocomplete(prefix, string_list):
    auto_list = []

    for i in string_list:  # note 1
        if i.startswith(prefix):  # note 2
            auto_list.append(i)  # note 3

    return auto_list


final = autocomplete(prefix, string_list)
print(final)

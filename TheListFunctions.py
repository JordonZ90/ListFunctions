def list_functions():
    lucky_numbers = [4, 8, 15, 16, 23, 42]
    friends = ["Bob", "Kevin", "Grace", "Sara", "Victor"]
    friends.extend(lucky_numbers)  # Append lists together
    friends.append("Apollo")
    friends.insert(1, "Jimbo")
    friends.remove("Sara")
    # friends.clear()
    # friends.pop()  # Removes last element in the list
    print(friends.index("Bob"))
    friends.count("Jimbo")
    friends.sort()  # Sorts in ascending order
    lucky_numbers.reverse()  # Reverse the order of the list

    friends2 = friends.copy()  # Copies the list to another list


def list_index():
    friends = ["Bob", "Kevin", "Grace", "Sara", "Victor"]
    print(friends[0])
    print(friends[1])
    print(friends[2])
    print(friends[-1])
    print(friends[-2])
    print(friends[1:])
    print(friends[1:3])  # Up to but not including the 3rd index position


list_index()
# list_functions()

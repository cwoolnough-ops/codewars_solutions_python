###John has invited some friends. His list is:
#s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
#Could you make a program that
#makes this string uppercase
#gives it sorted in alphabetical order by last name.
#When the last names are the same, sort them by first name.
#Last name and first name of a guest come in the result between parentheses separated by a comma.
#So the result of function meeting(s) will be:
# "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"
# It can happen that in two distinct families with the same family name two people have the same first name too
def meeting(s):
    s = s.upper().split(";")
    new_list = [name.split(":") for name in s]
    names_dict = {}
    for name in new_list:
        try:
            names_dict[name[1]].append(name[0])
            names_dict[name[1]].sort()
        except KeyError:
            names_dict[name[1]] = [name[0]]
    last_names = sorted(names_dict)
    final_string = ""
    for last in last_names:
        for first_name in names_dict[last]:
            final_string += "({}, {})".format(last, first_name)
    return final_string

# test case
string = "Barney:Tornbull;Fred:Corwill;Wilfred:Corwill;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
print(meeting(string))

class Tool:
    def __init__(self, name, insert_number):
        self.name = name
        self.insert_number = insert_number

    def side(self):
        print(self.name + ' outside and insert number ' + self.insert_number)

my_tool_list = Tool('Turning', '1')
new_tool_list = Tool('Drilling', '3')

print(my_tool_list.side())
print(new_tool_list.side())

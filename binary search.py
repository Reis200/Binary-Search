# binary search
import sys

class Program:
    def __init__(self):
        self.list_input = input("Enter a list of sorted items seperated by commas e.g 1,2,3 or a,b,c,d:")
        self.list = self.list_input.split(",")
        print(self.list)
        self.list_type = input("Do you want to search a sorted list of text, numbers, or decimals: ")
        self.list_type = self.list_type.strip()
        self.list_type = self.list_type.lower()
        match self.list_type:
            case "t":
                self.list_type = "string"
            case "text":
                self.list_type = "string"
            case "texts":
                self.list_type = "string"
            case "n":
                self.list_type = "number"
            case "number":
                self.list_type = "number"
            case "numbers":
                self.list_type = "number"
            case "d":
                self.list_type = "decimal"
            case "decimal":
                self.list_type = "decimal"
            case "decimals":
                self.list_type = "decimal"
            case _:
                print("We could not identify the type of list please re-run and try again...")
                sys.exit()

        print(self.list_type + " search type has been selected")

        
    def binary_search(self):
        if self.list_type == "string":
            self.binary_search_string_list()
        elif self.list_type == "number":
            self.binary_search_integer_list()
        else:
            self.binary_search_decimal_list()
    
    def binary_search_string_list(self):
        item_found = False
        first = 0
        last = len(self.list)-1
        item_to_find = input("Enter the item that needs to be found by the linear search: ")
        item_to_find = item_to_find.strip()
        while item_found == False and first <= last:
            midpoint = (first + last) // 2
            if item_to_find == self.list[midpoint]:
                print("Item is found and at index " + str(midpoint))
                item_found = True
            else:
                if item_to_find > self.list[midpoint]:
                    first = midpoint + 1
                elif item_to_find < self.list[midpoint]:
                    last = midpoint - 1
                    
            

    def binary_search_integer_list(self):
        item_found = False
        first = 0
        last = len(self.list)-1
        item_to_find = input("Enter the item that needs to be found by the linear search: ")
        item_to_find = int(item_to_find.strip())
        self.list = [int(item.strip()) for item in self.list]
        while item_found == False and first <= last:
            midpoint = (first + last) // 2
            if item_to_find == self.list[midpoint]:
                print("Item is found and at index " + str(midpoint))
                item_found = True
            else:
                if item_to_find > self.list[midpoint]:
                    first = midpoint + 1
                elif item_to_find < self.list[midpoint]:
                    last = midpoint - 1

    def binary_search_decimal_list(self):
        item_found = False
        first = 0
        last = len(self.list)-1
        item_to_find = input("Enter the item that needs to be found by the linear search: ")
        item_to_find = float(item_to_find.strip())
        self.list = [float(item.strip()) for item in self.list]
        while item_found == False and first <= last:
            midpoint = (first + last) // 2
            if item_to_find == self.list[midpoint]:
                print("Item is found and at index " + str(midpoint))
                item_found = True
            else:
                if item_to_find > self.list[midpoint]:
                    first = midpoint + 1
                elif item_to_find < self.list[midpoint]:
                    last = midpoint - 1



program1 = Program()
program1.binary_search()

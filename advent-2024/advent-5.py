# https://adventofcode.com/2024/day/5

from pprint import pprint

class Node:
    def __init__(self, value, children=None):
        self.children = children if children is not None else set()
        self.value = value
    
    def __repr__(self):
        return(f"VALUE: {self.value}, BEFORE: {[child.value for child in self.children]}")
    
    def merge_with(self, node):
        if self.value == node.value:
            self.children = self.children.union(node.children)
        else:
            print("VALUES MISMATCH. CAN'T MERGE")

    def has_child(self, child_value):
        for node_child in self.children:
            if int(child_value) == int(node_child.value):
                return True
        return False

def follow_children_for_value(hierarchies, hierarchy, value, found=None, depth=0, path=None):
    if found is None:
        found = set()
    if path is None:
        path = [hierarchy.value]
    else:
        path = path + [hierarchy.value]
    
    found.add(hierarchy)
    
    for child in hierarchy.children:
        print(f"Examining child: {child.value}")
        
        if int(child.value) == int(value):
            print(f"FOUND! {value} is a direct child of {hierarchy.value}")
            print(f"Complete path to {value}: {path} → {child.value}")
            return True
        
        child_hierarchy = hierarchies.get(child.value)
        if child_hierarchy and child_hierarchy not in found:
            print(f"Exploring hierarchy of child: {child.value}")
            
            if follow_children_for_value(hierarchies, child_hierarchy, value, found, depth+1, path):
                print(f"Chain complete: {value} is a descendant of {hierarchy.value} through {child.value}")
                return True
    
    print(f"Finished checking all children of {hierarchy.value}, {value} not found in this branch")
    return False


def do_the_thing(items, hierarchies_2):
    for index, item in enumerate(items):
        for sub_item in items[index+1:]:
            if hierarchy := hierarchies_2.get(int(sub_item)):
                if hierarchy.has_child(item):
                    print(f"{hierarchy.value} has child: {item}")
                    return False
    return True


with open("./inputs-2024/input_5.txt","r", encoding="utf8") as file:
    hierarchies = []
    hierarchies_2 = {}
    codes_to_check = []
    for line in file:
        if "|" in line:
            [higher, lower] = line.split("|")
            lower = int(lower)
            higher = int(higher)
            new_node = Node(children={Node(value=lower)}, value=higher)
            if found := hierarchies_2.get(higher):
                found.merge_with(new_node)
            else:
                hierarchies_2[higher] = new_node
        else:
            codes_to_check.append(line.strip("\n").split(","))

    # go over each sequence
    running_valid_sum = 0
    running_sum = 0
    fixed_codes = []
    for items in codes_to_check:
        is_valid = True
        for index, item in enumerate(items):
            for sub_item in items[index+1:]:
                if hierarchy := hierarchies_2.get(int(sub_item)):
                    if hierarchy.has_child(item):
                        is_valid = False
                        new_list = []
                        # go through the whole list to construct a new one
                        for index, thing in enumerate(items):
                            index_to_append_to = 0

                            # if this item in the list has rules
                            if hierarchy := hierarchies_2.get(int(thing)):
                                p = 10
                            else:
                                hierarchy = Node(value=thing)

                            insert_index = 0
                            has_inserted = False

                            # go through our newly built list to find out where to insert
                            for sub_index, new_sub_item in enumerate(new_list):
                                # if new node needs to come bfore the thing we're looking at
                                # insert it here
                                if hierarchy.has_child(new_sub_item):
                                    has_inserted = True
                                    new_list.insert(sub_index, thing)
                                    break

                                # if going through the new list, an an item has rules
                                if sub_hierarchy := hierarchies_2.get(int(new_sub_item)):
                                    # check if the item in the list has to come before/the item
                                    # we're looking to add needs to come after
                                    if sub_hierarchy.has_child(hierarchy.value):
                                        insert_index = sub_index + 1
                                
                            if not has_inserted:
                                new_list.insert(insert_index, thing)

                        break

            if not is_valid:
                break
    
        if item != '':
            if is_valid:
                running_valid_sum += int(items[int(len(items)/2)])
            else:
                fixed_codes.append(new_list)
            running_sum += int(items[int(len(items)/2)])

new_rolling = 0
for x in fixed_codes:
    if not do_the_thing(x, hierarchies_2):
        import pdb;
        pdb.set_trace()
    else:
        new_rolling += int(x[int(len(x)/2)])

print("running_valid_sum: " + str(running_valid_sum))
print("running_sum: " + str(running_sum))
    

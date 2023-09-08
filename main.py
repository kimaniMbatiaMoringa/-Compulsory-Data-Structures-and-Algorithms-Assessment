import ipdb

def is_balanced(expression):
    content =[]
    for item in expression:
        if item in ["(","{","["]:
            content.append(item)
        else:
            if not content:
                return False
            current_char = content.pop()
            if current_char == '(':
                if item != ")":
                    return False
            if current_char == '{':
                if item != "}":
                    return False    
            if current_char == '[':
                if item != "]":
                    return False   
    
    if content:
        return False
    return True


def remove_duplicates(sequence):
    list_content = []
    for item in sequence:
        if item not in list_content:
            list_content.append(item)
    return list_content        
        
sequence1 = [2, 3, 2, 4, 5, 3, 6, 7, 5]

ipdb.set_trace()
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
    pass


ipdb.set_trace()
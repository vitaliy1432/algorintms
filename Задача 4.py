def get_tree(serialized):
    tree = {'left': None, 'right': None, 'up': None, 'type': 'root'}
    node = tree
    for i in serialized:
        if i == 'D':
            new_node = {'left': None, 'right': None, 'up': node, 'type': 'left'}
            node['left'] = new_node
            node = new_node
        elif i == 'U':
            while node['type'] == 'right':
                node = node['up']
            node = node['up']
            new_node = {'left': None, 'right': None, 'up': node, 'type': 'right'}
            node['right'] = new_node
            node = new_node
    return tree

def traverse(root, prefix):
    if root['left'] is None and root['right'] is None:
        return [''.join(prefix)]
    prefix.append('0')
    result = traverse(root['left'], prefix)
    prefix.pop()
    prefix.append('1')
    result.extend(traverse(root['right'], prefix))
    prefix.pop()
    return result

serialized_1 = 'DDUUDU'
print(f'Для {serialized_1} -- {traverse(get_tree(serialized_1), [])}')

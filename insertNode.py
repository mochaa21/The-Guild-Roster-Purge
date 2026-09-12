class GuildMembers:
    def __init__(ArielAshera, data):
        ArielAshera.data = data
        ArielAshera.next = None

def print_gm(node):
    currentNode = node
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

# -------- #
def insert_gm(head, newNode, position):
    if position == 1:
        newNode.next = head
        return newNode

    currentNode = head
    for i in range(position - 2):
        if currentNode.next == None:
            break
        currentNode = currentNode.next

    newNode.next = currentNode.next
    currentNode.next = newNode
    return head

def delete_gm(head, target_gm):
    if head.data == target_gm:
        return head.next
    currentNode = head
    if currentNode.next == None:
        return head
    while currentNode.next:
        if currentNode.next.data == target_gm:
            currentNode.next = currentNode.next.next
            break
        currentNode = currentNode.next
    return head

node1 = GuildMembers("Angelica ven Ashera")
node2 = GuildMembers("Serafina de Lavilliant")
node3 = GuildMembers("Emilia")
node4 = GuildMembers("Sylvie Leywin")
node5 = GuildMembers("Audrey Hall")
node6 = GuildMembers("Nephis")
node7 = GuildMembers("Alyssa Maclius")

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

print_gm(node1)

newNode = GuildMembers("Beatrice")
insert_gm(node1, newNode, 3)
delete_gm(node1, "Emilia")
print_gm(node1)
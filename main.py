class GuildMembers:
    def __init__(ArielAshera, data):
        ArielAshera.data = data
        ArielAshera.next = None

def print_gm(head):
    current = head
    while current:
        print(f"[{current.data}]", end=" -> ")
        current = current.next
    print("null")

def delete_gm(head, target_gm):
    if not head:
        return head
    if head.data == target_gm:
        return head.next
    current = head
    while current.next:
        if current.next.data == target_gm:
            current.next = current.next.next
            break
        current = current.next
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
new_gm = delete_gm(node1, "Emilia")
print_gm(new_gm)
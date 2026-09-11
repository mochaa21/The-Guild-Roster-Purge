class GuildMembers:
    def __init__(ArielAshera, data):
        ArielAshera.data = data
        ArielAshera.next = None

def print_gm(head):
    current = head
    while current:
        print(f"[{current.data}]", end=" -> ")
        current = current.next

def delete_gm(head, target_gm):
    if not head:
        return head.next

    if


node1 = GuildMembers("Angelica ven Ashera")
node2 = GuildMembers("Veera Voile")
node3 = GuildMembers("Emilia")
node4 = GuildMembers("Sylvie Leywin")

node1.next = node2
node2.next = node3
node3.next = node4

print_gm(node1)
delete_gm(node1, "Emilia")
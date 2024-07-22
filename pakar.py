import random

class Node:
    def __init__(self, question=None, yes_node=None, no_node=None, diagnose=None):
        self.question = question
        self.yes_node = yes_node
        self.no_node = no_node
        self.diagnose = diagnose

def build_tree():
    # Daun node yang berisi diagnosa
    atletis = Node(None, diagnose="Wah, kayaknya kamu bakal jadi atlet nih!")
    gamer = Node(None, diagnose="Kamu suka main game ya? Keren!")
    olahragawan = Node(None, diagnose="Kamu punya bakat jadi atlet atau olahragawan!")
    pemalas = Node(None, diagnose="Mending cari hobi lain yang lebih produktif deh.")

    # Daftar pertanyaan yang akan dipilih secara acak
    questions = [
        "Kamu suka olahraga ga? (ya/ga): ",
        "Kamu doyan main game ga? (ya/ga): ",
        "Kamu suka nonton olahraga? (ya/ga): ",
        "Sering gerak atau olahraga ga? (ya/ga): ",
        "Minat sama olahraga ga? (ya/ga): ",
        "Suka ikutan aktivitas olahraga ga? (ya/ga): ",
        "Pengen belajar atau tingkatin kemampuan olahraga ga? (ya/ga): ",
        "Olahraga jadi bagian penting buat hidupmu ga? (ya/ga): "
    ]

    # Pertanyaan-pertanyaan
    random.shuffle(questions)  # Acak urutan pertanyaan
    node1 = Node(questions[0], yes_node=atletis, no_node=gamer)
    node2 = Node(questions[1], yes_node=gamer, no_node=olahragawan)
    node3 = Node(questions[2], yes_node=olahragawan, no_node=pemalas)
    node4 = Node(questions[3], yes_node=node1, no_node=node2)
    node5 = Node(questions[4], yes_node=node2, no_node=node3)
    node6 = Node(questions[5], yes_node=node3, no_node=node4)
    node7 = Node(questions[6], yes_node=node4, no_node=node5)
    node8 = Node(questions[7], yes_node=node5, no_node=node6)

    return node8  # Mengembalikan node terakhir yang telah berisi semua pertanyaan

def system_diagnosa(node):
    while node.question:
        answer = input(node.question).lower()
        if answer == "ya":
            node = node.yes_node
        elif answer == "ga":
            node = node.no_node
        else:
            print("Jawab ya atau ga.")
    print("Hasil diagnosa: ", node.diagnose)

def main():
    print("Sistem Diagnosa Minat dan Bakat Olahraga")
    root = build_tree()
    system_diagnosa(root)

if __name__ == '__main__':
    main()

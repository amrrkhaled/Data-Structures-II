from RedBlackTree.red_black_tree import RedBlackTree

class DictionaryApp:
    def __init__(self, dictionary_file):
        self.dictionaryRBT = RedBlackTree()
        self.load_dictionary(dictionary_file)

    def load_dictionary(self, dictionary_file):
        with open(dictionary_file, "r") as file:
            for line in file:
                word = line.strip().lower()
                self.dictionaryRBT.insert(word)
        print("Dictionary loaded into Red-Black Tree successfully....!")
        self.validation()

    def validation(self):
        self.dictionaryRBT.print_tree_size()
        self.dictionaryRBT.print_height()
        self.dictionaryRBT.print_black_height()
        print("-------------------------------------------------")

    def lookup_word(self):
        print("-> Enter the word to look-up in Dictionary:")
        word = input().strip().lower()
        node = self.dictionaryRBT.searchTree(word)
        if node == self.dictionaryRBT.NIL:
            print("NO:(")
        else:
            print("YES:)")
    
    def insert_word(self):
        print("-> Enter the word to insert in Dictionary:")
        word = input().strip().lower()
        node = self.dictionaryRBT.searchTree(word)
        if node == self.dictionaryRBT.NIL:
            self.dictionaryRBT.insert(word)
            print("Word Inserted in Dictionary.")
            with open("Dictionary.txt", "a") as file:
                file.write(f"{word}\n")
                self.validation()
        else:
            print("ERROR!! Word already exists in Dictionary.")
        

    def start(self):
        print("** Welcome to our Dictionary **")
        self.validation()
        while True:
            print("-> Please select an option <-")
            print("Press 1 to look-up a word in Dictionary")
            print("Press 2 to insert a word in Dictionary")
            print("Press 3 to exit")

            try:
                inputChoice = int(input())
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if inputChoice == 1:
                self.lookup_word()
            elif inputChoice == 2:
                self.insert_word()
            elif inputChoice == 3:
                self.validation()
                print("Exiting the program...")
                break
            else:
                print("Invalid Input. Please try again.")


if __name__ == "__main__":
    app = DictionaryApp("Dictionary.txt")
    app.start()
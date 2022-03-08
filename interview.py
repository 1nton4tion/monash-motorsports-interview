import json, random, string, time
import matplotlib.pyplot as plt
from typing import List, Callable

class WordHandler():
    
    def __init__(self, word_list: List[str] = []) -> None:
        self.words: List[str] = word_list

    def insert(self, index: int, input_word: str) -> None:
        """
        Inserts a word (input_word) at the index specified in the list.

        Can be written using python inbuilt functions as:
        self.words.insert(index, input_word)

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if index == len(self.words):
            self.words.append(input_word)
        elif 0 <= index and index < len(self.words):
            self.words = [self.words[i] if i < index else input_word if i == index else self.words[i-1] for i in range(len(self.words)+1)]
        else:
            raise ValueError(f"index, {index} out of range")
        # print(f"{input_word} was inserted into the list at index, {index}")

    def search(self, input_word: str) -> int:
        """
        Returns the first index of an input word in the word list if it exists, otherwise raises a ValueError

        Time Complexity: O(n*s) where s is the length of the input string
        Space Complexity: O(1)
        """
        
        for i in range(len(self.words)):
            word = self.words[i]
            if word == input_word:
                return i
            
        raise ValueError(f"{input_word} does not exist in word list")

    def delete(self, input_word: str) -> None:
        """
        Deletes the first instance of an input word in the word list if it exists, otherwise raises a ValueError

        Time Complexity: O(n*s) where s is the length of the input string
        Space Complexity: O(n)
        """

        i = self.search(input_word)
        self.words = self.words[:i] + self.words[i+1:]

    def __str__(self):
        return str(self.words)

    def __len__(self):
        return len(self.words)



class Tester():

    def __init__(self, word_list: List[str]):
        self.word_handler_list = []
        for i in range(1, len(word_list), 10000):
            handler = WordHandler(random.choices(word_list, k=i))
            self.word_handler_list.append(handler)


    def check_time_complexity_insert(self) -> None:
        """
        plots the time taken vs n for insert function
        """
        x = []
        y = []
        for handler in self.word_handler_list:
            start = time.time()
            handler.insert(len(handler)-1, 'asdf')
            end = time.time()
            x.append(len(handler))
            y.append(end - start)
        plt.figure(1)
        plt.scatter(x, y)
        plt.show()

    def check_time_complexity_search(self) -> None:
        """
        plots the time taken vs n for insert function
        """
        x = []
        y = []
        for handler in self.word_handler_list:
            start = time.time()
            handler.search(handler.words[-1])
            end = time.time()
            x.append(len(handler))
            y.append(end - start)
        plt.figure(2)
        plt.scatter(x, y)
        plt.show()

    def check_time_complexity_delete(self) -> None:
        """
        plots the time taken vs n for insert function
        """
        x = []
        y = []
        for handler in self.word_handler_list:
            start = time.time()
            handler.delete(handler.words[-1])
            end = time.time()
            x.append(len(handler))
            y.append(end - start)
        plt.figure(3)
        plt.scatter(x, y)
        plt.show()



if __name__ == '__main__':
    WORD_LIST = [''.join(random.choice(string.ascii_letters) for i in range(random.randint(1, 5))) for _ in range(1, 1000000)]
    
    tester = Tester(WORD_LIST)

    tester.check_time_complexity_insert()
    tester.check_time_complexity_delete()
    tester.check_time_complexity_search()




class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = defaultdict(int)  # Stores frequency of sentences at this node


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.children = {}
        self.sentences = defaultdict(int)  # Stores frequency of sentences at this node

    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.history = ""  # Tracks current prefix
        self.sentence_freq = defaultdict(int)  # Global frequency tracker

        # Insert initial sentences into Trie
        for sentence, freq in zip(sentences, times):
            self._insert(sentence, freq)

    def _insert(self, sentence, count):
        """Inserts a sentence into the Trie and updates frequency."""
        node = self.root
        self.sentence_freq[sentence] += count  # Update frequency map

        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.sentences[sentence] = self.sentence_freq[sentence]  # Store frequency

    def _search(self, prefix):
        """Returns the top 3 sentences matching a given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        # Sort by frequency (descending), then lexicographically
        return heapq.nsmallest(
            3, node.sentences.keys(), key=lambda x: (-node.sentences[x], x)
        )

    def input(self, c: str) -> List[str]:
        if c == "#":
            self._insert(self.history, 1)  # Store the new sentence in Trie
            self.history = ""  # Reset prefix
            return []

        self.history += c
        return self._search(self.history)


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

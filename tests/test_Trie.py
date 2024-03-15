from katas import day1

def test_Trie():
    trie = day1.Trie()
    trie.insert("foo")
    trie.insert("fool")
    trie.insert("foolish")
    trie.insert("bar")

    assert sorted(trie.find("fo")) == [
        "foo",
        "fool",
        "foolish",
    ]

    trie.delete("fool")

    assert sorted(trie.find("fo")) == [
        "foo",
        "foolish",
    ]

# atcoder
## input
ref: [Pythonで使う競技プログラミング用チートシート - Qiita](https://qiita.com/_-_-_-_-_/items/34f933adc7be875e61d0)

文字列で読み込まれるので数値はintにキャストするのを忘れない。

|Input|script|結果|
|:-|:-|:-|
|abcde|s=input()|s='abcde'|
|abcde|s=list(input())|s=['a', 'b', 'c', 'd', 'e']|
|5(1つだけ)|a=int(input())|a=5|
|1 2|x,y = map(int,input().split())|x=1,y=2|
|1 2 3 4 5 ... n|li = input().split()|li=['1','2','3',...,'n']|
1 2 3 4 5 ... n|li = list(map(int,input().split()))|li=[1,2,3,4,5,...,n]|
FFFTFTTFF|li = input().split('T')|li=['FFF', 'F', '', 'FF']|

## sorted
ref: [Pythonソートチートシート - Qiita](https://qiita.com/tag1216/items/95dc6bff5422e26601bf)

tupleの場合要素をすべて比較して昇順に並べる。

```
>>> a = [("b", 3, 1), ("b", 1, 2), ("a", 1, 3), ("a", 1, 4), ("c", 2, 5)]
>>> sorted(a)
[('a', 1, 3), ('a', 1, 4), ('b', 1, 2), ('b', 3, 1), ('c', 2, 5)]
```

itemgetterで簡単に要素を指定できる。tupleのときも使える。

```
>>> a = [{"key1": 3}, {"key1": 1}]
>>> from operator import itemgetter
>>> sorted(a, key=itemgetter("key1"))
[{'key1': 1}, {'key1': 3}]
>>> sorted(a, key=lambda x: x["key1"]) # これと同じ
```

`reverse=True` で降順もできるが、入力時に符号を反転させた複合ソートのとき都合が良い。

```
>>>> sorted(a, reverse=True)
[3, 2, 1]
>>>> b = [('a', 3), ('a', 2), ('b', 2), ('b', 4)]
>>> sorted(b)
[('a', 2), ('a', 3), ('b', 2), ('b', 4)]
>>>> c = [('a', -3), ('a', -2), ('b', -2), ('b', -4)]
>>> sorted(c)
>>>> sorted(c)
[('a', -3), ('a', -2), ('b', -4), ('b', -2)]
```

#string similarity finder
string1 = '''Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.'''
string2 = '''Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[29]Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.[30]'''

#tokenization
token1 = string1.split()
token2 = string2.split()

#Remove stop words ->helping verb, conjunction,interjectio,articles.....
#import nltk
#nltk.download('stopwords')

from nltk.corpus import stopwords
stopwords = stopwords.words('english')

for word in stopwords:
    if word in token1:
        token1.remove(word)
    if word in token2:
        token2.remove(word)

set1 = set(token1)
set2 = set(token2)

uni = set1.union(set2)
inter = set1.intersection(set2)

ji = (len(inter)/len(uni))*100
print(ji,"%")

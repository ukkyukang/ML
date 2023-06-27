from sklearn import tree
x = [
    [0,0],
    [1,1]
]
y = [0,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

# predict
ret = clf.predict(
    [
        [2.,2.,]
    ]
)
print(ret)

# As a alternative to outputting a specific class, the probability of each class can be predicted
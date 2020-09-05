# Trees
A binary tree is a tree data structure where each node has up to two child nodes, creating the branches of the tree. The two children are usually called the left and right nodes. Parent nodes are nodes with children, while child nodes may include references to their parents.

## Challenge
the challenge was how to write the code from your mind without videos but without success


## Approach & Efficiency
I watched videos until understanding then I wrote the code

preOrder,inOrder,postOrder ===> O(n)
add,contains ===> O(log n)

## API
**Create a Node class** that has properties for the value stored in the node, the left child node, and the right child node.

**Create a BinaryTree class**

Define a method for each of the depth first traversals called preOrder, inOrder, and postOrder which returns an array of the values, ordered appropriately.

Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

**Create a BinarySearchTree class**

Define a method named add that accepts a value, and adds a new node with that value in the correct location in the binary search tree.

Define a method named contains that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.
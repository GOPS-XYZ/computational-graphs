import tensorflow as tf

# Nodes: operators, variables and constants
# Edges: tensors
a = tf.add(2, 3)
print(a)
b = tf.add(3.0, 5.0)
print(b)

# Create a session
# sess.run(x)    x <= whole graph or a node of a graph
sess = tf.Session()
print(sess.run(a))
print(sess.run(b))
sess.close()

# with clause take care of sess.close()
with tf.Session() as sess:
    print(sess.run(a))

# tf.Session()
# A Session object encapsulates the environment in which
# Operation objects are executed,
# and Tensor objects are evaluated.
import tensorflow as tf
#Note: Input floating point values
#Note: tf.divide(x,y)
#Note: tf.sqrt()
x = tf.constant(2.0,name='x')
y = tf.constant(3.0,name='y')

add = tf.add(x,y)
add1 = tf.add(x,y)
mul = tf.multiply(add,y)
mul1 = tf.multiply(add1,y)
add2 = tf.add(mul,mul1)
div = tf.divide(add1,y)
mul3 = tf.add(add2,div)

with tf.Session() as sess:
    writer = tf.summary.FileWriter('graph_assgn1',sess.graph)
    print(sess.run(mul3))
writer.close()
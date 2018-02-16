import tensorflow as tf

x = tf.constant(2.0,name="x")
y = tf.constant(3.0,name="y")

const1 = tf.constant(2.0,name='2')
const2 = tf.constant(1.0,name='1')

a = tf.multiply(x,const1)
b = tf.multiply(a,y)
c = tf.sqrt(const2)
d = tf.multiply(c,a)
e = tf.add(const2,d)
f = tf.sqrt(e)
g = tf.multiply(f,a)
h = tf.add(e,g)
i = tf.div(h,y)

with tf.Session() as sess:
    writer = tf.summary.FileWriter('graph_assgn2',sess.graph)
writer.close()
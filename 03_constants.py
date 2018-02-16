import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

# Constants and Variables
# tf.constant(value, dtype=None, shape=None, name='Const', verify_shape=False)

# a = tf.constant(2,shape=[2,2],verify_shape=True)
# This will throw an error "Tensor's shape: (2,2), got ().
# By default verify_shape = False
a = tf.constant(2,shape=[2,2])
print(a)

# Enter below code in console
# tf.InteractiveSession()
# a.eval()

b = tf.constant([2,1],shape=[3,4])
print(b)

with tf.Session() as sess:
    print(sess.run([a,b]))


W = tf.Variable(tf.zeros([2,3]))
b = tf.Variable(tf.zeros([3]))
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run([W,b]))


x = tf.placeholder(tf.float32, shape=[None, 784])

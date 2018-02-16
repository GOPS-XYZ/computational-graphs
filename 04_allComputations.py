import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

x = tf.constant(2)
y = tf.constant(3)

op1 = tf.add(x,y)
op2 = tf.multiply(x,y)
useless = tf.multiply(x,op1)
op3 = tf.pow(op2,op1)
print(op3,x,y,op1,op2,useless)
# Saves computation

# Create a Session
with tf.Session() as sess:
    op = sess.run(op3)
    print(op)
    writer = tf.summary.FileWriter('graphs2',sess.graph)
writer.close()

with tf.Session() as sess:
    op3, not_useless = sess.run([op3, useless])
    # tf.Session.run(fetches, feed_dict=None, options=None, run_metadata=None)
    # Pass all the variables whose value u want 2 list in fetches

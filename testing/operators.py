import tensorflow as tf

## Creating Operators
'''
The list of operators in tensorflow
tf.add(a,b)
tf.subtract(a,b)
tf.multiply(a,b)
tf.div(a,b)
tf.pow(a,b)
tf.exp(a)
tf.sqrt(a,b)
'''
x = tf.constant([2.0], dtype= tf.float32)
print(tf.sqrt(x))

# Adding
tensor_a = tf.constant([[1,2]],dtype=tf.int32)
tensor_b = tf.constant([[3,4]],dtype= tf.int32)

tensor_add = tf.add(tensor_a,tensor_b)
print(tensor_add)

with tf.Session() as sess:
	print(sess.run(tensor_add))

# Multiply 

tensor_multiply = tf.multiply(tensor_a,tensor_b)
with tf.Session() as sess:
	print(sess.run(tensor_multiply))
import tensorflow as tf
import numpy as np

#Defining the variables

X_1 = tf.placeholder(tf.float32, name="X_1")
X_2 = tf.placeholder(tf.float32, name="X_2")

# Defining the computation

multiply = tf.multiply(X_1,X_2, name="multiply")

#Execute the operation
with tf.Session() as session:
	result = session.run(multiply, feed_dict={X_1:[1,2,3],X_2:[4,5,6]})
	print(result)

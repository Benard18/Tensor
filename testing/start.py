import tensorflow as tf

# initializing two constants
x1 = tf.constant([1,2,3,4])
x2 = tf.constant([5,6,7,8])

# Multiply
result = tf.multiply(x1,x2)

#Intialize the session

# sesh = tf.Session()

# #Print the result
# print(sesh.run(result))

# ##Closing the sesh
# sesh.close()

with tf.Session() as sesh:
	output = sesh.run(result)
	print(output)
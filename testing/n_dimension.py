import tensorflow as tf
'''
tf.constant(value, dtype, name= "")
arguements

-`value`:Value of n dimension to define the tensor. Optional
-`dtype`: Define the type of data:
	- `tf.string`: String variable
	- `tf.float32`: Float variable
	-`tf.int16`: Integer variable
- "name": Name of the tensor. Optional. By default, `Const_1:0`	
'''
r1 = tf.constant(1, tf.int16)
print(r1)

## Named my_scalar
r2 = tf.constant(1,tf.int16, name="my_scalar")
print(r2)

##Decimal
r1_decimal = tf.constant(1.12345,tf.float32)
print(r1_decimal)
#String
r1_string = tf.constant("DamnSON", tf.string)
print(r1_string)

## A tensor of dimension 1 can be created as follows

r1_vector = tf.constant([1,3,5],tf.int16)
print(r1_vector)
r2_bool = tf.constant([True,True,False], tf.bool)

print(r2_bool)


## Learning on creating matrices with two dimensions

r2_matrix = tf.constant([[1,2],[3,4]],tf.int16)
print(r2_matrix)

## matrices with 3 dimensions

r3_matrix = tf.constant([[[1,2],[3,4],[5,6]]],tf.int16)
print(r3_matrix)
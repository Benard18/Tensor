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

## Shape of tensor

m_shape = tf.constant([ [10,11],[12,13],[14,15]])
print(m_shape.shape)

## Creating a 1D tensor
print(tf.zeros(10))

## Creating a 10x10 matrix
print(tf.ones([10,10]))

## Create a vector of ones with the same number of rows as m_shape
print(tf.ones(m_shape.shape[0]))

# Create a vector of ones with the same number of column as m_shape with the second number.
print(tf.ones(m_shape.shape[1]))

### Types of data
print(m_shape.dtype)

### Changing type of data
type_float = tf.constant(3.123456789, tf.float32)
type_int = tf.cast(type_float, dtype=tf.int32)
print(type_float.dtype)
print(type_int.dtype)


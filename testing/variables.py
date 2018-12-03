import tensorflow as tf
'''
tf.get_variable(name="",values, dtype, intializer)
arguements
- `name = ""`:Name of the variable
- `Values`: Dimension of the tensor
-`dtype`: Type of the data (optional)
-`intializer`: How to intialize the tensor. Optional
If initializer is specified, there is no need to include the the `values` as the shape of `initializer` is used.
'''

# Create a Variable 
# Create a 2 Rendomized values
var=tf.get_variable("var",[1, 2])

print(var.shape)

# Creating with one row and two columns. You need to use [1,2] to create the dimension of the variable

var_init_1 = tf.get_variable("var_init_1",[1,2],dtype=tf.int32,initializer=tf.zeros_initializer)
print(var_init_1.shape)

#Create a 2x2 matrix
tensor_const = tf.constant([[10,20],[30,40]])

#Initialize the first value of the tensor equals to tensor_const
var_init_2=tf.get_variable("var_init_2",dtype=tf.int32,initializer=tensor_const)
print(var_init_2.name)
print(var_init_2.shape)


import list_ds
import tuple_ds

my_list = list_ds.create_list()
list_ds.add_element(my_list, 5)

my_tuple = tuple_ds.create_tuple([1,2,3,4])
print(my_tuple)
print(tuple_ds.length(my_tuple)) # Uses custom function 

#print(len(my_tuple)) This won't print 'Calaculating length' as it uses in-built Python function
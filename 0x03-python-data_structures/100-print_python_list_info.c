#include <Python.h>

/**
 * print_python_list_info - prints basic info about python list objects.
 * @p: address of a PyObject struct representing a list object.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t allocation, size, i;

	size = PyList_Size(p);

	/* typecast so the 'allocated' field is available */
	allocation = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocation);
	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, (Py_TYPE(PyList_GetItem(p, i)))->tp_name);
	}
}

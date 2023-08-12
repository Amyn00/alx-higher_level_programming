#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	long int size = Py_SIZE(p), i;
	PyListObject *list = (PyListObject *)p;
	PyObject *item;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

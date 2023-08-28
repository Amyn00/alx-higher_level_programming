#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - print python list
 * @p: input
 */
void print_python_list(PyObject *p)
{
	PyListObject *l = (PyListObject *)p;
	Py_ssize_t i, size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", Py_SIZE(l));
	printf("[*] Allocated = %ld\n", l->allocated);

	for (i = 0, size = Py_SIZE(l); i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(l->ob_item[i])->tp_name);
		if (PyBytes_Check(l->ob_item[i]))
			print_python_bytes(l->ob_item[i]);
		else if (PyFloat_Check(l->ob_item[i]))
			print_python_float(l->ob_item[i]);
	}
}
/**
 * print_python_bytes - print python bytes
 * @p: input
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t i, size;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", Py_SIZE(bytes));
	printf("  trying string: %s\n", PyBytes_AS_STRING(bytes));
	printf("  first 10 bytes:");
	size = Py_SIZE(bytes) + 1;
	if (size > 10)
		size = 10;
	for (i = 0; i < size; i++)
		printf(" %02x", (unsigned char)PyBytes_AS_STRING(bytes)[i]);
	printf("\n");
}
/**
 * print_python_float - print python float
 * @p: input
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *flt_obj = (PyFloatObject *)p;
	double val;

	printf("[.] float object info\n");
	val = flt_obj->ob_fval;
	printf("  value: %f\n", val);
}

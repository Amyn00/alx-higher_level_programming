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
	PyListObject *list = (PyListObject *)p;
}
/**
 * print_python_bytes - print python bytes
 * @p: input
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
}
/**
 * print_python_float - print python float
 * @p: input
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *flt_obj = (PyFloatObject *)p;
}

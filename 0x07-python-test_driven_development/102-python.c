#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string.
 *
 * Return: Nothing.
 */
void print_python_string(PyObject *p)
{
	long int l;

	fflush(stdout);

	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	l = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		printf("  type: compact unicode object\n");
	}
	else
	{
		printf("  type: compact ascii\n");
	}
	printf("  length: %ld\n", l);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &l));
}

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
	Py_ssize_t length;
	const wchar_t *value = PyUnicode_AsUnicode(p);

	printf("[.] string object info\n");

	if (PyUnicode_Check(p))
	{
		if (PyUnicode_IS_COMPACT_ASCII(p))
		{
			printf("  type: compact ascii\n");
		}
		else
		{
			printf("  type: compact unicode object\n");
		}

		length = PyUnicode_GET_LENGTH(p);
		printf("  length: %ld\n", length);
		printf("  value: %ls\n", value);
	}
	else
	{
		printf("  [ERROR] Invalid String Object\n");
	}
}

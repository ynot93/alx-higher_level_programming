#define PY_SSIZE_T_CLEAN
#include "Python.h"

void print_python_string(PyObject *p)
{
	if (PyUnicode_Check(p))
	{
		Py_UCS4 *wstr = PyUnicode_AS_UCS4(p);
		Py_ssize_t length = PyUnicode_GET_LENGTH(p);

		printf("[.] string object info\n");

		if (PyCompactUnicode_Check(p))
			printf("  type: compact unicode object\n");
		else if (PyASCII_WCHAR_COMPACT_ASCII_Check(p))
			printf("  type: compact ascii\n");
		else
		{
			printf("  [ERROR] Invalid String Object\n")
				return;
		}

		printf("  length: %ld\n", length);
		printf("  value: %ls\n", wstr);
	}
	else
	{
		printf("  [ERROR] Invalid String Object\n");
	}
}

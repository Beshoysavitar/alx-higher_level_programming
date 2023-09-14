#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_bytes - ***
 * @p: ***
 */
void print_python_bytes(PyObject *p)
{
	unsigned char q, x;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		x = 10;
	else
		x = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", x);
	for (q = 0; q < x; q++)
	{
		printf("%02hhx", bytes->ob_sval[q]);
		if (q == (x - 1))
			printf("\n");
		else
			printf(" ");
	}
}
/**
 * print_python_list - ***
 * @p: ***
 */
void print_python_list(PyObject *p)
{
	int x, y, q;
	const char *t;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	x = var->ob_size;
	y = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", x);
	printf("[*] Allocated = %d\n", y);

	for (q = 0; q < x; q++)
	{
		t = list->ob_item[q]->ob_type->tp_name;
		printf("Element %d: %s\n", q, t);
		if (strcmp(t, "bytes") == 0)
			print_python_bytes(list->ob_item[q]);
	}
}

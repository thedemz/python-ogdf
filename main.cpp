#include <ogdf/basic/Graph.h>
#include <ogdf/basic/GraphAttributes.h>
#include <ogdf/fileformats/GraphIO.h>
#include <Python.h>

using namespace ogdf;

//Method
static PyObject *
spam_system(PyObject *self, PyObject *args)
{
    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    
    sts = system(command);
    
    Graph G;
    GraphAttributes GA(G, GraphAttributes::nodeGraphics | GraphAttributes::edgeGraphics );

	const int LEN = 11;
	for(int i = 1; i<LEN; ++i) {
		node left = G.newNode();
		GA.x(left) = -5*(i+1);
		GA.y(left) = -20*i;
		GA.width(left) = 10*(i+1);
		GA.height(left) = 15;

		node bottom = G.newNode();
		GA.x(bottom) = 20*(LEN-i);
		GA.y(bottom) = 5*(LEN+1-i);
		GA.width(bottom) = 15;
		GA.height(bottom) = 10*(LEN+1-i);

		edge e = G.newEdge(left,bottom);
		DPolyline &p = GA.bends(e);
		p.pushBack(DPoint(10,-20*i));
		p.pushBack(DPoint(20*(LEN-i),-10));
	}

	GraphIO::writeGML(GA, "manual_graph.gml");
	GraphIO::drawSVG(GA, "manual_graph.svg");
    
    return PyLong_FromLong(sts);
}


//Method declarations
static PyMethodDef SpamMethods[] = {
    {"system",  spam_system, METH_VARARGS,
     "Execute a shell command."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};


//Module declaration
static struct PyModuleDef spammodule = {
   PyModuleDef_HEAD_INIT,
   "spam",   /* name of module */
   NULL, /* module documentation, may be NULL */
   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   SpamMethods
};

//Module initialization
PyMODINIT_FUNC
PyInit_ogdf(void)
{
    return PyModule_Create(&spammodule);
}

// ====== Includes

#include <iostream.h>
#include <string.h>

// ====== Defines

#define BOOL int
#define FALSE 0
#define TRUE 1

// ====== Consts

const int
	stringSize = 100,
	tableSize = 5;

// ====== Typedefs

typedef char TString [stringSize];

/*
Having a string class with a < and = operator and some extra's would allow the use of
C++ function templates, but the point here is to illustrate that the template pattern
doesn't need them.
*/

// ====== Classes

class TSortableTable {
public:
	void initEntries ();  // Some compilers construct VFT at end of constructor
	void sort ();
protected:
	virtual void initEntry (int index) = 0;
	virtual BOOL pairWrongOrder (int index) = 0;
	virtual void swapPair (int index) = 0;
};

class TNumberTable: public TSortableTable {
public:
	float entries [tableSize];  // Normally protected or private
protected:
	virtual void initEntry (int index);
	virtual BOOL pairWrongOrder (int index);
	virtual void swapPair (int index);
};

class TStringTable: public TSortableTable {
public:
	TString entries [tableSize];  // Normally protected or private
protected:
	virtual void initEntry (int index);
	virtual BOOL pairWrongOrder (int index);
	virtual void swapPair (int index);
};

// ====== Global functions

// --- Main program function

int main () {
	cout << endl << endl;

	// Number table

	TNumberTable numberTable;
	numberTable.initEntries ();

	numberTable.entries [0] = 3;
	numberTable.entries [1] = 1;
	numberTable.entries [2] = 2;

	cout << "Number table before sorting" << endl;
	{for (int i = 0; i < tableSize; i++) {
		cout << numberTable.entries [i] << endl;
	}}

	numberTable.sort ();

	cout << "Number table after sorting" << endl;
	{for (int i = 0; i < tableSize; i++) {
		cout << numberTable.entries [i] << endl;
	}}

	// String table

	TStringTable stringTable;
	stringTable.initEntries ();

	strcpy (stringTable.entries [0], "Jan");
	strcpy (stringTable.entries [1], "Piet");
	strcpy (stringTable.entries [2], "Marie");

	cout << "String table before sorting" << endl;
	{for (int i = 0; i < tableSize; i++) {
		cout << stringTable.entries [i] << endl;
	}}

	stringTable.sort ();

	cout << "String table after sorting" << endl;
	{for (int i = 0; i < tableSize; i++) {
		cout << stringTable.entries [i] << endl;
	}}


	return 0;
}

// ====== Member functions

// Member functions of class TSortableTable

void TSortableTable::initEntries () {
	{for (int i = 0; i < tableSize; i++) {
		initEntry (i);
	}}
}

void TSortableTable::sort () {
	BOOL swapDone;
	do {
		swapDone = FALSE;
		{for (int i = 0; i < tableSize - 1; i++) {
			if (pairWrongOrder (i)) {
				swapPair (i);
				swapDone = TRUE;
			}
		}}
	} while (swapDone);
}

// Member functions of class TNumberTable

void TNumberTable::initEntry (int index) {
	entries [index] = 0;
}

BOOL TNumberTable::pairWrongOrder (int index) {
	return entries [index] > entries [index + 1];
}

void TNumberTable::swapPair (int index) {
	int parkplatz;

	parkplatz = entries [index];
	entries [index] = entries [index + 1];
	entries [index + 1] = parkplatz;
}

// Member functions of class TStringTable

void TStringTable::initEntry (int index) {
	strcpy (entries [index], "-");
}

BOOL TStringTable::pairWrongOrder (int index) {
	return strcmp (entries [index], entries [index + 1]) > 0;
}

void TStringTable::swapPair (int index) {
	TString parkplatz;

	strcpy (parkplatz, entries [index]);
	strcpy (entries [index], entries [index + 1]);
	strcpy (entries [index + 1], parkplatz);
}

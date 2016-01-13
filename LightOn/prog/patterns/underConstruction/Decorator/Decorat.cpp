// ====== Includes

#include <stdlib.h>  // exit (int status)
#include <iostream.h>

// ====== Classes

class TSoftPlc {
public:
	virtual void cycle () = 0;
};

class TSimPlc: public TSoftPlc {
public:
	virtual void cycle ();
};

class TWrapper: public TSoftPlc {
public:
	TWrapper (TSoftPlc *pSoftPlc);
	virtual void cycle ();
protected:
	TSoftPlc *pSoftPlc;
};

class TSeePlc: public TWrapper {
public:
	TSeePlc (TSoftPlc *pSoftPlc);
	virtual void cycle ();
	void exchangeGui ();
};

class TComPlc: public TWrapper {
public:
	TComPlc (TSoftPlc *pThisPlc, int otherPlcNr);
	virtual void cycle ();
	void exchangePlc ();
protected:
	int otherPlcNr;
};

// ====== Global functions

// --- Main program function

int main () {
	TSimPlc bareSoftPlc;
	TSeePlc softPlcWithGui (&bareSoftPlc);
	TComPlc
		softPlcWithGuiAnd1Peer (&softPlcWithGui, 2),
		softPlcWithGuiAnd2Peers (&softPlcWithGuiAnd1Peer, 3);



	cout <<
		endl << endl <<
		"1 = bare soft-PLC" << endl <<
		"2 = soft-PLC with GUI" << endl <<
		"3 = soft-PLC with GUI and 1 peer" << endl <<
		"4 = soft-PLC with GUI and 2 peers" << endl << endl <<
		"<configuration number> [enter] ";
	int choice = 0;
	cin >> choice;
	cout << endl;

	TSoftPlc *pSoftPlc;

	switch (choice) {  // They're all soft-PLC's of some kind
		case 1:
			pSoftPlc = &bareSoftPlc;
			break;
		case 2:
			pSoftPlc = &softPlcWithGui;
			break;
		case 3:
			pSoftPlc = &softPlcWithGuiAnd1Peer;
			break;
		case 4:
			pSoftPlc = &softPlcWithGuiAnd2Peers;
			break;
		default:
			exit (1);
			break;  // Redundant
	}

	for (;;) {
		pSoftPlc->cycle ();
	}

	return 0;
}

// ====== Member functions

// Member functions of class TSimPlc

void TSimPlc::cycle () {
	cout << endl << "process control signals" << endl;
}

// Member functions of class TWrapper

TWrapper::TWrapper (TSoftPlc *pSoftPlc): pSoftPlc (pSoftPlc) {
}

void TWrapper::cycle () {
	pSoftPlc->cycle ();
}

// Member functions of class TSeePlc

TSeePlc::TSeePlc (TSoftPlc *pSoftPlc): TWrapper (pSoftPlc) {
}

void TSeePlc::cycle () {
	TWrapper::cycle ();
	exchangeGui ();
}

void TSeePlc::exchangeGui () {
	cout << "exchange data with GUI" << endl;
}

// Member functions of class TComPlc

TComPlc::TComPlc (TSoftPlc *pSoftPlc, int otherPlcNr):
	TWrapper (pSoftPlc), otherPlcNr (otherPlcNr)
{
}

void TComPlc::cycle () {
	TWrapper::cycle ();
	exchangePlc ();
}

void TComPlc::exchangePlc () {
	cout << "exchange data with PLC " << otherPlcNr << endl;
}

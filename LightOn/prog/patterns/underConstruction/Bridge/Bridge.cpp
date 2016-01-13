// ====== Includes

#include <iostream.h>

// ====== Defines

#define BOOL int
#define FALSE 0
#define TRUE 1

// ====== Classes

// --- Implementation hierarchy

class TCharsImplem {
public:
	virtual int nrOfChars () = 0;
	virtual void setContents (char *s) = 0;
	virtual char charAt (int i) = 0;  // char *getContents () would help performance
};

class TCharsHeapArray: public TCharsImplem {
public:
	virtual char charAt (int i);
protected:
	TCharsHeapArray ();
	~TCharsHeapArray ();
	int setContentsAndReturnCharCount (char *s, BOOL zeroTerm);
	char *pContents;
};

class TCharsZeroTerm: public TCharsHeapArray {
public:
	virtual int nrOfChars ();
	virtual void setContents (char *s);
};

class TCharsLengthField: public TCharsHeapArray {
public:
	virtual int nrOfChars ();
	virtual void setContents (char *s);
private:
	int charCount;
};

// --- Implementation factory hierarchy

class TCharsImplemFactory {
public:
	virtual TCharsImplem *makeCharsImplem () = 0;
};

class TCharsZeroTermFactory: public TCharsImplemFactory {
public:
	virtual TCharsImplem *makeCharsImplem ();
};

class TCharsLengthFieldFactory: public TCharsImplemFactory {
public:
	virtual TCharsImplem *makeCharsImplem ();
};

// --- Functional hierarchy

class TChars {
public:
	TChars (char *s);
	~TChars ();
	int nrOfChars ();
	char charAt (int i);
	static TCharsImplemFactory *pCharsImplemFactory;
protected:
	TCharsImplem *pCharsImplem;
};

class TMessage: public TChars {
public:
	TMessage (char *s);
	void show ();
};

class TCharSet: public TChars {
public:
	TCharSet (char *s);
	BOOL contains (char c);
};

// ====== Global functions

// --- Main program function

int main () {
	cout << endl;

	TCharsImplemFactory *pCharsImplemFactory = NULL;

	{for (int i = 0; i < 4; i++) {
		// Following thought to reside in package that knows about implementations
		// "Lower abstraction layer"

		delete pCharsImplemFactory;  // Delete on a NULL pointer is harmless

		pCharsImplemFactory =
			i%2 == 0
			?
			(TCharsImplemFactory*) new TCharsZeroTermFactory
			:
			(TCharsImplemFactory*) new TCharsLengthFieldFactory;

		// Following thought to reside in package that does not know about implementations
		// "Higher abstraction layer"

		TChars::pCharsImplemFactory = pCharsImplemFactory;

		TMessage
			greenMessage ("Then you may drive on"),
			notGreenMessage ("Then you may have to stop");

		TCharSet continueAnswerSet ("yY");

		cout << "Was the green traffic light on? ";
		char answer = ' ';
		cin >> answer;

		if (continueAnswerSet.contains (answer)) {
			greenMessage.show ();
		}
		else {
			notGreenMessage.show ();
		}
	}}
	return 0;
}

// ====== Member functions

// --- Member functions of classes from implementation hierarchy

// class TCharsHeapArray

TCharsHeapArray::TCharsHeapArray () {
	pContents = NULL;
}

TCharsHeapArray::~TCharsHeapArray () {
	delete [] pContents;
}

char TCharsHeapArray::charAt (int i) {
	return pContents [i];
}

int TCharsHeapArray::setContentsAndReturnCharCount (char *s, BOOL zeroTerm) {
	int charCount = 0;

	{
		char *pChar = s;

		while (*pChar != '\0') {
			pChar++;
			charCount++;
		}
	}

	pContents = new char [charCount + (zeroTerm ? 1 : 0)];

	{
		char
			*pSource = s,
			*pTarget = pContents;

		while (*pSource != NULL) {
			*pTarget = *pSource;
			pSource++;
			pTarget++;
		}
	}

	return charCount;
}

// class TCharsZeroTerm

int TCharsZeroTerm::nrOfChars () {
	char *pChar = pContents;
	int charCount = 0;

	while (*pChar != NULL) {
		pChar++;
		charCount++;
	}

	return charCount;
}

void TCharsZeroTerm::setContents (char *s) {
	int charCount = setContentsAndReturnCharCount (s, TRUE);
	pContents [charCount] = '\0';
}

// class TCharsLengthField

int TCharsLengthField::nrOfChars () {
	return charCount;
}

void TCharsLengthField::setContents (char *s) {
	charCount = setContentsAndReturnCharCount (s, FALSE);

}

// --- Member functions of implementation factory hierarchy

// class TCharsImplemFactory

// class TCharsZeroTermFactory

TCharsImplem *TCharsZeroTermFactory::makeCharsImplem () {
	cout << "TCharsZeroTerm instantiated" << endl;
	return new TCharsZeroTerm;
}

// class TCharsLengthFieldFactory

TCharsImplem *TCharsLengthFieldFactory::makeCharsImplem () {
	cout << "TCharsLengthField instantiated" << endl;
	return new TCharsLengthField;
}


// --- Member functions and static data members of classes from functional hierarchy

// class TChars

TChars::TChars (char *s) {
	pCharsImplem = pCharsImplemFactory->makeCharsImplem ();
	pCharsImplem->setContents (s);
}

TChars::~TChars () {
	delete pCharsImplem;
}

int TChars::nrOfChars () {
	return pCharsImplem->nrOfChars ();
}

char TChars::charAt (int i) {
	return pCharsImplem->charAt (i);
}

TCharsImplemFactory *TChars::pCharsImplemFactory;

// class TMessage

TMessage::TMessage (char *s): TChars (s) {
}

void TMessage::show () {
	{for (int charIndex = 0; charIndex < nrOfChars (); charIndex++) {
		cout << charAt (charIndex);
	}}
	cout << endl;
}

// class TCharSet

TCharSet::TCharSet (char *s): TChars (s) {
}

BOOL TCharSet::contains (char c) {
	{for (int charIndex = 0; charIndex < nrOfChars (); charIndex++) {
		if (charAt (charIndex) == c) {
			return TRUE;
		}
	}}
	return FALSE;
}

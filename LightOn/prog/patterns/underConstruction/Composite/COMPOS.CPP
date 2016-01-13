// ====== Includes

#include <iostream.h>

// ====== Defines

#define NULL 0

// ====== Classes

class TConversationFragment {
public:
	TConversationFragment ();
	virtual void activate () = 0;
	virtual void add (TConversationFragment *pConversationFragment);
	virtual void remove (TConversationFragment *pConversationFragment);

	TConversationFragment *pNext;  // A conversation fragment may be part of a list
};

class TCompositeFragment: public TConversationFragment {
public:
	TCompositeFragment ();
	virtual void activate ();
	virtual void add (TConversationFragment *pConversationFragment);
	virtual void remove (TConversationFragment *pConversationFragment);

	TConversationFragment *pFirst;  // A composite fragment contains a list
};

class TTellMyName: public TConversationFragment {
public:
	virtual void activate ();
};

class TAskYourName: public TConversationFragment {
	virtual void activate ();
};

class TAskSum: public TConversationFragment {
	virtual void activate ();
};

class TTellPoem: public TConversationFragment {
	virtual void activate ();
};

class TSayGoodbye: public TConversationFragment {
	virtual void activate ();
};

// ====== Global functions

// --- Main program function

int main () {
	TTellMyName tellMyName;
	TAskYourName askYourName;

	TCompositeFragment getAcquainted;
	getAcquainted.add (&tellMyName);
	getAcquainted.add (&askYourName);

	TAskSum askSum;
	TTellPoem tellPoem;

	TCompositeFragment talkALittle;
	talkALittle.add (&askSum);
	talkALittle.add (&tellPoem);

	TSayGoodbye sayGoodbye;

	TCompositeFragment wholeConversation;
	wholeConversation.add (&getAcquainted);
	wholeConversation.add (&talkALittle);
	wholeConversation.add (&sayGoodbye);

	wholeConversation.activate ();

	return 0;
}

// ====== Member functions

// Member functions of class TConversationFragment

TConversationFragment::TConversationFragment () {
	pNext = NULL;
}

void TConversationFragment::add (TConversationFragment *pConversationFragment) {
	// Do nothing (is not the same as pure virtual!)
}

void TConversationFragment::remove (TConversationFragment *pConversationFragment) {
	// Do nothing (is not the same as pure virtual!)
}

// Member functions of class TCompositeFragment

TCompositeFragment::TCompositeFragment () {
	pFirst = NULL;
}

void TCompositeFragment::activate () {
	TConversationFragment *pCurrent = pFirst;
	while (pCurrent != NULL) {
		pCurrent->activate ();
		pCurrent = pCurrent->pNext;
	}
}

void TCompositeFragment::add (TConversationFragment *pConversationFragment) {
	TConversationFragment **ppCurrent = &pFirst;
	while (*ppCurrent != NULL) {
		ppCurrent = &((*ppCurrent)->pNext);
	}
	*ppCurrent = pConversationFragment;
}

void TCompositeFragment::remove (TConversationFragment *pConversationFragment) {
	// Not implemented
}

// Member functions of class TTellMyName
void TTellMyName::activate () {
	cout << "Hi, I am Patsy the Pattern Girl!" << endl << endl;
}

// Member functions of class TAskYourName

void TAskYourName::activate () {
	cout << "What's your name?" << endl;
	char name [100];
	cin >> name;
	cout <<
		"Well hi " << name <<
		", it's so nice to meet you!" << endl << endl;
}

// Member functions of class TAskSum

void TAskSum::activate () {
	cout << "Tell me, how much is 1 + 1? ";
	int answer;
	cin >> answer;
	if (answer == 2) {
		cout << "Wow, you're good at this!" << endl << endl;
	}
	else {
		cout << "Never mind, I don't know either!" << endl << endl;
	}
}

// Member functions of class TTellPoem

void TTellPoem::activate () {
	cout <<
		"Please do remember" << endl <<
		"The fifth of November" << endl <<
		"Treason and plot" << endl <<
		"I see no reason" << endl <<
		"Why the gunpowder treason" << endl <<
		"Should be ever, yes ever forgot" << endl << endl;
}

// Member functions of class TSayGoodbye

void TSayGoodbye::activate () {
	cout <<
		"Well, I've got to go now!" << endl <<
		"Goodbye!" << endl << endl;
}

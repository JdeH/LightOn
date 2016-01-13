// ====== Includes

#include <iostream.h>

// ====== Classes

// --- Calculators in general

class TEngine;

class TConsole {
public:
	void getInput (char *prompt, float &input);
	void getInput (char *prompt, char &input);  // Or use a function template
	virtual void showResult () = 0;

	TEngine *pEngine;
};

class TEngine {
public:
	void attachConsole (TConsole *pConsole);
	virtual void algorithm () = 0;
	void compute ();

	TConsole *pConsole;
	float
		firstOperand,
		secondOperand,
		result;
	char
		anOperator;
};

class TCalculatorFactory {				// Normally there would also be a
public:							// calculator "product", serving as
	virtual TConsole *makeConsole () = 0;		// a container for console and engine.
	virtual TEngine *makeEngine () = 0;		// It's make-function would probably
};							// make its parts and its destructor
							// would destroy them.
// --- Algebraic notation calculator

class TAnConsole: public TConsole {
public:
	void showResult ();
};

class TAnEngine: public TEngine {
public:
	void algorithm ();
};

class TAnCalculatorFactory: public TCalculatorFactory {
public:
	TConsole *makeConsole ();
	TEngine *makeEngine ();
};

// --- Reverse polish notation calculator

class TRpnConsole: public TConsole {
public:
	void showResult ();
};

class TRpnEngine: public TEngine {
public:
	void algorithm ();
};

class TRpnCalculatorFactory: public TCalculatorFactory {
public:
	TConsole *makeConsole ();
	TEngine *makeEngine ();
};

// ====== Global functions

// --- Main program function

int main () {
	{for (;;) {
		// What kind of calculator do you want?

		cout <<
			"a = algebraic notation calculator" << endl <<
			"r = reversed polish notation calculator" << endl <<
			"q = quit " << endl <<
			"<choice> [enter] ";

		char choice = ' ';
		cin >> choice;

		if (choice == 'q') {
			break;
		}

		TCalculatorFactory *pCalculatorFactory = NULL;

		// Make the right factory

		switch (choice) {
			case 'a':
				pCalculatorFactory = new TAnCalculatorFactory;
				break;
			case 'r':
				pCalculatorFactory = new TRpnCalculatorFactory;
				break;
			default:
				break;
		}

		// Let the factory make the parts of a calculator
		// They will be of the type that this factory specializes in

		TConsole *pConsole = pCalculatorFactory->makeConsole ();	// Normally done by
		TEngine *pEngine = pCalculatorFactory->makeEngine ();		// constructor of
										// calculator
		// Assemble the parts
		// They will match, because they came from the same factory

		pEngine->attachConsole (pConsole);		// Normally done by constructor
								// of calculator
		// Use the calculator

		char answer = ' ';
		do {
			pEngine->algorithm ();
			cout << "Use same calculator again? <y|n> [enter] ";
			cin >> answer;
		} while (answer == 'y');

		// Throw away parts, normally one would throw away just the calculator object

		delete pConsole;				// Normally done by destructor
		delete pEngine;					// of calculator
	}}
	return 0;
}

// ====== Member functions

// --- Member functions that have to do with general calculators

// class TConsole

void TConsole::getInput (char *prompt, float &input) {
	cout << prompt;
	cin >> input;
};

void TConsole::getInput (char *prompt, char &input) {
	cout << prompt;
	cin >> input;
};

// class TEngine

void TEngine::attachConsole (TConsole *pConsole) {
	TEngine::pConsole = pConsole;
	pConsole->pEngine = this;
};

void TEngine::compute () {
	switch (anOperator) {
		case '+':
			result = firstOperand + secondOperand;
			break;
		case '-':
			result = firstOperand - secondOperand;
			break;
		case '*':
			result = firstOperand * secondOperand;
			break;
		case '/':
			result = firstOperand / secondOperand;
			break;
	}
}

// --- Members functions that have to do with algebraic notation calculators

// class TAnCalculatorFactory

TConsole *TAnCalculatorFactory::makeConsole () {
	return new TAnConsole;
};

TEngine *TAnCalculatorFactory::makeEngine () {
	return new TAnEngine;
};

// class TAnConsole

void TAnConsole::showResult () {
	cout <<
		pEngine->firstOperand << " " <<
		pEngine->anOperator << " " <<
		pEngine->secondOperand << " = " <<
		pEngine->result << endl;
};

// class TAnEngine

void TAnEngine::algorithm () {
	pConsole->getInput ("<first operand>  [enter] ", firstOperand);
	pConsole->getInput ("<+|-|*|/>        [enter] ", anOperator);
	pConsole->getInput ("<second operand> [enter] ", secondOperand);
	compute ();
	pConsole->showResult ();
}

// --- Member functions that have to do with reverse polish notation calculators

// class TRpnCalculatorFactory

TConsole *TRpnCalculatorFactory::makeConsole () {
	return new TRpnConsole;
};

TEngine *TRpnCalculatorFactory::makeEngine () {
	return new TRpnEngine;
};

// class TRpnConsole

void TRpnConsole::showResult () {
	cout <<
		pEngine->firstOperand << " " <<
		pEngine->secondOperand << " " <<
		pEngine->anOperator << " --> " <<
		pEngine->result << endl;
};

// class TRpnEngine

void TRpnEngine::algorithm () {
	pConsole->getInput ("<first operand>  [enter] ", firstOperand);
	pConsole->getInput ("<second operand> [enter] ", secondOperand);
	pConsole->getInput ("<+|-|*|/>        [enter] ", anOperator);
	compute ();
	pConsole->showResult ();
}

// ====== Includes

#include <iostream.h>

// ====== Classes

// --- Abstract classes

class TRouteSegmenter {
public:
	virtual void move (char *sourceLocator, char *targetLocator) = 0;
	virtual void pause () = 0;
};

// --- Concrete classes

class TAscSequenceControl {
public:
	void get (char *sourceLocator);
	void put (char *targetLocator);
};

class TAscRouteSegmenter: public TRouteSegmenter, public TAscSequenceControl {
public:
	virtual void move (char *sourceLocator, char *targetLocator);
	virtual void pause ();
};

// ====== Global functions

// --- Main program function

int main () {  // Plays role of MovementPlanner to keep example brief
	TRouteSegmenter *pRouteSegmenter = NULL;
	// ... Code inbetween determines type of segmenter
	pRouteSegmenter = new TAscRouteSegmenter;  // Assignment, compiler doesn't know type

	pRouteSegmenter->move ("S1E3", "T7");      // Unknown that it's an ASC segmenter
	pRouteSegmenter->pause ();

	delete pRouteSegmenter;
	return 0;
}

// ====== Member functions

// --- Member functions of concrete classes

// class TAscSequenceControl

void TAscSequenceControl::get (char *sourceLocator) {
	cout << "Container picked up at " << sourceLocator << endl;
}

void TAscSequenceControl::put (char *targetLocator) {
	cout << "Container put down at " << targetLocator << endl;
}

// class TAscRouteSegmenter

void TAscRouteSegmenter::move (char *sourceLocator, char *targetLocator) {
	get (sourceLocator);
	put (targetLocator);
}

void TAscRouteSegmenter::pause () {
   cout <<
	"Function ""driveControl.pause ()"" called" << endl <<
	"Function ""manualControl.notifyPause ()"" called" << endl << endl;
}
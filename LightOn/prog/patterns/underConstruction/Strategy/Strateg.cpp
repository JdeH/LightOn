// ====== Includes

#include <iostream.h>
#include <stdlib.h>  // exit

// ====== Defines

#define tableSize 100
#define nrOfDimensions 3
#define dDummy 1.0

#define NULL 0

#define BOOL int
#define TRUE 1
#define FALSE 0

// ====== Classes

class TGonioStrategy {
public:
	virtual double sin (double angleInRadians) = 0;
	virtual double cos (double angleInRadians) = 0;
	virtual double tan (double angleInRadians) = 0;
	virtual char *getStrategyName () = 0;
};

class TGonioComputations: public TGonioStrategy {
public:
	virtual double sin (double angleInRadians);
	virtual double cos (double angleInRadians);
	virtual double tan (double angleInRadians);
	virtual char *getStrategyName ();
};

class TGonioTables: public TGonioStrategy {
public:
	TGonioTables ();
	virtual double sin (double angleInRadians);
	virtual double cos (double angleInRadians);
	virtual double tan (double angleInRadians);
	virtual char *getStrategyName ();
protected:
	double sinTable [tableSize];
	double cosTable [tableSize];
	double tanTable [tableSize];
};

class TRotationMatrix {
public:
	TRotationMatrix (TGonioStrategy *pGonioStrategy);
	fill (double pitch, double banking, double heading);
	double sin (double angleInRadians) {
		return pGonioStrategy->sin (angleInRadians);
	};
	double cos (double angleInRadians) {
		return pGonioStrategy->cos (angleInRadians);
	};
protected:
	double entries [nrOfDimensions][nrOfDimensions];
	TGonioStrategy *pGonioStrategy;
};

// ====== Global functions

// --- Main program function

int main () {
	for (;;) {
		cout <<
			"More than " << sizeof (TGonioTables) << 
			" bytes of free memory? <y/n/q(uit)> [enter] " << endl;
		char answer;
		cin >> answer;

		TGonioStrategy *pGonioStrategy;

		switch (answer) {
			case 'y':
				pGonioStrategy = new TGonioTables;
				break;
			case 'n':
				pGonioStrategy = new TGonioComputations;
				break;
			default:
				exit (0);
				break;  // Redundant
		}

		TRotationMatrix rotationMatrix (pGonioStrategy);

		for (int i = 0; i < 5; i++) {  // Simulate varying angles
			double
				pitch = 1.1 * i,
				banking = 1.01 * i,
				heading = 1.001 * i;

			rotationMatrix.fill (pitch, banking, heading);
			
			// Multiply rotation matrix with all vectors denoting vertices
		}

		delete pGonioStrategy;  // Leaves rotationMatrix in the cold
	}

	return 0;
}

// ====== Member functions

// Member functions of class TGonioComputations

double TGonioComputations::sin (double angleInRadians) {
	cout << "Compute sin (" << angleInRadians << ") with lib function" << endl;
	return dDummy;
}

double TGonioComputations::cos (double angleInRadians) {
	cout << "Compute cos (" << angleInRadians << ") with lib function" << endl;
	return dDummy;
}

double TGonioComputations::tan (double angleInRadians) {
	cout << "Compute tan (" << angleInRadians << ") with lib function" << endl;
	return dDummy;
}

char *TGonioComputations::getStrategyName () {
	return "TGonioComputations";
}

// Member functions of class TGonioTables

TGonioTables::TGonioTables () {
	cout << "Fill gonio-tables" << endl;
}

double TGonioTables::sin (double angleInRadians) {
	cout << "Interpolate sin (" << angleInRadians << ") from table" << endl;
	return dDummy;
}

double TGonioTables::cos (double angleInRadians) {
	cout << "Interpolate cos (" << angleInRadians << ") from table" << endl;
	return dDummy;
}

double TGonioTables::tan (double angleInRadians) {
	cout << "Interpolate tan (" << angleInRadians << ") from table" << endl;
	return dDummy;
}

char *TGonioTables::getStrategyName () {
	return "TGonioTables";
}

// Member functions of class TRotationMatrix

TRotationMatrix::TRotationMatrix (TGonioStrategy *pGonioStrategy) {
	TRotationMatrix::pGonioStrategy = pGonioStrategy;
	cout <<
		"Adopted strategy " << pGonioStrategy->getStrategyName () <<
		" <o(k)> [enter] ";
	char cDummy;
	cin >> cDummy;
}

TRotationMatrix::fill (double pitch, double banking, double heading) {
	// Compute entries from quotients of sines and cosine

	// Row 0
	entries [0][0] = cos (pitch) * cos (heading);
	entries [0][1] = cos (pitch) * cos (heading);
	entries [0][2] = sin (pitch);

	// Row 1
	entries [1][0] = -cos (banking) * sin (heading) -
		sin (banking) * sin (pitch) * cos (heading);
	entries [1][1] = -cos (banking) * cos (heading) -
		sin (banking) * sin (pitch) * sin (heading);
	entries [1][2] = sin (banking) * cos (pitch);

	// Row 2
	entries [2][0] = sin (banking) * sin (heading) -
		cos (banking) * sin (pitch) * cos (heading);
	entries [2][1] = -sin (banking) * cos (heading) -
		cos (banking) * sin (pitch) * sin (heading);
	entries [2][2] = cos (banking) * cos (pitch);
}

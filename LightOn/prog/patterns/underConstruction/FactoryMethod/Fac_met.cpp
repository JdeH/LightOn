// ====== Includes

#include <iostream.h>

// ====== Typedefs

typedef int BOOL;

// ====== Classes

// --- Abstract classes

class TPropertyDialog {
public:
	virtual void run () = 0;
};

class TGuiElement {
public:
	void setProperties ();
	virtual void show () = 0;
protected:
	virtual TPropertyDialog &createPropertyDialog () = 0;
	void deletePropertyDialog (TPropertyDialog &propertyDialog);
};

// --- Concrete classes

class TMenu: public TGuiElement {
	friend class TMenuPropertyDialog;
public:
	TMenu ();
	virtual void show ();
protected:
	virtual TPropertyDialog &createPropertyDialog ();

	BOOL
		isFloating,
		hasSystemSubmenu;
};

class TMenuPropertyDialog: public TPropertyDialog {
public:
	TMenuPropertyDialog (TMenu *pMenu);
protected:
	virtual void run ();

	TMenu *pMenu;
};

// ====== Global functions

// --- Main program function

int main () {
	TGuiElement *pGuiElement = NULL;

	// ... Code inbetween determines at run time which type of GUI element
	// is instantiated

	pGuiElement = new TMenu;
	pGuiElement->setProperties ();
	pGuiElement->show ();
	delete pGuiElement;

	return 0;
}

// ====== Member functions

// --- Member functions of abstract classes

// class TGuiElement

void TGuiElement::setProperties () {
	TPropertyDialog &propertyDialog = createPropertyDialog ();
	propertyDialog.run ();
	deletePropertyDialog (propertyDialog);
};

void TGuiElement::deletePropertyDialog (TPropertyDialog &propertyDialog) {
	delete &propertyDialog;
}

// --- Members functions of concrete classes

// class TMenu

TMenu::TMenu () {
	cout << endl << endl << "Menu created" << endl;
}

void TMenu::show () {
	if (isFloating) {
		cout << "Floating menu shown ";
	}
	else {
		cout << "Docked menu shown ";
	}

	if (hasSystemSubmenu) {
		cout << "with system submenu";
	}
	else {
		cout << "without system submenu";
	}
}

TPropertyDialog &TMenu::createPropertyDialog () {
	return *(new TMenuPropertyDialog (this));
}

// class TMenuPropertyDialog

TMenuPropertyDialog::TMenuPropertyDialog (TMenu *pMenu): pMenu (pMenu) {
}

void TMenuPropertyDialog::run () {
	cout << "Menu property dialog launched" << endl;

	char answer;

	cout << "Floating menu <y/n> [enter] ";
	cin >> answer;
	pMenu->isFloating = (answer == 'y');

	cout << "Insert system submenu <y/n> [enter] ";
	cin >> answer;
	pMenu->hasSystemSubmenu = (answer == 'y');
}

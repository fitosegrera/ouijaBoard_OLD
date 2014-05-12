//
//
// ouija.h
// Created by fito_segrera
//
//

#pragma once

#include "ofMain.h"
#include "ofxOsc.h"

#define PORT 9000

using namespace std; // This is for avoiding typing std::string for declaring strings

class ouija{
	public:
		ofxOscReceiver receiver;
		ofImage boardImgBg;
		ofImage boardImgOuija;
		ofImage boardImgH;
		ofImage boardImgI;
		ofImage boardImgT;
		ofImage boardImgL;
		ofImage boardImgE;
		ofImage boardImgR;
		string argument;
		bool drawOuija = false;
		bool drawH = false;
		bool drawI = false;
		bool drawT = false;
		bool drawL = false;
		bool drawE = false;
		bool drawR = false;
		void setupBoard();
		void drawBoard(string title);
		ofTrueTypeFont myfont;
};

//#endif
// defined(__firstClassOnClasses__Person__)
